import os
import requests
from dotenv import load_dotenv

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool=False):
    """scrape information from LinkedIn profile url,
    Manually scrape the information from the LinkedIn profile
     """
    if mock:
        response = requests.get(
            linkedin_profile_url,
            timeout=10
        )
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10
        )
    data = response.json().get("person")
    data = {key:value for key, value in data.items() if value not in ([], "", "", None)}
    
    return data

if __name__ == "__main__":
    print(scrape_linkedin_profile(linkedin_profile_url="https://gist.github.com/momomozhang/8d758dd057d4acdd4d622cbc0f3d5762/raw", mock=True))