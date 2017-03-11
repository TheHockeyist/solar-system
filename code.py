# WORK IN PROGRESS NOT EVERYTHING IS FUNCTIONAL YET.

import turtle

# colors of planets
# Sun: 255, 230, 200
# Mercury: 170, 170, 170
# Venus: 220, 220, 210
# Earth: 0, 50, 100
# Earth Land: 80, 120, 80
# Mars: 180, 60, 20
# Jupiter: 230, 180, 130
# Jupiter’s Spot: 230, 110, 10
# Saturn: 250, 220, 180
# Uranus: 80, 220, 230
# Neptune: 150, 210, 240

# sizes of planets
# Sun: 10
# Mercury: 2
# Venus: 3
# Earth: 3
# Mars: 2
# Jupiter: 7
# Saturn: 6
# Uranus: 5
# Neptune: 5

# distances of planets
# Mercury: 8
# Venus: 11
# Earth: 15
# Mars: 19
# Jupiter: 30
# Saturn: 40
# Uranus: 50
# Neptune: 60

my_turtle = turtle.Turtle(shape="turtle")

my_turtle.setposition(0, 0)
my_turtle.pendown()
turtle.color('#fee6c8', '#fee6c8')
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
my_turtle.penup()

my_turtle.setposition(8, 0) # Will need to change later as it is orbiting. A function of sine and cosine, perhaps?
my_turtle.pendown()
turtle.color('#aaaaaa', '#aaaaaa')
turtle.begin_fill()
turtle.circle(2)
turtle.end_fill()
my_turtle.penup()
