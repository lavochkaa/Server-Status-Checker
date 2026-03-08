import time
from urllib.parse import urlparse

import requests


DEFAULT_TIMEOUT = 5
SERVERS_FILE = "servers.txt"


def load_servers(file_path):
    """Load server URLs from a text file."""
    servers = []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                url = line.strip()
                if url:
                    servers.append(url)
    except FileNotFoundError:
        print(f"Could not find {file_path}.")
        return []

    return servers


def get_server_name(url):
    """Return a simple name for display in the console."""
    parsed_url = urlparse(url)
    return parsed_url.netloc or url


def check_server(url):
    """Check whether a server is online and measure response time."""
    start_time = time.time()

    try:
        response = requests.get(url, timeout=DEFAULT_TIMEOUT)
        response_time = round((time.time() - start_time) * 1000)

        if response.ok:
            return True, response_time

        return False, response_time
    except requests.exceptions.RequestException:
        return False, None


def print_server_status(url, is_online, response_time):
    """Print a friendly status message for one server."""
    server_name = get_server_name(url)

    if is_online:
        print(f"{server_name} - ONLINE ({response_time}ms)")
    else:
        print(f"{server_name} - OFFLINE")


def main():
    print("Checking servers...\n")

    servers = load_servers(SERVERS_FILE)

    if not servers:
        print("No servers found to check.")
        print("\nDone.")
        return

    for server_url in servers:
        is_online, response_time = check_server(server_url)
        print_server_status(server_url, is_online, response_time)

    print("\nDone.")


if __name__ == "__main__":
    main()
