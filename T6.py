import math

class Sphere:
    # radius self
    def __init__(self, radius):
        self.radius = radius

    # use radius to find the sphere surface area
    def sphere_area(self):
        r = self.radius
        surface_area = 4 * math.pi * (r**2)
        sarea_twodec = round(surface_area, 2)
        print("Surface Area is", sarea_twodec)

    # use of radius to find the sphere volume
    def sphere_volume(self):
        r = self.radius
        volume = (4/3) * math.pi * (r**3)
        vol_twodec = round(volume, 2)
        print("Volume is", vol_twodec)

def main():
    # if radius is 3, and 1.5, surface area and volume is out once ran on terminal
    radius1 = Sphere(3)
    print("\nFor the spherical radius of 3: ")
    radius1.sphere_area()
    radius1.sphere_volume()
    # stars to differenciate two radius values
    print("\n***********************************")
    radius2 = Sphere(1.5)
    print("\nFor the spherical radius of 1.5: ")
    radius2.sphere_area()
    radius2.sphere_volume()

if __name__ == "__main__":
    main()