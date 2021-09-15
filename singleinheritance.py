class RaCRohaCentral:
    president = "Rtr. Akash Rumade"
    secretary = "Rtr. Satyen Deshpande"
    treasurer = "Rtr. Yash Shinde"



class Avenue(RaCRohaCentral):
    def display(self):
        print(f"Roha Central has 4 avenue - PDD, CSD, CMD, ISD, president is {self.president}")
    
    president = "Rtr. Yash Shinde"



a = Avenue()
a.display()

print(a.president)