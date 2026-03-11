# OOPS in python

class Books:
    def __init__(self, name, publisher, price):
        self.name= name
        self.publisher= publisher
        self.price= price



book1= Books("English W/B-1", "Emaan Printers", 1040)
book2= Books("English W/B-2", "Emaan Printers", 2000)
book3= Books("English W/B-3", "Emaan Printers", 1440)
book4=Books("English W/B-4", "Emaan Printers", 1640)
book5=Books("English W/B-5", "Emaan Printers", 1350)


print(f"{book1.name} : {book1.price}")
print(f"{book2.name} : {book2.price}")
print(f"{book3.name} : {book3.price}")
print(f"{book4.name} : {book4.price}")
        