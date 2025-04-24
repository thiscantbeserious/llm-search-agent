from pydantic import BaseModel
from typing import List, Dict, Any
from langgraph.graph import StateGraph, END

from llm_search_agent.config import Config
from llm_search_agent.agents.intent_agent import IntentAgent
from llm_search_agent.agents.search_agent import SearchAgent
from llm_search_agent.agents.filter_agent import FilterAgent
from llm_search_agent.agents.scoring_agent import ScoringAgent
from llm_search_agent.agents.refinement_agent import RefinementAgent


class State(BaseModel):
    query: str
    intent: str = ""
    results: List[Dict[str, Any]] = []
    filtered: List[Dict[str, Any]] = []
    answer: str = ""


cfg = Config()
ia = IntentAgent()
sa = SearchAgent()
fa = FilterAgent()
sca = ScoringAgent()
aa = RefinementAgent()

builder = StateGraph(State)
builder.add_node("extract_intent", lambda s: {"intent": ia.extract(s.query)})
builder.add_node("perform_search", lambda s: {"results": sa.search(s.intent)})
builder.add_node("filter_results", lambda s: {"filtered": fa.filter(s.results)})
builder.add_node("score_results", lambda s: {"filtered": sca.score(s.filtered)})
builder.add_node("synthesize_answer", lambda s: {"answer": aa.generate(s.query, s.filtered)})

builder.set_entry_point("extract_intent")
builder.add_edge("extract_intent", "perform_search")
builder.add_edge("perform_search", "filter_results")
builder.add_edge("filter_results", "score_results")
builder.add_edge("score_results", "synthesize_answer")
builder.add_edge("synthesize_answer", END)

graph = builder.compile()


def run_pipeline(query: str) -> State:
    # 1) Build your initial state model
    init = State(query=query)

    # 2) Invoke the compiled graph with a dict
    #    (you can also pass init.dict() if you prefer)
    output_dict = graph.invoke(init.dict())

    # 3) Turn the result back into your Pydantic State
    return State(**output_dict)
