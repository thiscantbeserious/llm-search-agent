import sys
from llm_search_agent.orchestrator import run_pipeline


def repl():
    """Read–Eval–Print Loop for continuous queries."""
    banner = "LLM Search Agent REPL. Type 'exit()' or 'quit()' to stop."
    print(banner)
    while True:
        try:
            query = input("Query> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not query:
            continue
        if query.lower() in ("exit()", "quit()"):
            print("Goodbye!")
            break

        try:
            state = run_pipeline(query)
            print(state.json(indent=2))
        except Exception as e:
            print(f"[Error] {e}", file=sys.stderr)


if __name__ == "__main__":
    repl()
