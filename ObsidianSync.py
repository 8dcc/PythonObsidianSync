import json, shutil, datetime, os
from colorama import Fore, Style
from mega import Mega

def data_print_green(type, text):
    print(f" {Style.BRIGHT}{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {type} {Fore.GREEN}{text}{Style.RESET_ALL}")
def data_print_empty(type, text):
    print(f"     {Style.BRIGHT}{Fore.WHITE}{type} {Fore.GREEN}{text}{Style.RESET_ALL}")
def print_warning(text):
    print(f" {Style.BRIGHT}{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] {Fore.YELLOW}{text}{Style.RESET_ALL}")
def print_mega_rem(current, total):
    print(f" {Style.BRIGHT}{Fore.WHITE}[{Fore.BLUE}i{Fore.WHITE}] You used {Fore.BLUE}{current}{Fore.WHITE} of your {Fore.BLUE}{total}{Style.RESET_ALL}")
def print_zip_file_finished(text, file):
    print(f" {Style.BRIGHT}{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.GREEN}{text}{Fore.WHITE}{file}{Style.RESET_ALL}")

def main():
    # Load the config from config.json
    with open("config.json",) as config_file:
        config = json.load(config_file)
    email = config["email"]
    password = config["password"]
    mega_path = config["mega-path"]

    m = Mega().login(email, password)
    user_details = m.get_user()

    # Print login information if the setting is enabled
    data_print_green("Logged in...", "")
    if config["displayDetails"]:
        data_print_empty("Username:", user_details['name'])
        data_print_empty("Email:", user_details['email'])
        data_print_empty("Password:", "*"*len(config["password"]))
    print()

    # Check if the "ObsidianBackups" folder exists. If not, create it.
    if not os.path.exists(os.path.abspath(os.path.dirname(__file__)).replace("\\", "/") + "/ObsidianBackups"):
        os.makedirs(os.path.abspath(os.path.dirname(__file__)).replace("\\", "/") + "/ObsidianBackups")

    # Create the zip file
    print_warning("Creating the zip file. This might take a while depending on the files.")
    now = str(datetime.datetime.today().date())
    ziparchive = f"ObsidianVault-{now}"
    shutil.make_archive(f"ObsidianBackups/{ziparchive}", 'zip', config["obsidian-path"])
    local_file_path = f"ObsidianBackups/{ziparchive}.zip"
    print_zip_file_finished("Saved zip file: ", local_file_path)

    # Upload to mega
    print_warning(f"Uploading to the folder {mega_path}. This might take a while...")
    mega_folder = m.find(mega_path)
    mega_upload = m.upload(local_file_path, mega_folder)
    mega_link = m.get_upload_link(mega_upload)
    data_print_green("File uploaded at:", f"\033[4m{mega_link}")

    if config["delete-local-file"]:
        print_warning("Deleting local backup...")
        os.remove(local_file_path)

    mega_space = m.get_storage_space(giga=True)
    print_mega_rem(f"{str(round(quota['used'], 2))}GB", f"{str(quota['total'])}GB")


main()