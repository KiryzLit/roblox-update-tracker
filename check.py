import requests
import os

WEBHOOK = os.getenv("DISCORD_WEBHOOK")

VERSION_URL = "https://setup.roblox.com/version"

def get_version():
    return requests.get(VERSION_URL).text.strip()

def send(version):
    data = {
        "content": f"🚨 Roblox Update Detected!\nNew Version: `{version}`"
    }
    requests.post(WEBHOOK, json=data)

def main():
    try:
        with open("last.txt", "r") as f:
            last = f.read().strip()
    except:
        last = ""

    new = get_version()

    if new != last:
        send(new)
        with open("last.txt", "w") as f:
            f.write(new)

if __name__ == "__main__":
    main()
