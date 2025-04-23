import requests

class OllamaClient:
    def __init__(self, api_url: str):
        self.api_url = api_url.rstrip('/')
        self.headers = {'Content-Type':'application/json'}

    def chat(self, model: str, prompt: str) -> str:
        payload = {"model": model, "messages":[{"role":"user","content":prompt}]}
        resp = requests.post(
            f"{self.api_url}/chat/completions",
            json=payload,
            headers=self.headers,
            timeout=30
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()
