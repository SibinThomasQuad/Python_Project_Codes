import os
import requests
import hashlib
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import subprocess

# Load environment variables from .env file
load_dotenv()
def label():
    label_text = '''

░██╗░░░░░░░██╗██╗███╗░░██╗░░░░░░██╗███╗░░██╗░██████╗████████╗░█████╗░██╗░░░░░██╗░░░░░███████╗██████╗░
░██║░░██╗░░██║██║████╗░██║░░░░░░██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░░░██║░░░░░██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║██╔██╗██║█████╗██║██╔██╗██║╚█████╗░░░░██║░░░███████║██║░░░░░██║░░░░░█████╗░░██████╔╝
░░████╔═████║░██║██║╚████║╚════╝██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░██║██║░╚███║░░░░░░██║██║░╚███║██████╔╝░░░██║░░░██║░░██║███████╗███████╗███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝░░░░░░╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝
'''
    print(label_text)
    print("\n")
    
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def fetch_files_from_url(url, extensions):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        file_info = []
        for index, link in enumerate(soup.find_all("a"), start=1):
            href = link.get("href")
            if href and not href.startswith("../"):
                for ext in extensions:
                    if href.endswith(ext):
                        file_url = url + href
                        head_response = requests.head(file_url)
                        last_modified = head_response.headers.get("Last-Modified", "")
                        md5_hash = hashlib.md5(link.text.encode()).hexdigest()
                        file_info.append((index, link.text, ext, last_modified, md5_hash, file_url))
                        break

        return file_info

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

if __name__ == "__main__":
    try:
        # Read URL and extensions from .env file
        url = os.getenv("URL")
        extensions = os.getenv("EXTENSIONS").split(",")

        while True:
            clear_screen()  # Clear the screen before displaying fetched files
            label()
            if url and extensions:
                files = fetch_files_from_url(url, extensions)
                if files:
                    print("Fetched files:")
                    print("{:<6} {:<20} {:<10} {:<20} {:<32}".format("ID", "File Name", "Extension", "Last Modified", "MD5 Sum"))
                    print("="*94)
                    for file in files:
                        index, file_name, ext, last_modified, md5_hash, _ = file
                        print("{:<6} {:<20} {:<10} {:<20} {:<32}".format(index, file_name, ext, last_modified, md5_hash))

                    selected_ids = input("\nEnter the IDs of the files you want to download and install (comma-separated), or type 'exit' to quit: ")
                    
                    if selected_ids.lower() == 'exit':
                        break
                    
                    selected_ids = [int(id.strip()) for id in selected_ids.split(",")]

                    for selected_id in selected_ids:
                        selected_file = None
                        for file in files:
                            index, file_name, ext, _, _, file_url = file
                            if index == selected_id:
                                selected_file = file
                                break

                        if selected_file:
                            _, file_name, ext, _, _, file_url = selected_file
                            print(f"Selected file: ID {selected_id}, File Name: {file_name}, Extension: {ext}")
                            response = requests.get(file_url)
                            with open(file_name, "wb") as file:
                                file.write(response.content)
                            try:
                                subprocess.run(file_name, shell=True)
                            except Exception as e:
                                print(f"Error running {file_name}: {e}")
                            os.remove(file_name)
                        else:
                            print(f"File with ID {selected_id} not found.")
                else:
                    print("No files fetched.")
            else:
                print("URL or extensions not found in .env file.")
    except:
        print("[@@] ERROR OCCURED EXITING...")
