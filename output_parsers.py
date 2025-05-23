from typing import List, Dict, Any
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class Summary(BaseModel):
    summary: str = Field(description="summary")
    facts: List[str] = Field(description="interesting facts about them")
    ice_breakers: List[str] = Field(description="ice breaker questions to ask them")
    topics_of_interest: List[str] = Field(description="topics that may interest them")
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "summary": self.summary,
            "facts": self.facts,
            "ice_breakers": self.ice_breakers,
            "topics_of_interest": self.topics_of_interest,
            }
    
summary_parser = PydanticOutputParser(pydantic_object=Summary)