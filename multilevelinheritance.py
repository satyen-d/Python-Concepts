class RaCRohaCentral:
    president = "Rtr. Akash Rumade"
    secretary = "Rtr. Satyen Deshpande"
    treasurer = "Rtr. Yash Shinde"

class Avenue(RaCRohaCentral):
    CSD = "Rtr. Rohit"
    PDD = "Rtr. Srushti"
    CMD = "Rtr. Sanket"
    ISD = "Rtr. Mitesh"

class display(Avenue):
    def displayy(self):
        print(f"CSD is {self.CSD}, Treasurer is {self.treasurer}")
    


a = display()
a.displayy()
