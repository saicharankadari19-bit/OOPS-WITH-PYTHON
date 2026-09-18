class student:
    def __init__(self,Name,Roll_No,s1,s2,s3):
        self.Name=Name
        self.Roll_No=Roll_No
        self.s1=s1
        self.s2=s2
        self.s3=s3
    def Total_Marks(self):
        self.TM=self.s1+self.s2+self.s3
        print(self.TM)
    def AVERAGE(self):
        Avg=self.TM/3
        print(Avg)
    def Grade(self):
        if(self.TM>=90):
            print("A Grade")
        elif(90>self.TM>=75):
            print("B Grade")
        elif(75>self.TM>=60):
            print("C Grade")
        elif(60>self.TM>=40):
            print("D Grade")
        else:
            print("FAIL!")
S1=student("SAI",6639,30,30,30)
S1.Total_Marks()
S1.AVERAGE()
S1.Grade()

        

