import math
print("==================")
print("Area Calculator 📐")
print("==================")
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")
choice=int(input("Which shape: "))
if choice==1:
    base=float(input("Base: "))
    height=float(input("Height: "))
    area=0.5*base*height
    print("Area of Triangle:", area)
elif choice==2:
    length=float(input("Length: "))
    width=float(input("Width: "))
    area=length*width
    print("Area of Rectangle:", area)
elif choice==3:
    side=float(input("Side: "))
    area=side*side
    print("Area of Square:", area)
elif choice==4:
    radius=float(input("Radius: "))
    area=math.pi*radius*radius
    print("Area of Circle:", area)
elif choice==5:
    print("Quit")
else:
    print("Invalid choice")