import sys 
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain import hub
from tools.tools import get_profile_url_tavily

def lookup(name:str) -> str:
    llm = ChatOpenAI(temperature=0, model="gpt-4.1-nano") 
    
    template = """
        Given the full name {name_of_person}. 
        Please get the url to their Linkedin profile page. 
        Your answer should contain only a url starting with "http"
    """
    prommpt_template = PromptTemplate(input_variables=["name_of_person"], template=template)
    
    tools_for_agent = [
        Tool(
            name = "Crawl Google to get Linkedin profile page",
            func= get_profile_url_tavily,
            description="useful for when you need get the Linkedin Page url",
        )
    ]
    
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)
    
    result = agent_executor.invoke(
        input={"input":prommpt_template.format_prompt(name_of_person=name)}
    )
    
    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if __name__ == "__main__":
    print(lookup("Mengni Zhang Berlin"))