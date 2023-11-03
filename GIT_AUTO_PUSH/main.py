import os
import time
import git

# Define the path to your cloned Git repository
repository_path = "steel-repo-cprs"

# Create a Git repository object
repo = git.Repo(repository_path)

def auto_commit_and_push():
    try:
        # Add all changes to the Git index
        repo.git.add('--all')

        # Commit with the current time and date
        commit_message = f"Automatic commit at {time.strftime('%Y-%m-%d %H:%M:%S')}"
        repo.git.commit('-m', commit_message)

        print(f"Changes committed: {commit_message}")

        # Push to the remote repository
        origin = repo.remotes.origin
        origin.push()

        print("Changes pushed to the remote repository.")
    except Exception as e:
        print(f"Error while processing changes: {str(e)}")

if __name__ == "__main__":
    while True:
        auto_commit_and_push()
        time.sleep(60)  # Adjust the interval as needed (e.g., 60 seconds)
