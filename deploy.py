import subprocess

def main():
    try:
        subprocess.run(["git", "add", "."], check=True)
        commit_message = input("Enter commit message: ")
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Changes have been added, committed, and pushed successfully.")
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
