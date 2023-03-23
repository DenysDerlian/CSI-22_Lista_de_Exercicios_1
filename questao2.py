import turtle


# Desenhar um polígono regular com n lados e lado de tamanho sz
def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)


# Exemplo de utilização:
tess = turtle.Turtle()

draw_poly(tess, 8, 50)
turtle.done()
