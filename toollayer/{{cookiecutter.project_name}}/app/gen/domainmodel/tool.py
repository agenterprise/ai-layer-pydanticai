from pydantic import BaseModel
import enum


class ToolType(str, enum.Enum):
    CODE = "aiurn:tooltype:code"
    RESSOURCE = "aiurn:tooltype:ressource"
    OPENAPI = "aiurn:tooltype:openapi"
    MCP = "aiurn:tooltype:mcp"
    CUSTOM = "aiurn:tooltype:custom"
    

class AbstractTool(BaseModel):
    """Abstract base class for tools."""
    async def call(self, query: str):
        pass

    async def prepare(self, query: str):
        pass

class MCPNotAvailableException(Exception):
    pass


    