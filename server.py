from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "protocol": "mcp",
        "name": "Tally MCP",
        "version": "1.0"
    }
