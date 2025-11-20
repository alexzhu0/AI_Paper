import json
from langchain.tools import tool
from perplexity import Perplexity
from config import PERPLEXITY_API_KEY

@tool
def web_searcher(query: str) -> str:
    """
    A tool for performing web searches and getting up-to-date information.
    It uses the Perplexity API to search the web and returns the most relevant results.
    """
    try:
        client = Perplexity(api_key=PERPLEXITY_API_KEY)
        
        # Try using the search endpoint as suggested
        # Note: If 'search' is not available in the SDK version, we might need to fallback to chat
        # But based on user input, we assume it exists.
        
        # Check if client has search attribute to be safe, or just try it
        if hasattr(client, 'search'):
            try:
                search_response = client.search.create(
                    query=query,
                    max_results=5,
                    max_tokens_per_page=1024
                )
                
                results_text = ""
                for result in search_response.results:
                    # Use 'snippet' instead of 'content' as per inspection
                    content = getattr(result, 'snippet', getattr(result, 'text', ''))
                    results_text += f"Title: {result.title}\nURL: {result.url}\nContent: {content}\n\n"
                
                return results_text if results_text else "No results found."
            except Exception as search_error:
                print(f"[WARNING] Search endpoint failed: {search_error}. Falling back to chat completions.")
                # Fall through to chat completion fallback
                pass
            
        # Fallback to chat completions if search is not available or failed
        # This uses the 'sonar' model which has online capabilities
        messages = [
            {"role": "system", "content": "You are an AI assistant that provides concise and accurate information."},
            {"role": "user", "content": query}
        ]
        
        completion = client.chat.completions.create(
            model="sonar",
            messages=messages
        )
        
        return completion.choices[0].message.content

    except Exception as e:
        return f"An error occurred while using Perplexity SDK: {e}"

if __name__ == '__main__':
    # For testing the tool directly
    query = "What are the latest advancements in AI chips?"
    print(web_searcher.run(query))
