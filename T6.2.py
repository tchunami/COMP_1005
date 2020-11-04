# Math Library for pi. 
import math

class Sphere():
    # constructor
    def __init__(self, radius):
        self.radius = radius
    
    # surface area function
    def area(self):
        return round((4 * math.pi * (self.radius**2)), 2)

    # volume function
    def volume(self):
        return round(((4/3) * math.pi * (self.radius**3)), 2)

def main():
    # Asks user for the radius of the sphere to be calculated
    radius = float(input("Enter the radius of the sphere: "))
    rad1 = Sphere(radius)

    # Final print
    print(f"\nFor the radius of: {radius}. \nThe Surface Area is: {str(rad1.area())}. \nThe Volume is: {str(rad1.volume())}.")

# Calls for main()
if __name__ == "__main__":
    main()