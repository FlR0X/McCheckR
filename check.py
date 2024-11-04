import requests
import time
import os
from datetime import datetime
from colorama import init, Fore

init(autoreset=True)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_ping_response_time(url):
    start_time = time.time()
    try:
        requests.get(url, timeout=1)
        return round((time.time() - start_time) * 1000)
    except requests.RequestException:
        return None

def check_username_availability(username):
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    response = requests.get(url)
    
    if response.status_code == 204:
        return True, None
    elif response.status_code == 200:
        data = response.json()
        return False, data['id']
    elif response.status_code == 404:
        error_message = response.json().get('errorMessage', '')
        if "couldnt find any profile with name" in error_message:
            return True, None
    return None, None

def save_to_file(filename, content):
    header = "==========Minecraft Username Checker by github.com/FlR0X==========\n"
    with open(filename, 'w') as file:
        file.write(header)
        file.write(content)

def set_console_title(username, ping):
    title = f"Minecraft Username Checker by Github.com/FlR0X | Currently checking: {username} | Ping: {ping} ms"
    if os.name == 'nt':
        os.system(f'title "{title}"')
    else:
        print(f"\033]0;{title}\a", end='', flush=True)

def check_usernames(input_file):
    with open(input_file, 'r') as file:
        usernames = file.read().splitlines()
    
    unclaimed_usernames = []
    claimed_usernames = []
    unknown_usernames = []
    
    print(Fore.WHITE + r"""
___  ___     _____ _               _   ______ 
|  \/  |    /  __ \ |             | |  | ___ \
| .  . | ___| /  \/ |__   ___  ___| | _| |_/ /
| |\/| |/ __| |   | '_ \ / _ \/ __| |/ /    / 
| |  | | (__| \__/\ | | |  __/ (__|   <| |\ \ 
\_|  |_/\___|\____/_| |_|\___|\___|_|\_\_| \_|
""" + Fore.RESET)
    
    timestamp = datetime.now().strftime("%d-%m-%Y @ %H-%M")
    
    for username in usernames:
        username = username.strip()
        if username:
            ping = get_ping_response_time("https://api.mojang.com/")
            set_console_title(username, ping if ping is not None else "N/A")
            availability, uuid = check_username_availability(username)
            if availability is None:
                unknown_usernames.append(username)
            elif availability:
                print(f"{Fore.WHITE}{username} {Fore.BLUE}| {Fore.WHITE}taken: no {Fore.BLUE}| {Fore.WHITE}uuid: N/A")
                unclaimed_usernames.append(username)
            else:
                print(f"{Fore.WHITE}{username} {Fore.BLUE}| {Fore.WHITE}taken: yes {Fore.BLUE}| {Fore.WHITE}uuid: {uuid}")
                claimed_usernames.append(f"{username} [ uuid: {uuid} ]")
    
    if unclaimed_usernames:
        unclaimed_filename = f'unclaimed - [{timestamp}].txt'
        save_to_file(unclaimed_filename, '\n'.join(unclaimed_usernames))
    
    if claimed_usernames:
        claimed_filename = f'claimed - [{timestamp}].txt'
        save_to_file(claimed_filename, '\n'.join(claimed_usernames))
    
    if unknown_usernames:
        unknown_filename = f'unknown - [{timestamp}].txt'
        save_to_file(unknown_filename, '\n'.join(unknown_usernames))
    
    set_console_title("N/A", "N/A")
    
    print(f"{Fore.WHITE}done checking usernames.txt. exiting in {Fore.BLUE}10 seconds...")
    time.sleep(10)

clear_console()
input_file = 'usernames.txt'
check_usernames(input_file)
