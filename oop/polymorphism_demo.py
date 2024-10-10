import math

# Base class Shape
class Shape:
    """A base class representing a generic shape."""

    def area(self):
        """Method to calculate area, must be overridden in derived classes."""
        raise NotImplementedError("Subclasses must override the area method.")


# Derived class Rectangle
class Rectangle(Shape):
    """A class to represent a rectangle, inherits from Shape."""

    def __init__(self, length, width):
        """Initialize a Rectangle instance with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate the rectangle's area."""
        return self.length * self.width


# Derived class Circle
class Circle(Shape):
    """A class to represent a circle, inherits from Shape."""

    def __init__(self, radius):
        """Initialize a Circle instance with a radius."""
        self.radius = radius

    def area(self):
        """Override the area method to calculate the circle's area."""
        return math.pi * self.radius ** 2

from polymorphism_demo import Shape, Rectangle, Circle
import math

def main():
    # Create instances of Rectangle and Circle
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    # Demonstrate polymorphism
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()
