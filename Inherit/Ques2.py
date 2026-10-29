class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print("Brand:",self.brand,"Model:",self.model)
class Car(Vehicle):
    def __init__(self,brand,model,fuel_type,price) :
        super().__init__(brand,model)
        self.fuel_type=fuel_type
        self.price=price
    def display(self):
        super().display()
        print("Fuel Type:",self.fuel_type)
        print("Price:",self.price)    
    def DiscountPrice(self):
        return (self.price-(self.price*(20/100)) )  
Kar=Car("Nexon",2013,"Petrol",500000)
Kar.display()     
print("Discounted Price:",Kar.DiscountPrice())