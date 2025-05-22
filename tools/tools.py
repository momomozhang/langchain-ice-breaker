from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str):
    """Searches for LinkedIn Profile page url"""
    search = TavilySearchResults()
    response = search.run(f"{name}")
    return response