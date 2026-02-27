class Students:
    institute="OneTeam"

    def SetDetails(self,n):
        self.name=n

    def display(self):
        print("Hello",self.name)

std1=Students()
std2=Students()


std1.SetDetails("aswin")
std1.display()