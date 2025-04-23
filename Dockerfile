
FROM python:3.11-slim

WORKDIR /llm_search_agent

COPY pyproject.toml poetry.lock* ./

RUN pip install --no-cache-dir poetry \
 && poetry config virtualenvs.create false \
 && poetry install --no-root --no-interaction --no-ansi

COPY . .

CMD ["python", "main.py"]
