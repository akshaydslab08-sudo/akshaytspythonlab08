from Graphics.rectFunction import*
from Graphics.cirFunction import*
from Graphics.DGraphics.cubFunction import*
from Graphics.DGraphics.sphFunction import*

l=int(input("enter length:"))
b=int(input("enter breadth:"))
print("Area of rectangle:",rectArea(l,b))
print("Perimeter of rectangle:",rectPerimeter(l,b))

r=int(input("enter the radius of circle:"))
print("Area of circle:",circleArea(r))
print("Perimeter of circle:",circlePerimeter(r))

r=int(input("enter the radius of sphere:"))
print("Area of sphere:",sphArea(r))
print("Perimeter of sphere:",sphPerimeter(r))

l=int(input("enter length:"))
b=int(input("enter breadth:"))
h=int(input("enter height:"))
print("Area of cuboid: ",cubArea(l,b,h))
print("perimeter of cuboid: ",cubPerimeter(l,b,h))

