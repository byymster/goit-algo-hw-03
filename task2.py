import turtle


def draw_koch_segment(length, level):
    if level == 0:
        turtle.forward(length)
    else:
        length /= 3
        draw_koch_segment(length, level - 1)
        turtle.left(60)
        draw_koch_segment(length, level - 1)
        turtle.right(120)
        draw_koch_segment(length, level - 1)
        turtle.left(60)
        draw_koch_segment(length, level - 1)


def draw_koch_snowflake(length, level):
    for _ in range(3):
        draw_koch_segment(length, level)
        turtle.right(120)


if __name__ == "__main__":
    # Вказати рівень рекурсії
    recursion_level = int(input("Введіть рівень рекурсії: "))

    # Налаштування Turtle
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-150, 100)
    turtle.pendown()

    # Малювання сніжинки Коха
    draw_koch_snowflake(300, recursion_level)

    # Завершення роботи Turtle
    turtle.hideturtle()
    turtle.done()
