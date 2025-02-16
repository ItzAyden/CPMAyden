debug_mode = False
CURRENT_VERSION = """
2.6.2
"""
CURRENT_VERSION=CURRENT_VERSION.replace('\n','')



import os,sys,random,requests



def get_latest_version_info():
    try:
        response = requests.get(VERSION_CHECK_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestError as e:
        print(f"Error checking for updates: {e}")
        return None

def download_new_version(download_url, filename):
    try:
        response = requests.get(download_url)
        response.raise_for_status()
        
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            
        with open(filename, 'wb') as file:
            file.write(response.content)
    except Exception as e:
        print(f"Error saat mengunduh: {e}")
        


try:
    from colorama import init, Fore, Back, Style
    init()
    def color(text, fore=None, back=None):
        color_map = {
            (255,0,0): Fore.RED,
            (0,255,0): Fore.GREEN, 
            (0,0,255): Fore.BLUE,
            (255,255,0): Fore.YELLOW,
            (0,255,255): Fore.CYAN,
            (255,0,255): Fore.MAGENTA
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem
    local_ip = requests.get('https://api.ipify.org').text
    response = requests.get(f"https://ipinfo.io/{local_ip}/json")
    data_jaringan = response.json()
except Exception as e:
    os.system("pip install colorama")
    os.system("pip install requests")
    os.system("pip install pystyle")
    
    from colorama import init, Fore, Back, Style
    init()
    def color(text, fore=None, back=None):
        color_map = {
            (255,0,0): Fore.RED,
            (0,255,0): Fore.GREEN, 
            (0,0,255): Fore.BLUE,
            (255,255,0): Fore.YELLOW,
            (0,255,255): Fore.CYAN,
            (255,0,255): Fore.MAGENTA
        }
        result = ""
        if fore in color_map:
            result += color_map[fore]
        result += text
        result += Style.RESET_ALL
        return result

    from pystyle import Anime as pyAnime
    from pystyle import Colors as pyColors
    from pystyle import Colorate as pyColorate
    from pystyle import Center as pyCenter
    from pystyle import System as pySystem
    


banner = r"""


 ⣀⣀⣀⣀⣠⣤⣤⣤⠶⠶⠶⢦⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣤⠤⠤⠤⢤⣤⣤⣤⣤⣄⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⣟⠛⠿⢭⣛⣉⠉⠉⠉⠉⠉⠉⠙⢿⡁⠀⠀⠉⠉⠉⠉⠛⣦⠤⠖⠒⠚⠛⠛⠛⠛⠛⢓⣶⠶⠖⠚⠉⢙⣁⣭⠭⠿⠛⠛⠛⠻⢶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⢽⣄⢀⣠⡴⠛⠉⠉⠉⠉⠻⡗⠚⢻⡇⠀⠀⠀⠀⠀⣠⡴⠋⠀⠀⠀⠀⠀⢀⣠⠴⠚⠉⠀⠤⢤⡶⠊⠉⠀⠹⡄⠀⠀⠀⠀⠀⠀⠉⠻⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠉⠉⠀⠀⠀⠀⢀⣤⣴⣾⣥⣶⡾⣷⣀⣀⣠⣴⣿⠥⠤⣄⣀⣀⣀⡤⠖⠉⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⢹⣄⣀⣀⣀⣀⣀⣀⣀⣀⣹⣿⣶⣶⣤⣤⣀⡀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⣰⠟⠻⠯⠥⣄⣄⣿⠓⠛⡛⢉⣭⣤⣤⣤⠤⠴⠚⠛⠁⠀⠀⠀⠈⠉⠉⠉⠉⠙⠛⠉⠉⠉⠉⠉⠉⣿⡁⠀⠀⠀⠀⢀⣀⣀⣀⣀⣉⣧⣀⢉⡽⠛⠛⢳⣦⡄⠀
 ⠀⠀⠀⠀⢰⡿⣄⡀⠀⠀⠀⠀⢉⣹⡿⢻⣿⠿⣿⣇⡉⣑⣦⣀⣀⣀⡤⠤⠤⣤⣤⡶⠶⠶⠶⠷⠶⢾⣉⠉⠉⠉⠙⡏⠉⠉⠉⠉⠉⠉⠁⠀⠀⠈⢹⢻⣿⠇⠀⣴⣿⣿⣿⣿
 ⠀⠀⠀⢠⡿⠀⠀⠉⠉⠙⠒⣶⡟⢉⣿⡿⠁⠀⢸⣿⠋⠉⣿⠀⠀⠀⢀⡤⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⡄⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⠀⢰⣿⣿⣿⣿⢻
 ⠀⠀⠀⢸⡷⣦⣀⡀⠀⠀⠘⢿⣧⠞⢫⣷⣄⣠⠏⣸⠀⠀⡏⠀⢀⡴⠋⠀⠀⠀⠀⠀⢀⣴⣶⣶⣶⡦⣄⡀⠀⠈⢦⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡿⠀⠀⣿⣿⣿⣾⣿⣴
 ⠀⠀⠀⢸⣷⡇⠀⠉⠑⣶⠀⠀⠀⠀⠀⠉⠉⠀⠐⡇⠀⢸⡇⣠⠟⠀⠀⠀⠀⠀⣠⣾⣿⡟⢀⣽⣧⡹⣟⣷⡀⠀⠈⣧⠸⡄⠀⠀⠀⠀⢀⣀⣠⣼⣿⠃⠀⢀⡇⠻⣿⣿⠟⠛
 ⠀⠀⠀⢸⡿⢷⣄⡀⢀⡇⠀⣀⣀⣀⣀⣀⣀⠀⢀⠇⠀⠈⢻⡟⠲⢶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⠟⢷⢸⣹⣷⠀⠀⠘⣆⣧⣠⢤⣶⣾⣿⣿⣷⣿⣿⠤⠴⠚⠉⠉⠉⠁⠀⠀
 ⠀⠀⠀⢸⣿⣦⣍⡛⠻⠃⡜⠉⠉⠀⠈⠉⢹⡆⢸⠀⠀⠀⠈⢧⡀⠀⠀⢀⡝⢉⣿⣿⣿⣿⣿⣅⡀⣸⢻⢿⣿⠀⠀⠀⢹⡿⢷⣾⡿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠻⣿⣿⢿⣿⣷⣶⣧⣄⣀⣀⠀⠀⢸⡇⢸⠀⠀⠀⠀⠀⠉⠑⠲⡞⠀⠀⣿⣿⣿⡿⠿⣿⣿⠇⣼⡾⣹⠀⠀⣀⠼⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠈⠻⢶⣭⣛⣻⣿⣷⡾⢿⣿⣿⣿⣷⣿⡦⠤⣤⣤⣀⣀⣠⣼⡇⠀⠀⠹⣿⣿⣿⠀⡨⢏⣼⣿⣧⣧⠴⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 ⠀⠀⠀⠀⠀⠀⠀⠘⠻⢯⣉⠙⣷⣼⣿⣇⣳⣿⠈⢧⠀⠸⣄⡰⠋⠀⠀⣧⣄⡀⠀⠈⠻⠽⢯⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀




              ░█████╗░██╗░░░██╗██████╗░███████╗███╗░░██╗
              ██╔══██╗╚██╗░██╔╝██╔══██╗██╔════╝████╗░██║
              ███████║░╚████╔╝░██║░░██║█████╗░░██╔██╗██║
              ██╔══██║░░╚██╔╝░░██║░░██║██╔══╝░░██║╚████║
              ██║░░██║░░░██║░░░██████╔╝███████╗██║░╚███║
              ╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░╚══════╝╚═╝░░╚══╝
                                                                       
                     𝙲𝙰𝚁 𝙿𝙰𝚁𝙺𝙸𝙽𝙶 𝙼𝚄𝙼𝚃𝙸𝙿𝙻𝙰𝚈𝙴𝚁 𝟷
                      𝙿𝚁𝙴𝚂𝚂 𝙴𝙽𝚃𝙴𝚁 𝚃𝙾 𝙲𝙾𝙽𝚃𝙸𝙽𝚄                                 
"""[1:]


pyAnime.Fade(pyCenter.Center(banner), pyColors.red_to_yellow, pyColorate.Vertical, enter=True)


pySystem.Clear()



import random
import requests
from time import sleep
import os, signal, sys
from pyfiglet import figlet_format
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate

from cpmayden  import CPMAyden

__CHANNEL_USERNAME__ = "cpmayden_channel" 
__GROUP_USERNAME__   = "cpmayden_chat"

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)  # Ensure the index is within bounds
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
    console.print(f"[bold]CPM Tools Version 2.5.8.9 || Author https://t.me/cpmayden_channel")
    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
    console.print(f"[bold]         Please Logout From CPM Before Using This Tool")
    console.print(f"[bold] ‌          Telegram : @{__CHANNEL_USERNAME__} Group @{__GROUP_USERNAME__}")
    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))

