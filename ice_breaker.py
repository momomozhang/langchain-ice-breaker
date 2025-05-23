from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from agents.linkedin_lookup_agent import lookup
from third_parties.linkedin import scrape_linkedin_profile
from output_parsers import summary_parser, Summary
from typing import Tuple



def ice_break_with(name: str="Mengni Zhang Berlin", mock: bool=False) -> Tuple[Summary, str]:
    
    if mock:
        linkedin_data = scrape_linkedin_profile(mock=True)
    else:
        linkedin_url = lookup(name=name)
        linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url, mock=False)
    
    summary_template = """
        given the LinkedIn information {information} about a person. I want you to create:
        1. a short summary
        2. two interesting facts about them
        \n{format_instructions}
    """
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], 
        template=summary_template,
        partial_variables={"format_instructions":summary_parser.get_format_instructions()},
        )
    llm = ChatOpenAI(temperature=0, model_name="gpt-4.1-nano")
    chain = summary_prompt_template | llm | summary_parser
    chain_result:Summary = chain.invoke(input={"information": linkedin_data})
    
    return chain_result, linkedin_data.get("photoUrl")

if __name__ == "__main__":
    load_dotenv()
    
    print("Ice Breaker Enter")
    ice_break_with(mock = False)
    