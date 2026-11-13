from typing import Any

import httpx2
from mcp.server import MCPServer

# Initialize MCPServer
mcp = MCPServer("weather")

# Constants
NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"