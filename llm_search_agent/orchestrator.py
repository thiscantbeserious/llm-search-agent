from pydantic import BaseModel
from typing import List, Dict, Any
from langgraph.graph import StateGraph, END

from llm_search_agent.config import Settings
from llm_search_agent.pipeline.agents.intent_agent import IntentAgent
from llm_search_agent.pipeline.agents.search_agent import SearchAgent
from llm_search_agent.pipeline.agents.filter_agent import FilterAgent
from llm_search_agent.pipeline.agents.scoring_agent import ScoringAgent
from llm_search_agent.pipeline.agents.answer_agent import AnswerAgent

class State(BaseModel):
    query: str
    intent: str = ""
    results: List[Dict[str, Any]] = []
    filtered: List[Dict[str, Any]] = []
    answer: str = ""

cfg = Settings()
ia = IntentAgent()
sa = SearchAgent()
fa = FilterAgent()
sca = ScoringAgent()
aa = AnswerAgent()

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
    init = State(query=query)
    final: State = graph.run(init)
    return final
