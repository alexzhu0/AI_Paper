
import httpx
import json
from langchain.tools import tool
from config import PERPLEXITY_API_KEY, PERPLEXITY_API_URL

@tool
def web_searcher(query: str) -> str:
    """
    A tool for performing web searches and getting up-to-date information.
    It uses the Perplexity API to search the web and returns the most relevant results.
    """
    url = PERPLEXITY_API_URL + "/chat/completions"
    payload = {
        "model": "sonar-small-online",
        "messages": [
            {"role": "system", "content": "You are an AI assistant that provides concise and accurate information."},
            {"role": "user", "content": query}
        ]
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}"
    }

    try:
        with httpx.Client() as client:
            response = client.post(url, json=payload, headers=headers, timeout=30.0)
            response.raise_for_status()  # Raise an exception for bad status codes
            result = response.json()
            # Extract the content from the response
            if result.get("choices") and len(result["choices"]) > 0:
                content = result["choices"][0]["message"]["content"]
                return content
            else:
                return "No content found in the response."
    except httpx.RequestError as e:
        return f"An error occurred while requesting from Perplexity API: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

if __name__ == '__main__':
    # For testing the tool directly
    query = "What are the latest advancements in AI chips?"
    search_result = web_searcher.run(query)
    print(search_result)
