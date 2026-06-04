# super() function in python is used to call methods or constructor  from parent class

class Shape:
        
        def __init__(self,color,is_filled):
                
                self.color = color
                self.is_filled = is_filled

        def describe(self):
         print(f" It is  {self.color}  and {'filled' if self.is_filled else 'not filled'}")



class Circle(Shape):
        
        def __init__(self,color,is_filled,radius):
                
                super().__init__(color,is_filled)
                self.radius = radius
                
        def describe(self):
               
               print(f" It is a circle with area {3.14 * self.radius * self.radius} cm") # its called overiding
               super().describe()


class Square(Shape):
        
         def __init__(self,color,width,is_filled):
                
                
                super().__init__(color,is_filled)
                self.width = width
        


class Triangle(Shape):
         
         def __init__(self,color,width,height,is_filled):
                
                
                super().__init__(color,is_filled)
                self.width =  width
                self.height = height

         def describe(self):
               
               print(f" It is a triangkle with area {3.14 * self.width * self.height /2 } cm^2") # its called overiding
               super().describe()

            

circle1 = Circle("blue",True,16)
square1 = Square("Red",15,False)
triangle = Triangle("Black",15,16,False)

print(circle1.color)
print(circle1.is_filled)
print(circle1.radius)
circle1.describe()

print(square1.color)
print(square1.is_filled)

print(triangle.is_filled)
triangle.describe()