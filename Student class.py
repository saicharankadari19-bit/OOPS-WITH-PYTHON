class student:
    def __init__(self,Name,Roll_No,Marks):
        self.Name=Name
        self.Roll_No=Roll_No
        self.Marks=Marks
    def display(self):
        print(self.Name)
        print(self.Roll_No)
        print(self.Marks)
s1=student("Ravi",101,85)
s1.display()
