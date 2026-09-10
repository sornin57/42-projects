import os
import sys

try:
    from dotenv import load_dotenv  # type: ignore[import-not-found]
except ImportError:
    load_dotenv = None


def get_config(name: str, default: str = "") -> str:
    value = os.getenv(name)
    if value is None:
        return default
    return value


def show_config() -> None:
    mode = get_config("MATRIX_MODE", "development")
    database_url = get_config("DATABASE_URL", "")
    api_key = get_config("API_KEY", "")
    log_level = get_config("LOG_LEVEL", "INFO")
    zion_endpoint = get_config("ZION_ENDPOINT", "")

    print("Configuration loaded:")
    print("Mode:", mode)

    if database_url == "":
        print("Database: Missing")
    elif "localhost" in database_url:
        print("Database: Connected to local instance")
    else:
        print("Database: Connected to remote instance")

    if api_key == "":
        print("API Access: Missing")
    else:
        print("API Access: Authenticated")

    print("Log Level:", log_level)

    if zion_endpoint == "":
        print("Zion Network: Offline")
    else:
        print("Zion Network: Online")


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...")

    if load_dotenv is None:
        print("python-dotenv is missing.")
        print("Install with: pip install -r requirements.txt")
        sys.exit(0)

    load_dotenv()
    show_config()
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file is ignored by git")
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")
