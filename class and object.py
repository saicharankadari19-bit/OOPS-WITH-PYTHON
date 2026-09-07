class student:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def show_details(self):
        print(f"Repository: {self.name}")
        print(f"department: {self.department}")

# Create an object
repo1 = student("Sai", "AIML")

# Use the object
repo1.show_details()
