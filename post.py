from colorama import Fore, Style, init
import time
import os
import random

init(autoreset=True)

# Logo ko colorful dikhane ke liye function
def print_colored_logo(logo):
    colors = [31, 32, 33, 34, 35, 36]
    for line in logo.split('\n'):
        color = random.choice(colors)
        print(f'\033[1;{color}m{line}\033[0m')
        time.sleep(0.1)

# Logo aur basic details display karne ka function
def display_logo():
    logo = '''
    #######  ######## ######## ##       #### ##    ## ######## 
    ##     ## ##       ##       ##        ##  ###   ## ##       
    ##     ## ##       ##       ##        ##  ####  ## ##       
    ##     ## ######   ######   ##        ##  ## ## ## ######   
    ##     ## ##       ##        ##       ##  ##  #### ##       
    ##     ## ##       ##        ##       ##  ##   ### ##       
    #######  ##       ##       ######## #### ##    ## ########                                          
    '''
    print_colored_logo(logo)
    print(f'{Fore.GREEN}< INFORMATION >----------------------------------------')
    print(f'[ DEVELOPER  ]: OWNER-RAJ THAKUR')
    print(f'[ VERSION    ]: 1.1')
    print(f'[ TOOL NAME  ]: CONVO OFFLINE')
    print(f'[ FACEBOOK   ]: https://www.facebook.com/ramesh.shewale.youtuber.9678')
    print(f'------------------------------------------------------------')

# IP information fetch karne ka function
def fetch_ip_info():
    try:
        response = requests.get('http://ip-api.com/json/')
        if response.status_code == 200:
            data = response.json()
            return {
                'ip': data.get('query', 'N/A'),
                'country': data.get('country', 'N/A'),
                'region': data.get('regionName', 'N/A'),
                'city': data.get('city', 'N/A')
            }
        print(f'{Fore.RED}Failed to fetch IP information.')
    except Exception as e:
        print(f'{Fore.RED}Error fetching IP info: {e}')

# IP aur user info display karne ka function
def display_info():
    ip_info = fetch_ip_info()
    if ip_info:
        info = f"""
{Fore.YELLOW}< YOUR INFO >-----------------------------------------
[ IP ADDRESS ]: {ip_info['ip']}
[ TIME       ]: {time.strftime('%I:%M %p')}
[ DATE       ]: {time.strftime('%d/%B/%Y')}
------------------------------------------------------------
[ COUNTRY    ]: {ip_info['country']}
[ REGION     ]: {ip_info['region']}
[ CITY       ]: {ip_info['city']}
------------------------------------------------------------
"""
        print(info)
    else:
        print(f'{Fore.RED}Could not retrieve IP and location information.')

# File se data load karne ka function
def load_from_file(file_path):
    if not os.path.exists(file_path):
        print(f'{Fore.RED}File not found: {file_path}')
        return []
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines() if line.strip()]

# Menu dikhane aur actions handle karne ka main function
def menu():
    display_logo()
    display_info()
    note = f"""
{Fore.LIGHTMAGENTA_EX}< NOTE >-------------------------------------------
              Tool Paid Monthly: ₹250
------------------------------------------------------------
"""
    print(note)
    while True:
        options = f"""
{Fore.CYAN}< MENU >-------------------------------------------
[1] Start Loader
[2] Stop Loader
[3] Show Running Loaders
[4] Exit
------------------------------------------------------------
"""
        print(options)
        choice = input(f'{Fore.CYAN}Choose an option: {Style.RESET_ALL}')
        if choice == '1':
            start_loader()
        elif choice == '2':
            stop_loader()
        elif choice == '3':
            show_running_loaders()
        elif choice == '4':
            print(f'{Fore.GREEN}Exiting... Goodbye!')
            break
        else:
            print(f'{Fore.RED}Invalid choice! Try again.')

# Loader start karne ka function
def start_loader():
    print(f'\n{Fore.YELLOW}--- Start a New Loader ---')
    convo_id = input(f'{Fore.CYAN}Enter Conversation ID: {Style.RESET_ALL}')
    hater_name = input(f'{Fore.CYAN}Enter Hater Name: {Style.RESET_ALL}')
    tokens_file = input(f'{Fore.CYAN}Enter Access Tokens File Path: {Style.RESET_ALL}')
    access_tokens = load_from_file(tokens_file)
    if not access_tokens:
        print(f'{Fore.RED}No access tokens found!')
        return
    print(f'{Fore.CYAN}1. Enter Messages Manually')
    print(f'{Fore.CYAN}2. Load Messages from File')
    message_choice = input(f'{Fore.CYAN}Choose an option: {Style.RESET_ALL}')
    if message_choice == '1':
        messages = []
        print(f'{Fore.CYAN}Enter messages one per line (type "END" to finish):{Style.RESET_ALL}')
        while True:
            message = input()
            if message.upper() == 'END':
                break
            messages.append(message.strip())
    elif message_choice == '2':
        file_path = input(f'{Fore.CYAN}Enter Message File Path: {Style.RESET_ALL}')
        messages = load_from_file(file_path)
    else:
        print(f'{Fore.RED}Invalid choice!')
        return

    if not messages:
        print(f'{Fore.RED}No messages found!')
        return
    timer = int(input(f'{Fore.CYAN}Enter Timer Interval (in seconds): {Style.RESET_ALL}'))
    print(f'{Fore.GREEN}Loader started successfully!')
    print(f'{Fore.BLUE}Details:')
    print(f'Conversation ID: {convo_id}')
    print(f'Hater Name: {hater_name}')
    print(f'Timer Interval: {timer} seconds')

# Loader stop karne ka function
def stop_loader():
    print(f'\n{Fore.YELLOW}--- Stop a Loader ---')
    task_id = input(f'{Fore.CYAN}Enter Task ID to stop: {Style.RESET_ALL}')
    print(f'{Fore.GREEN}Loader stopped successfully!')

# Running loaders ko show karne ka function
def show_running_loaders():
    print(f'\n{Fore.YELLOW}--- Show Running Loaders ---')
    print(f'{Fore.GREEN}Currently no active loaders.')

if __name__ == '__main__':
    menu()
