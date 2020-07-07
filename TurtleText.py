import turtle


#-284.00
turtle.setup(600,600)                
wn = turtle.Screen()                 
wn.title("Turtle OS")     
wn.bgcolor("White")             
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.goto(-295,280)

buffer = []


def chara():
   t.write('a')
   t.forward(6)
   buffer.append('a')
   
def charb():
   t.write('b')
   t.forward(6)

def charc():
   t.write('c')
   t.forward(6)

def chard():
   t.write('d')
   t.forward(6)

def chare():
   t.write('e')
   t.forward(6)
   
def charf():
   t.write('f')
   t.forward(4)

def charg():
   t.write('g')
   t.forward(6)

def charh():
   t.write('h')
   t.forward(6)

def chari():
   t.write('i')
   t.forward(3)

def charj():
   t.write('j')
   t.forward(3)

def chark():
   t.write('k')
   t.forward(5)

def charl():
   t.write('l')
   t.forward(3)

def charm():
   t.write('m')
   t.forward(9)

def charn():
   t.write('n')
   t.forward(6)
   
def charo():
   t.write('o')
   t.forward(6)

def charp():
   t.write('p')
   t.forward(6)

def charq():
   t.write('q')
   t.forward(6)

def charr():
   t.write('r')
   t.forward(4)

def chars():
   t.write('s')
   t.forward(6)

def chart():
   t.write('t')
   t.forward(4)

def charu():
   t.write('u')
   t.forward(5)

def charv():
   t.write('v')
   t.forward(5.5)

def charw():
   t.write('w')
   t.forward(8.5)

def charx():
   t.write('x')
   t.forward(7)

def chary():
   t.write('y')
   t.forward(6)

def charz():
   t.write('z')
   t.forward(6)
   
def charA():
   t.write('A')
   t.forward(8)
   
def charB():
   t.write('B')
   t.forward(7)

def charC():
   t.write('C')
   t.forward(7)

def charD():
   t.write('D')
   t.forward(7)

def charE():
   t.write('E')
   t.forward(6)

def charF():
   t.write('F')
   t.forward(6)

def charG():
   t.write('G')
   t.forward(8)

def charH():
   t.write('H')
   t.forward(7)

def charI():
   t.write('I')
   t.forward(3)

def charJ():
   t.write('J')
   t.forward(5)

def charK():
   t.write('K')
   t.forward(7)

def charL():
   t.write('L')
   t.forward(6)

def charM():
   t.write('M')
   t.forward(8)

def charN():
   t.write('N')
   t.forward(7)

def charO():
   t.write('O')
   t.forward(8)

def charP():
   t.write('P')
   t.forward(6)

def charQ():
   t.write('Q')
   t.forward(8)

def charR():
   t.write('R')
   t.forward(7)

def charS():
   t.write('S')
   t.forward(7)

def charT():
   t.write('T')
   t.forward(6)

def charU():
   t.write('U')
   t.forward(7)

def charV():
   t.write('V')
   t.forward(9)

def charW():
   t.write('W')
   t.forward(11)

def charX():
   t.write('X')
   t.forward(8)

def charY():
   t.write('Y')
   t.forward(8)

def charZ():
   t.write('Z')
   t.forward(7)

def charSPACE():
    t.write(' ')
    t.forward(4)

def charENTER():
    Ycoordinate = t.ycor()
    t.goto(-295, Ycoordinate - 12)
    if (Ycoordinate < -280):
        t.clear()
        t.goto(-295,280)


#Continue work here
def charBACKSPACE():
  t.backward(6)
  t.pencolor("white")
  t.write('a')
  t.pencolor("black")
  
   

def getpos():
    print(t.position())
    print(buffer)

def putstring(inputstring):
   chartable = {
      'a' : chara,
      'b' : charb,
      'c' : charc,
      'd' : chard,
      'e' : chare,
      'f' : charf,
      'g' : charg,
      'h' : charh,
      'i' : chari,
      'j' : charj,
      'k' : chark,
      'l' : charl,
      'm' : charm,
      'n' : charn,
      'o' : charo,
      'p' : charp,
      'q' : charq,
      'r' : charr,
      's' : chars,
      't' : chart,
      'u' : charu,
      'v' : charv,
      'w' : charw,
      'x' : charx,
      'y' : chary,
      'z' : charz,
      'A' : charA,
      'B' : charB,
      'C' : charC,
      'D' : charD,
      'E' : charE,
      'F' : charF,
      'G' : charG,
      'H' : charH,
      'I' : charI,
      'J' : charJ,
      'K' : charK,
      'L' : charL,
      'M' : charM,
      'N' : charN,
      'O' : charO,
      'P' : charP,
      'Q' : charQ,
      'R' : charR,
      'S' : charS,
      'T' : charT,
      'U' : charU,
      'V' : charV,
      'W' : charW,
      'X' : charX,
      'Y' : charY,
      'Z' : charZ,
      ' ' : charSPACE
      }
   for letters in inputstring:
      if letters in chartable:
         chartable[letters]()
    

def putchar():
    wn.onkey(chara, "a")
    wn.onkey(charb, "b")
    wn.onkey(charc, "c")
    wn.onkey(chard, "d")
    wn.onkey(chare, "e")
    wn.onkey(charf, "f")
    wn.onkey(charg, "g")
    wn.onkey(charh, "h")
    wn.onkey(chari, "i")
    wn.onkey(charj, "j")
    wn.onkey(chark, "k")
    wn.onkey(charl, "l")
    wn.onkey(charm, "m")
    wn.onkey(charn, "n")
    wn.onkey(charo, "o")
    wn.onkey(charp, "p")
    wn.onkey(charq, "q")
    wn.onkey(charr, "r")
    wn.onkey(chars, "s")
    wn.onkey(chart, "t")
    wn.onkey(charu, "u")
    wn.onkey(charv, "v")
    wn.onkey(charw, "w")
    wn.onkey(charx, "x")
    wn.onkey(chary, "y")
    wn.onkey(charz, "z")
    wn.onkey(charA, "A")
    wn.onkey(charB, "B")
    wn.onkey(charC, "C")
    wn.onkey(charD, "D")
    wn.onkey(charE, "E")
    wn.onkey(charF, "F")
    wn.onkey(charG, "G")
    wn.onkey(charH, "H")
    wn.onkey(charI, "I")
    wn.onkey(charJ, "J")
    wn.onkey(charK, "K")
    wn.onkey(charL, "L")
    wn.onkey(charM, "M")
    wn.onkey(charN, "N")
    wn.onkey(charO, "O")
    wn.onkey(charP, "P")
    wn.onkey(charQ, "Q")
    wn.onkey(charR, "R")
    wn.onkey(charS, "S")
    wn.onkey(charT, "T")
    wn.onkey(charU, "U")
    wn.onkey(charV, "V")
    wn.onkey(charW, "W")
    wn.onkey(charX, "X")
    wn.onkey(charY, "Y")
    wn.onkey(charZ, "Z")
    wn.onkey(charSPACE, "space")
    wn.onkey(charENTER, "Return")
    wn.onkey(charBACKSPACE, "BackSpace")
    wn.onkey(getpos, ".")

putchar()
pizza = 'abcdefghijklmnopqrstuvwxyz and ABCDEFGHIJKLMNOPQRSTUVWXYZ'
putstring(pizza)

wn.listen()
turtle.mainloop()
