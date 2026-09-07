class GitHubRepo:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

    def show_details(self):
        print(f"Repository: {self.name}")
        print(f"Owner: {self.owner}")

# Create an object
repo1 = GitHubRepo("MyPythonProject", "Sai")

# Use the object
repo1.show_details()
