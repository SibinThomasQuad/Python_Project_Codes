import crypt
import getpass

def authenticate_user(username, password):
    try:
        with open('/etc/shadow', 'r') as shadow_file:
            for line in shadow_file:
                fields = line.strip().split(':')
                if fields[0] == username:
                    stored_hash = fields[1]
                    salt = stored_hash[:stored_hash.rfind('$') + 1]
                    entered_hash = crypt.crypt(password, salt)
                    return stored_hash == entered_hash
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def main():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    if authenticate_user(username, password):
        print("Authentication successful!")
    else:
        print("Authentication failed.")

if __name__ == '__main__':
    main()