def load_player_data(cpm):
    response = cpm.get_player_data()
    if response.get('ok'):
        data = response.get('data')
        if 'floats' in data and 'localID' in data and 'money' in data and 'coin' in data:
        
            print(Colorate.Horizontal(Colors.green_to_yellow, f'======================[ Player Information ]======================'))
            
            console.print(f"[bold]>> Name   : {(data.get("Name") if "Name" in data else "UNDEFINED")}.")
                
            console.print(f"[bold]>> User ID: {data.get("localID")}.")
            
            console.print(f"[bold]>> Money  : {data.get("money")}.")
            
            console.print(f"[bold]>> Coin   : {data.get("coin")}.")
            
        else:
            console.print(f"[bold]! ERROR: new accounts most be signed-in to the game at least once !.")
            exit(1)
    else:
        console.print(f"[bold]! ERROR: seems like your login is not properly set !.")
        exit(1)


def load_key_data(cpm):

    data = cpm.get_key_data()
    
    print(Colorate.Horizontal(Colors.green_to_yellow, f'======================[ Secret Access Key ]======================='))
    
    console.print(f"[bold]>> Access Key : {data.get("access_key")}.")
    
    console.print(f"[bold]>> Telegram ID: {data.get("telegram_id")}.")
    
    console.print(f"[bold]>> Balance $  : {(data.get("coins") if not data.get("is_unlimited") else "Unlimited")}.")
        
    

