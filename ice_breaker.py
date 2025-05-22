from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from agents.linkedin_lookup_agent import lookup
from third_parties.linkedin import scrape_linkedin_profile


def ice_break_with(name: str="Mengni Zhang Berlin", mock: bool=False) -> str:
    
    if mock:
        linkedin_data = scrape_linkedin_profile(mock=True)
    else:
        linkedin_url = lookup(name=name)
        linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url, mock=False)
    
    summary_template = """
        given the LinkedIn information {information} about a person. I want you to create:
        1. a short summary
        2. two interesting facts about them
    """
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = ChatOpenAI(temperature=0, model_name="gpt-4.1-nano")
    chain = summary_prompt_template | llm | StrOutputParser()
    chain_result = chain.invoke(input={"information": linkedin_data})
    
    print(chain_result)

if __name__ == "__main__":
    load_dotenv()
    
    print("Ice Breaker Enter")
    ice_break_with(mock = True)
    