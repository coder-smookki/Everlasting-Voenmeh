# Random squares definitions

init python:
    import random

    # Function to generate random color
    def random_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Define random squares as images
image square1 = Solid(random_color(), xysize=(100, 100))
image square2 = Solid(random_color(), xysize=(150, 150))
image square3 = Solid(random_color(), xysize=(80, 80))
image square4 = Solid(random_color(), xysize=(120, 120))
image square5 = Solid(random_color(), xysize=(90, 90))
