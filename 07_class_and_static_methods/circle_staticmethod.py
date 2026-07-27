# Circle Class using @staticmethod

class Circle:

    # Static method to calculate the area of a circle
    @staticmethod
    def area(radius):
        return 3.14 * radius * radius

    # Static method to calculate the circumference of a circle
    @staticmethod
    def circumference(radius):
        return 2 * 3.14 * radius


# Radius of the circle
radius = 7

print(f"Radius : {radius}")
print(f"Area : {Circle.area(radius):.2f}")
print(f"Circumference : {Circle.circumference(radius):.2f}")
