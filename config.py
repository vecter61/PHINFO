import os
import json
from rich.console import Console

CONFIG_FILE = "config.json"
console = Console()

API_METADATA = {
    "abstract_api_key": {
        "name": "Abstract API",
        "url": "https://www.abstractapi.com/phone-validation-api"
    },
    "numverify_api_key": {
        "name": "NumVerify API",
        "url": "https://numverify.com"
    },
    "truecaller_token": {
        "name": "Truecaller Token",
        "url": "https://github.com/sumitrathi/truecallerpy"
    }
}

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

def ensure_api_keys():
    config = load_config()
    updated = False

    for key, meta in API_METADATA.items():
        if key not in config or not config[key]:
            console.print(f"\n[bold yellow]{meta['name']} key not found.[/bold yellow]")
            console.print(f"[cyan]You can get it from: {meta['url']}[/cyan]")
            entered = console.input(f"[green]Enter {meta['name']} key (MINIMUM ONE REQUIRED TO WORK PROPERLY or leave blank to skip): [/green]").strip()
            if entered:
                config[key] = entered
                updated = True

    if updated:
        save_config(config)
        console.print("\n[bold green]Saved API keys to config.json[/bold green]")

    return config
