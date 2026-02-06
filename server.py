from mcp.server import Server
from mcp.server.stdio import stdio_server
import asyncio
import sys

async def main():
    server = Server("tally-prime")
    
    # Define tools
    @server.list_tools()
    async def list_tools():
        return [
            {
                "name": "get_tally_companies",
                "description": "Get list of companies from Tally",
                "inputSchema": {"type": "object", "properties": {}}
            }
        ]
    
    @server.call_tool()
    async def call_tool(name: str, arguments: dict):
        if name == "get_tally_companies":
            return {"companies": ["Company 1", "Company 2"]}
        return {"error": "Unknown tool"}
    
    # Run server
    async with stdio_server() as streams:
        await server.run(*streams, server.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
