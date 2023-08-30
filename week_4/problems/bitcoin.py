import requests
from sys import exit,argv
import json

try:
    number=float(argv[1])
    bc=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
    bc_float=float(bc["bpi"]["USD"]["rate_float"])
    print(f"${number*bc_float:,.4f}")

except IndexError:
    print("Missing command-line argument")
    exit(1)
except ValueError:
    print("Command-line argument is not a number")
    exit(1)
except requests.RequestException:  
    exit(1)

