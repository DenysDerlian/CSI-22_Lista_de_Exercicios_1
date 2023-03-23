import turtle

reto = turtle.Turtle()
inclinado = turtle.Turtle()

reto.speed(0)
inclinado.speed(0)

reto.penup()
reto.goto(-200, 0)
reto.pendown()

inclinado.penup()
inclinado.goto(200, 0)
inclinado.pendown()

# Desenhando a espiral reta
for i in range(96):
    reto.forward(i*3)
    reto.right(90)

# Ajuste de ângulo da segunda espiral
angulo = -1

# Desenhando a espiral inclinada
for i in range(96):
    inclinado.forward(i*3)
    inclinado.right(90+angulo)

turtle.done()
