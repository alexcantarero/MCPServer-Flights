from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
def write_file(full_file_path: str, content: str) -> str:
    """
    Write content directly to a specific file path (including directory and filename).
    
    Args:
        full_file_path: Complete path including directory and filename
        content: Content to write to the file
    
    Returns:
        Success message with the file path
    """
    import os
    
    try:
        # Convertir a path absoluto
        abs_filepath = os.path.abspath(full_file_path)
        
        # Crear el directorio correspondiente si no existe
        directory = os.path.dirname(abs_filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)
        
        # Escribir el contenido en el fichero
        with open(abs_filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
        return f"File successfully created at: {abs_filepath}"
    
    except PermissionError:
        return f"Error: Permission denied to write to {full_file_path}"
    except Exception as e:
        return f"Error writing file: {str(e)}"


# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


# Add a prompt
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    """Generate a greeting prompt"""
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
    }

    return f"{styles.get(style, styles['friendly'])} for someone named {name}."