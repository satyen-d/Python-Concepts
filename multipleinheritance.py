class RaCRohaCentral:
    president = "Rtr. Akash Rumade"
    secretary = "Rtr. Satyen Deshpande"
    treasurer = "Rtr. Yash Shinde"

class Avenue:
    CSD = "Rtr. Rohit"
    PDD = "Rtr. Srushti"
    CMD = "Rtr. Sanket"
    ISD = "Rtr. Mitesh"

class display(RaCRohaCentral, Avenue):
    def displayy(self):
        print(f"CSD is {self.CSD}, Treasurer is {self.treasurer}")
    


a = display()
a.displayy()

