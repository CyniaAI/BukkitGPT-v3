import os
from dotenv import load_dotenv
from log_writer import logger


def load_config():
    """
    Loads the configuration from the ``.env`` file and sets the global
    variables accordingly.

    If the ``GENERATION_MODEL`` key in the configuration is set to ``gpt-4``,
    the function forces the use of ``gpt-4-turbo-preview`` as the value for this
    key since ``gpt-4`` no longer supports JSON modes.

    Returns:
        None
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Configuration keys that should be loaded
    config_keys = [
        'LLM_PROVIDER', 'API_KEY', 'BASE_URL', 'GENERATION_MODEL', 'FIXING_MODEL',
        'VERSION_NUMBER', 'SYS_GEN', 'USR_GEN', 'SYS_EDIT', 'USR_EDIT'
    ]
    
    for key in config_keys:
        value = os.getenv(key, '')
        globals()[key] = value
        logger(f"config: {key} -> {value if key != 'API_KEY' else '********'}")


def edit_config(key, value):
    """
    Edits the config file (.env).

    Args:
        key (str): The key to edit.
        value (str): The value to set.

    Returns:
        bool: True
    """
    env_file_path = '.env'
    
    # Read current .env file content
    env_lines = []
    try:
        with open(env_file_path, "r", encoding='utf-8') as f:
            env_lines = f.readlines()
    except FileNotFoundError:
        # If .env doesn't exist, create it
        pass
    
    # Update or add the key-value pair
    key_found = False
    for i, line in enumerate(env_lines):
        if line.strip().startswith(f"{key}="):
            if isinstance(value, bool):
                write_value = "true" if value else "false"
            else:
                write_value = str(value)
            env_lines[i] = f"{key}={write_value}\n"
            key_found = True
            break
    
    # If key wasn't found, add it
    if not key_found:
        if isinstance(value, bool):
            write_value = "true" if value else "false"
        else:
            write_value = str(value)
        env_lines.append(f"{key}={write_value}\n")
    
    # Write back to .env file
    with open(env_file_path, "w", encoding='utf-8') as f:
        f.writelines(env_lines)

    return True


load_config()
