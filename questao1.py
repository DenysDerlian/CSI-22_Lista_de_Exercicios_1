import turtle

denys = turtle.Turtle()

# Desenhar 5 quadrados, um dentro do outro
# Menor quadrado de lado 20
# Outros aumentam de 20 em tamanho
lado = 20
for i in range(5):
    denys.penup()
    denys.goto(-lado/2, -lado/2)
    denys.pendown()
    for j in range(4):
        denys.forward(lado)
        denys.left(90)
    lado += 20

turtle.done()
