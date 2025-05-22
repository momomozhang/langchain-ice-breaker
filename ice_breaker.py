from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    load_dotenv()
    
    print("Hello LangChain")
    
    summary_template = """
        given the LinkedIn information {information} about a person. I want you to create:
        1. a short summary
        2. two interesting facts about them
    """
    
    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    
    # llm = ChatOpenAI(temperature=0, model_name="gpt-4.1-nano")
    llm = ChatOllama(temperature=0, model= "llama3.2")
    
    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://gist.github.com/momomozhang/8d758dd057d4acdd4d622cbc0f3d5762/raw", mock=True)
    chain_result = chain.invoke(input={"information": linkedin_data})
    
    print(chain_result)