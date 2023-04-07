from canvas import Canvas, save_canvas
from shapes import Square, Rectangle, draw_random_shapes

canvas_height = int(input("Enter canvas height: "))
canvas_width = int(input("Enter canvas width: "))
background_color = input("Choose between black or white: ")

user_canvas = Canvas(h=canvas_height, w=canvas_width)
user_canvas.background(background_color)

q0 = input("Would you like to draw an object on this canvas? (y/n): ")

if q0 == 'y':
    while True:
        # Input color
        green = int(input("Enter green intensity (0-250): "))
        blue = int(input("Enter blue intensity (0-250): "))
        red = int(input("Enter red intensity (0-250): "))
        # Input upper left corner
        x = int(input("Enter x for upper left corner: "))
        y = int(input("Enter y for upper left corner: "))

        q1 = input("Enter square(s), rectangle(r), or quit(q) to exit: ")

        if q1 == "s":
            # Input size:
            side = int(input("Enter side\'s length: "))

            Square(x=x, y=y, side=side, color=[red, blue, green]).draw(user_canvas)
        elif q1 == "r":
            # Input size:
            h = int(input("Enter height: "))
            w = int(input("Enter width: "))

            Rectangle(x=x, y=y, h=h, w=w, color=[red, blue, green]).draw(user_canvas)
        else:
            pass

        q2 = input("Would you like to draw another object? (y/n): ")

        if q2 == 'y':
            continue
        else:
            break
else:
    q3 = input("Should I create a random canvas for you? (y/n): ")

    if q3 == 'y':
        draw_random_shapes(canvas=user_canvas, canvas_x=user_canvas.h, canvas_y=user_canvas.w, n_objects=100)
    else:
        pass

save_canvas(user_canvas.data, 'user_canvas.png')
