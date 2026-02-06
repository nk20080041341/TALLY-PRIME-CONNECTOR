from fastmcp import FastMCP

mcp = FastMCP("Tally MCP")

@mcp.tool()
def hello():
    return "MCP server is working!"

app = mcp.sse_app()
