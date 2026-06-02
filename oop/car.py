class Car:

            def __init__(self,model,year,color,for_sale):
                    
                    self.model = model
                    self.year = year
                    self.color = color
                    self.for_sale = for_sale
                    
            def drive(self):
                    print(f"You drive Car {self.model} {self.color} ")

            def stop(self):
                    print(f"Car Stop {self.model} {self.color} ")

            def describe(self):
                    print(f"{self.year} {self.for_sale} {self.model}")