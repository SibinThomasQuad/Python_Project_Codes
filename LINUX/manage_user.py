import subprocess

class UserManagement:
    # Function to create a user
    def create_user(self, username, password):
        # Execute the command to create the user
        subprocess.run(["useradd", username])

        # Set the user's password
        subprocess.run(["echo", f"{username}:{password}", "|", "chpasswd"], shell=True)

        print(f"User {username} created with password {password}.")

    # Function to delete a user
    def delete_user(self, username):
        # Execute the command to delete the user
        subprocess.run(["userdel", "-r", username])

        print(f"User {username} deleted.")

    # Function to change a user's password
    def change_password(self, username, new_password):
        # Set the user's new password
        subprocess.run(["echo", f"{username}:{new_password}", "|", "chpasswd"], shell=True)

        print(f"Password changed for user {username}.")

    # Function to deactivate a user
    def deactivate_user(self, username):
        # Lock the user's account
        subprocess.run(["passwd", "-l", username])

        print(f"User {username} deactivated.")

    # Function to activate a user
    def activate_user(self, username):
        # Unlock the user's account
        subprocess.run(["passwd", "-u", username])

        print(f"User {username} activated.")

# Usage example:
user_management = UserManagement()

username = "exampleuser"
password = "examplepassword"

# Create a user
user_management.create_user(username, password)

# Delete a user
user_management.delete_user(username)

# Change a user's password
new_password = "newpassword"
user_management.change_password(username, new_password)

# Deactivate a user
user_management.deactivate_user(username)

# Activate a user
user_management.activate_user(username)
