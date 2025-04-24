import sys
from llm_search_agent.orchestrator import run_pipeline


def execute():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your question here\"")
        sys.exit(1)
    query = " ".join(sys.argv[1:])
    state = run_pipeline(query)
    print(state.json(indent=2))


if __name__ == "__main__":
    execute()
