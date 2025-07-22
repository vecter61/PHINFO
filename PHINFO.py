from rich.console import Console
from rich.table import Table
from config import ensure_api_keys
from core import offline_lookup
from apis.abstract_api import query_abstract
from apis.numverify_api import query_numverify
from apis.truecaller_api import query_truecaller
import phonenumbers


from colorama import Fore, Style, init
init(autoreset=True)

print(Fore.CYAN + " ______ _   _ _____ _   _ ______ _____  ")
print(Fore.CYAN + "| ___ \\ | | |_   _| \\ | ||  ___|  _  | ")
print(Fore.WHITE + "| |_/ / |_| | | | |  \\| || |_  | | | | ")
print(Fore.WHITE + "|  __/|  _  | | | | . ` ||  _| | | | | ")
print(Fore.MAGENTA + "| |   | | | | | | | |\\  || |   \\ \\_/ / ")
print(Fore.MAGENTA + "\\_|   \\_| |_/\\___/\\_| \\_/\\_|    \\___/  ")
print(Style.RESET_ALL + "Welcome to PHINFO - Advanced Phone Number Info Tool By Vecter61\n")
print(Fore.YELLOW + '''Support / Donations

If you find PHINFO useful, consider supporting the project via Bitcoin:

bc1qlpw590fkykfdd9v92g9snfmx8hc8vwxvkz5npm\n''')


console = Console()

def show_data(title, data):
    table = Table(title=title)
    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    for k, v in data.items():
        table.add_row(k, str(v))

    console.print(table)

def analyze_number(full_number, region_code):
    console.rule(f"[bold blue]Analyzing: {full_number}[/bold blue]")

    # Offline Lookup
    offline = offline_lookup(full_number)
    show_data("Offline Lookup", offline)

    # Abstract API
    abstract = query_abstract(full_number)
    if "Error" not in abstract:
        show_data("Abstract API", abstract)

    # NumVerify (Fallback)
    if not abstract.get("Valid", False):
        numverify = query_numverify(full_number)
        if "Error" not in numverify:
            show_data("NumVerify API (Fallback)", numverify)

    # Truecaller Lookup
    truecaller = query_truecaller(full_number, region_code)
    if "Error" not in truecaller:
        show_data("Truecaller (Personal Use)", truecaller)

def main():
    console.print("[bold green]PHINFO - Advanced Phone Number Info Tool[/bold green]\n")

    # Prompt for API keys (if needed)
    ensure_api_keys()

    # Get user input
    region_code = console.input("[yellow]Enter country code (e.g. IN, US, GB): [/yellow]").strip().upper()
    local_number = console.input("[cyan]Enter phone number (without + or country code): [/cyan]").strip()

    # Parse number to E.164 format
    try:
        parsed = phonenumbers.parse(local_number, region_code)
        full_number = phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
    except Exception as e:
        console.print(f"[red]Invalid number or country code: {e}[/red]")
        return

    analyze_number(full_number, region_code)

if __name__ == "__main__":
    main()

