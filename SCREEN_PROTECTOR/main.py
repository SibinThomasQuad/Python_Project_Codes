import os
import hashlib
import pyautogui
import time
import threading
import sys
HASH_FILE = "pswd.data"


class Security:
    def prompt_password(self):
        auth_obj = Authenticate()
        password = input("password > ")
        auth_obj.login(password)
    
    def file_exists(self,file_path):
        return os.path.isfile(file_path)
    
    def read_file(self,file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
            return None
    
    def convert_to_md5(self,string):
        md5_hash = hashlib.md5(string.encode()).hexdigest()
        return md5_hash

    def create_file(self,file_path, content):
        try:
            with open(file_path, 'w') as file:
                file.write(content)
            print(f"File '{file_path}' Registered")
        except Exception as e:
            print(f"Error creating file: {str(e)}")

class Authenticate:
    
    def login(self,password):
        security_obj = Security()
        if(security_obj.file_exists(HASH_FILE)):
             input_hash = security_obj.convert_to_md5(password)
             password_hash = security_obj.read_file(HASH_FILE)
             if(input_hash == password_hash):
                 print("Auth Success")
                 print("Screen Unlocking...")
                 pyautogui.hotkey('alt', 'f4')
             else:
                 print("Auth failed")
        else:
            self.register()
    
    def register(self):
        security_obj = Security()
        print("Please add the password and note it")
        password = input("password > ")
        input_hash = security_obj.convert_to_md5(password)
        security_obj.create_file(HASH_FILE,input_hash)

class Screen:
    
    def prevent_window_escape(self):
        original_position = pyautogui.position()
        original_size = pyautogui.size()

        while True:
            current_position = pyautogui.position()
            current_size = pyautogui.size()

            # Check if the window has moved
            if current_position != original_position:
                pyautogui.moveTo(*original_position)

            # Check if the window has been resized
            if current_size != original_size:
                pyautogui.size(*original_size)

            time.sleep(0.1)
    
    def make_window_fullscreen(self):
        pyautogui.keyDown('alt')
        pyautogui.keyDown('space')
        pyautogui.press('x')
        pyautogui.keyUp('alt')
        pyautogui.keyUp('space')

class Main:
    
    def start():
        screen_obj = Screen()
        screen_obj.make_window_fullscreen()
        thread = threading.Thread(target=screen_obj.prevent_window_escape)
        thread.start()
        Security_obj = Security()
        Security_obj.prompt_password()

Main.start()
