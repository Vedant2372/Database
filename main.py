from query_sender import send_query_to_api
from utils import format_results

def cli():
    print("🧠 Welcome to Document Finder CLI!")
    print("Type your query (e.g., 'invoice', 'project report') or type 'exit' to quit.\n")

    while True:
        query = input("🔍 Query: ").strip()
        if query.lower() == "exit":
            print("👋 Exiting CLI. Goodbye!")
            break

        results = send_query_to_api(query)
        print("[DEBUG] Raw results from API:", results)
        print(format_results(results.get("results", [])))  # ✅ Safely pass just the list

if __name__ == "__main__":
    cli()
