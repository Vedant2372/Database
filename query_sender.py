### query_sender.py
import requests

def send_query_to_api(query: str, api_url="http://127.0.0.1:5005/search"):
    try:
        response = requests.get(api_url, params={"q": query})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"[ERROR] Failed to get results from search API: {e}")
        return {"results": []}