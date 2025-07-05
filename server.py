
from dotenv import load_dotenv
import os
import requests
from fastmcp import FastMCP

mcp = FastMCP(name="MCP Server with tools to get Weather")

load_dotenv()


@mcp.tool
def get_weather(city_name):
    """
    Fetches current time and weather condition for a given city using Weatherstack API.

    Args:
        city_name (str): Name of the city.

    Returns:
        dict: A dictionary with 'local_time' and 'weather_description', or an error message.
    """
    base_url = os.getenv("WEATHERSTACK_API_URL")
    params = {
        'access_key': os.getenv("WEATHERSTACK_API_KEY"),
        'query': city_name
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    # Check for errors in API response
    if 'error' in data:
        return {"error": data['error'].get('info', 'Unknown error')}

    # Extract current weather details
    local_time = data['location']['localtime']
    weather_desc = data['current']['weather_descriptions'][0]

    return {
        'local_time': local_time,
        'weather_description': weather_desc
    }

if __name__ == "__main__":
    # Start the server
    # You can access the server at http://localhost:8002
    mcp.run(
        transport="http",
        port=8002,
        )
    print("Weather MCP Server is running...") 