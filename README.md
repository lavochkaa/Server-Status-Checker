# Server Status Checker

Server Status Checker is a small Python project for checking whether websites or APIs are online. It reads a list of server URLs from a text file, sends a request to each one, and prints the result in the console.

## Features

- Checks multiple servers from a simple text file
- Uses the `requests` library for HTTP requests
- Measures response time in milliseconds
- Shows whether each server is online or offline
- Handles connection errors with simple user-friendly messages
- Keeps the code readable and beginner-friendly

## Installation

1. Make sure Python 3 is installed.
2. Install the required library:

```bash
pip3 install -r requirements.txt
```

## How to Run

1. Add the server URLs you want to check in `servers.txt`.
2. Run the script:

```bash
python3 main.py
```

If you see an error about `requests`, install the dependency first:

```bash
pip3 install -r requirements.txt
```

## Example `servers.txt`

```text
https://google.com
https://api.github.com
https://example.com
```

## Example Output

```text
Checking servers...

google.com - ONLINE (80ms)
api.github.com - ONLINE (120ms)
example.com - ONLINE (95ms)

Done.
```
