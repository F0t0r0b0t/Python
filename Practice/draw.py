import tkinter


width = 600
height = 600
title = "F0t0r0b0t"


top = tkinter.Tk()
top.minsize(width=width + 50, height=height + 50)
if title:
    top.title(title)

canvas = tkinter.Canvas(top, width=width + 2, height=height + 2)
canvas.pack()
canvas.xview_scroll(-15, 'units')  # hack so (0, 0) works correctly
canvas.yview_scroll(-15, 'units')  # otherwise it's clipped off


# Написать свой код сюда


x = 40
y = 70
n = 150

def compare(a, b):
    if x >= y:
        print (str(x) + "is bigger")
    else:
        print (str(y) + "is bigger")

compare(x, y)

print (x)

canvas.create_rectangle(x, y, width, height)

# Рисуем красные линии
for i in range(n):
    y_add = (i / (n - 1)) * (height - 1)
    canvas.create_line(x, y, x + width - 1, y + y_add, fill='cyan')

# Рисуем зеленые линии
for i in range(n):
    y_add = (i / (n - 1)) * (height - 1)
    x_add = (i / (n - 1)) * (width - 1)
    pass
    # Зеленые линии
    canvas.create_line(x, y + y_add, x + x_add, y + height - 1, fill='yellow')


# ----------------------------------------------


if tkinter._default_root:
    tkinter._default_root.update()
    tkinter.mainloop()