# Programa: Simple Pong Game
# Autor: Christian Thompson
# Fonte: freeCodeCamp.org
# Objetivo: Educacional
# Modificações: Renato Borelli

import turtle

# Configuração da Janela
wn = turtle.Screen()             
wn.title("Pong")                 
wn.bgcolor("black")              
wn.setup(width=800, height=600)  
wn.tracer(0)                  

# Pontuação inicial
score_a = 0
score_b = 0

# Barra A (Tamanho, cor, formato e posição)
paddle_a = turtle.Turtle()                         
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Barra B (Tamanho, cor, formato e posição)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Bola (velocidade, cor, formato e posição)
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

# Placar
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("courier",10, "normal"))

# Funções
# Barra a para cima
def paddle_a_up():
    y = paddle_a.ycor()         
    y += 10                      
    paddle_a.sety(y)            

# Barra a para baixo
def paddle_a_down():
    y = paddle_a.ycor()         
    y -= 10
    paddle_a.sety(y)

# Barra b para cima
def paddle_b_up():
    y = paddle_b.ycor()         
    y += 10
    paddle_b.sety(y)

# Barra b para baixo
def paddle_b_down():
    y = paddle_b.ycor()         
    y -= 10
    paddle_b.sety(y)

# Teclas para controle das barras
wn.listen()                     
wn.onkeypress(paddle_a_up, "w") 
wn.onkeypress(paddle_a_down, "s") 
wn.onkeypress(paddle_b_up, "Up") 
wn.onkeypress(paddle_b_down, "Down") 

# Main Game Loop
while True:
    #Atualiza a janela
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Limite superior
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Limite inferior
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Lateral direita e pontuação
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier",10, "normal"))
    
    # Lateral esquerda e pontuação
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier",10, "normal"))
    
    # Colisão com a barra b
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1 
    
    # Colisão com a barra a
    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1