def prompt_valid_value(content, tag, password=False):
    while True:
        value = Prompt.ask(content, password=password)
        if not value or value.isspace():
            console.print(f"[bold green]{tag} cannot be empty or just spaces. Please try again.")
        else:
            return value
            
def load_client_details():
    response = requests.get("http://ip-api.com/json")
    data = response.json()
    print(Colorate.Horizontal(Colors.green_to_yellow, f'===========================[ Location ]==========================='))
    console.print(f"[bold]>> Ip Address : {data.get("query")}.")
    console.print(f"[bold]>> Location   : {data.get("city")} {data.get("regionName")} {data.get("countryCode")}.")
    console.print(f"[bold]>> Country    : {data.get("country")} {data.get("zip")}.")
    print(Colorate.Horizontal(Colors.green_to_yellow, f'=============================[ MENU ]============================='))

def interpolate_color(start_color, end_color, fraction):
    start_rgb = tuple(int(start_color[i:i+2], 16) for i in (1, 3, 5))
    end_rgb = tuple(int(end_color[i:i+2], 16) for i in (1, 3, 5))
    interpolated_rgb = tuple(int(start + fraction * (end - start)) for start, end in zip(start_rgb, end_rgb))
    return "{:02x}{:02x}{:02x}".format(*interpolated_rgb)

def rainbow_gradient_string(customer_name):
    modified_string = ""
    num_chars = len(customer_name)
    start_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    end_color = "{:06x}".format(random.randint(0, 0xFFFFFF))
    for i, char in enumerate(customer_name):
        fraction = i / max(num_chars - 1, 1)
        interpolated_color = interpolate_color(start_color, end_color, fraction)
        modified_string += f'[{interpolated_color}]{char}'
    return modified_string

