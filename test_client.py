import asyncio
from fastmcp import Client

client = Client("http://127.0.0.1:8002/mcp")

async def main():
    async with client:
        # Get the available tools/operations
        tools = await client.list_tools()
        #print("Available tools:", tools)

        # Call the 'get_weather' tool with a city name
        response = await client.call_tool("get_weather", {"city_name": "Bangalore"})
        print("Response=", response[0].text)

asyncio.run(main())