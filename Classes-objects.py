# Classes and Objects


# Class
class Membersinfo:

    def __init__(self, name, address, age, post):
        self.name = name  #Object
        self.address = address  #Object
        self.age = age  #Object
        self.post = post    #Object

    def display(self):
        # f Statement
        Member = f"{self.name} is the name.\n {self.address} is address \n {self.age} is age \n {self.post} is his post \n"
        return Member


#Instances
Member1 = Membersinfo("Yash", "Dhangar Ali", 21, "Treasurer")
Member2 = Membersinfo("Akash", "Trimurti Nagar", 27, "President")
Member3 = Membersinfo("Satyen", "Sudarshan Nagar", 21, "Secretary")
Member4 = Membersinfo("Bhavesh", "Dhangar Ali", 21, "Finance Director")
Member5 = Membersinfo("Sarthak", "Mehendale High School", 21, "Edito")

print(Membersinfo.display(Member1))
print(Membersinfo.display(Member2))
print(Membersinfo.display(Member3))
print(Membersinfo.display(Member4))
print(Membersinfo.display(Member5))