if __name__ == "__main__":
    console = Console()
    signal.signal(signal.SIGINT, signal_handler)
    while True:
        banner(console)
        acc_email = prompt_valid_value("[bold][?] Account Email[/bold]", "Email", password=False)
        acc_password = prompt_valid_value("[bold][?] Account Password[/bold]", "Password", password=False)
        acc_access_key = prompt_valid_value("[bold][?] Access Key[/bold]", "Access Key", password=False)
        console.print("[bold][%] Trying to Login[/bold cyan]: ", end=None)
        cpm = CPMAyden(acc_access_key)
        login_response = cpm.login(acc_email, acc_password)
        if login_response != 0:
            if login_response == 100:
                console.print(f"[bold]ACCOUNT NOT FOUND.")
                sleep(2)
                continue
            elif login_response == 101:
                console.print(f"[bold]WRONG PASSWORD.")
                sleep(2)
                continue
            elif login_response == 103:
                console.print(f"[bold]INVALID ACCESS KEY.")
                sleep(2)
                continue
            else:
                console.print(f"[bold]TRY AGAIN.")
                console.print(f"[bold]! Note: make sure you filled out the fields !.")
                sleep(2)
                continue
        else:
            console.print(f"[bold]SUCCESSFUL.")
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"]
            console.print(f"[bold][01]  Change money             1.000K")
            console.print(f"[bold][02]  Change coin              3.500K")
            console.print(f"[bold][03]  King Rank                4.000K")
            console.print(f"[bold][04]  Custom ID                3.500K")
            console.print(f"[bold][05]  Change name              1.00")
            console.print(f"[bold][06]  Change rainbow name      1.00")
            console.print(f"[bold][07]  Number Plates            2.000K")
            console.print(f"[bold][08]  Delete account           FREE")
            console.print(f"[bold][09]  Account Register         FREE")
            console.print(f"[bold][10]  Delete friends list      5.00")
            console.print(f"[bold][11]  Unlock Paid Cars         4.000K")
            console.print(f"[bold][12]  Unlock all Cars          3.000K")
            console.print(f"[bold][13]  Inject get all cars      2.000K")
            console.print(f"[bold][14]  Unlock w16 Engine        3.000K")
            console.print(f"[bold][15]  Unlock All Horns         3.000K")
            console.print(f"[bold][16]  Unlock Disable Damage    2.000K")
            console.print(f"[bold][17]  Unlock Unlimited Fuel    2.000K")
            console.print(f"[bold][18]  Unlock House 3           3.500K")
            console.print(f"[bold][19]  Unlock Smoke             2.000K")
            console.print(f"[bold][20]  Unlock Wheels            4.000K")
            console.print(f"[bold][21]  Unlock Animations        2.000K")
            console.print(f"[bold][22]  Unlock Equipaments M     3.000K")
            console.print(f"[bold][23]  Unlock Equipaments F     3.000K")
            console.print(f"[bold][24]  Change race win          1.000K")
            console.print(f"[bold][25]  Change race lose         1.000K")
            console.print(f"[bold][26]  Clone Account            5.000K")
            console.print(f"[bold][27]  Glitch car               2.500K")
            console.print(f"[bold][28]  Custom Angle             1.500K")         
            console.print(f"[bold][0]   Exit tools")
            
            print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
            
            service = IntPrompt.ask(f"[bold][?] Input number menu [white][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            
            console.print(f"[bold]==================================================================")
            
            if service == 0: # Exit
                console.print(f"[bold green]Thank You for using our tool, please join our telegram channel: @{__CHANNEL_USERNAME__}.")
            elif service == 1: # Increase Money
                console.print(f"[bold][?] Insert how much money do you want.")
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Saving your data: ", end=None)
                if amount > 0 and amount <= 500000000:
                    if cpm.set_player_money(amount):
                        console.print(f"[bold]SUCCESSFUL")
                        print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                        else: continue
                    else:
                        console.print(f"[bold]FAILED.")
                        console.print(f"[bold]Please try again.")
                        sleep(2)
                        continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please use valid values.")
                    sleep(2)
                    continue
            elif service == 2: # Increase Coins
                console.print(f"[bold][?] Insert how much coins do you want.")
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Saving your data: ", end=None)
                if amount > 0 and amount <= 500000:
                    if cpm.set_player_coins(amount):
                        console.print(f"[bold]SUCCESSFUL")
                        print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                        else: continue
                    else:
                        console.print(f"[bold]FAILED.")
                        console.print(f"[bold]Please try again.")
                        sleep(2)
                        continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please use valid values.")
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold red][!] Note:[/bold red]: if the king rank doesn't appear in game, close it and open few times.", end=None)
                console.print("[bold red][!] Note:[/bold red]: please don't do King Rank on same account twice.", end=None)
                sleep(2)
                console.print("[%] Giving you a King Rank: ", end=None)
                if cpm.set_player_rank():
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                    else: continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please try again.")
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                console.print(f"[bold][?] Enter your new ID.")
                new_id = Prompt.ask("[?] ID")
                console.print("[%] Saving your data: ", end=None)
                if len(new_id) >= 0 and len(new_id) <= 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        console.print(f"[bold]SUCCESSFUL")
                        print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                        else: continue
                    else:
                        console.print(f"[bold]FAILED.")
                        console.print(f"[bold]Please try again.")
                        sleep(2)
                        continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please use valid ID.")
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                console.print(f"[bold][?] Enter your new Name.")
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Saving your data: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        console.print(f"[bold]SUCCESSFUL")
                        print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                        else: continue
                    else:
                        console.print(f"[bold]FAILED.")
                        console.print(f"[bold]Please try again.")
                        sleep(2)
                        continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please use valid values.")
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                console.print(f"[bold][?] Enter your new Rainbow Name.")
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Saving your data: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(rainbow_gradient_string(new_name)):
                        console.print(f"[bold]SUCCESSFUL")
                        print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                        else: continue
                    else:
                        console.print(f"[bold]FAILED.")
                        console.print(f"[bold]Please try again.")
                        sleep(2)
                        continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please use valid values.")
                    sleep(2)
                    continue
            elif service == 7: # Number Plates
                console.print("[%] Giving you a Number Plates: ", end=None)
                if cpm.set_player_plates():
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                    else: continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please try again.")
                    sleep(2)
                    continue
            elif service == 8: # Account Delete
                console.print(f"[bold][!] After deleting your account there is no going back !!.")
                answ = Prompt.ask("[?] Do You want to Delete this Account ?!", choices=["y", "n"], default="n")
                if answ == "y":
                    cpm.delete()
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                else: continue
            elif service == 9: # Account Register
                console.print(f"[bold][!] Registring new Account.")
                acc2_email = prompt_valid_value("[?] Account Email", "Email", password=False)
                acc2_password = prompt_valid_value("[?] Account Password", "Password", password=False)
                console.print("[%] Creating new Account: ", end=None)
                status = cpm.register(acc2_email, acc2_password)
                if status == 0:
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    console.print(f"[bold green]INFO: In order to tweak this account with CPMElsedev.")
                    console.print(f"[bold]you most sign-in to the game using this account.")
                    sleep(2)
                    continue
                elif status == 105:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]This email is already exists !.")
                    sleep(2)
                    continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please try again.")
                    sleep(2)
                    continue
            elif service == 10: # Delete Friends
                console.print("[%] Deleting your Friends: ", end=None)
                if cpm.delete_player_friends():
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                    else: continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please try again.")
                    sleep(2)
                    continue
            elif service == 11: # Unlock All Paid Cars
                console.print("[!] Note: this function takes a while to complete, please don't cancel.", end=None)
                console.print("[%] Unlocking All Paid Cars: ", end=None)
                if cpm.unlock_paid_cars():
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                    else: continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please try again.")
                    sleep(2)
                    continue
            elif service == 12: # Unlock All Cars
                console.print("[%] Unlocking All Cars: ", end=None)
                if cpm.unlock_all_cars():
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                    else: continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please try again.")
                    sleep(2)
                    continue
            elif service == 13: # Unlock All Cars Siren
                console.print("[%] Unlocking All Cars Siren: ", end=None)
                if cpm.unlock_all_cars_siren():
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                    else: continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please try again.")
                    sleep(2)
                    continue
            elif service == 14: # Unlock w16 Engine
                console.print("[%] Unlocking w16 Engine: ", end=None)
                if cpm.unlock_w16():
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                    else: continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please try again.")
                    sleep(2)
                    continue
            elif service == 15: # Unlock All Horns
                console.print("[%] Unlocking All Horns: ", end=None)
                if cpm.unlock_horns():
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                    else: continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please try again.")
                    sleep(2)
                    continue
            elif service == 16: # Disable Engine Damage
                console.print("[%] Unlocking Disable Damage: ", end=None)
                if cpm.disable_engine_damage():
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                    else: continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please try again.")
                    sleep(2)
                    continue
            elif service == 17: # Unlimited Fuel
                console.print("[%] Unlocking Unlimited Fuel: ", end=None)
                if cpm.unlimited_fuel():
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                    else: continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please try again.")
                    sleep(2)
                    continue
            elif service == 18: # Unlock House 3
                console.print("[%] Unlocking House 3: ", end=None)
                if cpm.unlock_houses():
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                    else: continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please try again.")
                    sleep(2)
                    continue
            elif service == 19: # Unlock Smoke
                console.print("[%] Unlocking Smoke: ", end=None)
                if cpm.unlock_smoke():
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                    else: continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please try again.")
                    sleep(2)
                    continue
            elif service == 20: # Unlock Smoke
                console.print("[%] Unlocking Wheels: ", end=None)
                if cpm.unlock_wheels():
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                    else: continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please try again.")
                    sleep(2)
                    continue
            elif service == 21: # Unlock Smoke
                console.print("[%] Unlocking Animations: ", end=None)
                if cpm.unlock_animations():
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                    else: continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please try again.")
                    sleep(2)
                    continue
            elif service == 22: # Unlock Smoke
                console.print("[%] Unlocking Equipaments Male: ", end=None)
                if cpm.unlock_equipments_male():
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                    else: continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please try again.")
                    sleep(2)
                    continue
            elif service == 23: # Unlock Smoke
                console.print("[%] Unlocking Equipaments Female: ", end=None)
                if cpm.unlock_equipments_female():
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                    else: continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold]Please try again.")
                    sleep(2)
                    continue
            elif service == 24: # Change Races Wins
                console.print(f"[bold][!] Insert how much races you win.")
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Changing your data: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                    if cpm.set_player_wins(amount):
                        console.print(f"[bold]SUCCESSFUL")
                        print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                        else: continue
                    else:
                        console.print(f"[bold]FAILED.")
                        console.print(f"[bold]Please try again.")
                        sleep(2)
                        continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold][!] Please use valid values.")
                    sleep(2)
                    continue
            elif service == 25: # Change Races Loses
                console.print(f"[bold][!] Insert how much races you lose.")
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Changing your data: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999:
                    if cpm.set_player_loses(amount):
                        console.print(f"[bold]SUCCESSFUL")
                        print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                        else: continue
                    else:
                        console.print(f"[bold]FAILED.")
                        console.print(f"[bold][!] Please use valid values.")
                        sleep(2)
                        continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold][!] Please use valid values.")
                    sleep(2)
                    continue
            elif service == 26: # Clone Account
                console.print(f"[bold][!] Please Enter Account Detalis.")
                to_email = prompt_valid_value("[?] Account Email", "Email", password=False)
                to_password = prompt_valid_value("[?] Account Password", "Password", password=False)
                console.print("[%] Cloning your account: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    console.print(f"[bold]SUCCESSFUL")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                    else: continue
                        
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold][!] Please use valid values.")
                    sleep(2)
                    continue
            elif service == 27:
                console.print("[bold yellow][!] Note[/bold yellow]: original speed can not be restored!.")
                console.print("[bold cyan][!] Enter Car Details.[/bold cyan]")
                car_id = IntPrompt.ask("[bold][?] Car Id[/bold]")
                console.print("[bold cyan][%] Hacking Car Speed[/bold cyan]:",end=None)
                if cpm.hack_car_speed(car_id):
                    console.print("[bold green]SUCCESFUL (✔)[/bold green]")
                    print(Colorate.Horizontal(Colors.green_to_yellow, f'=================================================================='))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print(f"[bold green]Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.")
                    else: continue
                else:
                    console.print(f"[bold]FAILED.")
                    console.print(f"[bold][!] Please use valid values.")
                    sleep(2)
                    continue
            elif service == 28: # ANGLE
                console.print(f"[bold][!] ENTER CAR DETALIS")
                car_id = IntPrompt.ask("[red][?] CAR ID[/red]")
                console.print(f"[bold][!] ENTER STEERING ANGLE")
                custom = IntPrompt.ask("[red][?]﻿ENTER THE AMOUNT OF ANGLE YOU WANT[/red]")                
                console.print("[red][%] HACKING CAR ANGLE[/red]: ", end=None)
                if cpm.max_max1(car_id, custom):
                    console.print(f"[bold]SUCCESSFUL")
                    answ = Prompt.ask("[red][?] DO YOU WANT TO EXIT[/red] ?", choices=["y", "n"], default="n")
                    if answ == "y": console.print("THANK YOU FOR USING OUR TOOL")
                    else: continue
                else:
                    console.print(f"[bold]FAILED")
                    console.print(f"[bold]PLEASE TRY AGAIN")
                    sleep(2)
                    continue                                        
            else: continue
            break
        break
        
            
        
            
              
