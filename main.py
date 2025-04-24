import sys
from llm_search_agent.orchestrator import run_pipeline

if __name__ == "__main__":
    # if len(sys.argv) < 2:
    #     print("Usage: python main.py \"Your question here\"")
    #     sys.exit(1)
    # query = " ".join(sys.argv[1:])
    state = run_pipeline("Ich hätte gerne die aktuelle Uhrzeit, ich habe gehört google.com ist eine gute Quelle dafür. Oder war es duckduckgo.com?")
    print(state.json(indent=2))
