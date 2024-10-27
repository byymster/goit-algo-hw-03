import turtle
import time


def draw_disk(x, y, width, color):
    turtle.penup()
    turtle.goto(x - width / 2, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
    turtle.end_fill()


def move_disk(from_pole, to_pole):
    disk = state[from_pole].pop()
    state[to_pole].append(disk)
    print(f"Перемістити диск з {from_pole} на {to_pole}: {disk}")
    print(f"Проміжний стан: {state}")
    draw_state()
    time.sleep(0.3)  # Затримка для візуалізації


def draw_state():
    turtle.clear()
    pole_positions = {'A': -200, 'B': 0, 'C': 200}
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'pink', 'cyan', 'magenta', 'lime', 'indigo', 'violet', 'gold', 'silver']
    for pole, disks in state.items():
        x = pole_positions[pole]
        y = -150  # Стартова координата знизу
        for i, disk in enumerate(disks):
            draw_disk(x, y + i * 25, disk * 20, colors[disk % len(colors)])
    turtle.update()


def hanoi(n, source, target, auxiliary):
    if n > 0:
        hanoi(n - 1, source, auxiliary, target)
        move_disk(source, target)
        hanoi(n - 1, auxiliary, target, source)


if __name__ == "__main__":
    try:
        n = int(input("Введіть кількість дисків: "))
        state = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}

        print(f"Початковий стан: {state}")

        turtle.speed(0)
        turtle.hideturtle()
        turtle.tracer(0, 0)
        turtle.setup(width=800, height=600)
        draw_state()

        hanoi(n, 'A', 'C', 'B')

        print(f"Кінцевий стан: {state}")
        # turtle.done()
        time.sleep(5)
        turtle.bye()
    except turtle.Terminator:
        print("Вікно графіки Turtle закрито.")
    except KeyboardInterrupt:
        print("Програму перервано користувачем.")
        turtle.bye()