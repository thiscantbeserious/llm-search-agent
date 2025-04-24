from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

from llm_search_agent.config import Config
from llm_search_agent.orchestrator import run_pipeline

v1 = FastAPI(title="LLM Search Agent API")
cfg = Config()


class QueryRequest(BaseModel):
    query: str


@v1.get("/health")
async def health_check():
    """
    Simple health check:
    - Returns 200 OK and JSON {"status":"ok"}
      when the API is fully up and ready.
    """
    return {"status": "ok"}


@v1.post("/search")
async def search_endpoint(req: QueryRequest):
    q = req.query.strip()
    if not q:
        raise HTTPException(status_code=400, detail="Empty query")
    try:
        state = run_pipeline(q)
        return state.dict()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def start(host: str | None = None, port: int | None = None, reload: bool = True):
    uvicorn.run("llm_search_agent.runners.rest_api:v1", host=host or cfg.api_host, port=port or cfg.api_port,
                reload=reload)


if __name__ == "__main__":
    start()
