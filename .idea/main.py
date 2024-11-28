import colorgram
import turtle as t
import random

t.colormode(255)
# extracted_colors = colorgram.extract('image.jpeg',30)
# colors = []
#
# for i in range(30):
#     color = extracted_colors[i]
#     rgb = tuple(color.rgb)
#     colors.append(rgb)

color_list = [ (208, 158, 96), (234, 213, 101), (41, 104, 144), (149, 78, 57), (130, 168, 194),
               (202, 137, 162), (148, 65, 83), (24, 40, 55), (204, 90, 68), (169, 159, 55), (139, 180, 152),
               (193, 89, 121), (59, 117, 93), (26, 44, 36), (223, 171, 187), (63, 46, 34), (91, 154, 104),
               (44, 161, 182), (237, 212, 7), (226, 175, 167), (13, 96, 75), (41, 59, 99), (179, 189, 213),
               (99, 125, 168), (65, 33, 43), (104, 43, 59)]

tim = t.Turtle()

def call_tim_back(y_axis):
    tim.left(90)
    tim.teleport(y = y_axis)
    tim.left(90)
    tim.teleport(x=0)
    tim.right(180)

def draw_hirst_painting(x_points, y_points):
    for y in range(1,y_points+1):
        for x in range(1,x_points+1):
            tim.dot(20, random.choice(color_list))
            tim.teleport(x * 50)
        y_axis = y*50
        call_tim_back(y_axis)

draw_hirst_painting(7,5)


screen = t.Screen()
screen.exitonclick()