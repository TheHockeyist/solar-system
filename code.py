# WORK IN PROGRESS NOT EVERYTHING IS FUNCTIONAL YET.

import turtle

# colors of planets
# Sun: 255, 230, 200
# Mercury: 170, 170, 170
# Venus: 230, 210, 180
# Earth: 0, 50, 100
# Earth Land: 80, 120, 80
# Mars: 200, 100, 80
# Jupiter: 230, 200, 160
# Jupiter’s Spot: 230, 170, 140
# Saturn: 240, 220, 170
# Uranus: 80, 220, 240
# Neptune: 140, 210, 240

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
