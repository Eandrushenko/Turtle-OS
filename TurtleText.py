import turtle


#-284.00
textcolor = "White"
bgcolor = "Black"

turtle.setup(600,600)                
wn = turtle.Screen()                 
wn.title("Turtle OS")

wn.bgcolor(bgcolor)             
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()
t.goto(-295,280)
t.pencolor(textcolor)

buffer = []


def chara():
   t.write('a')
   t.forward(6)
   buffer.append('a')
   
def charb():
   t.write('b')
   t.forward(6)
   buffer.append('b')

def charc():
   t.write('c')
   t.forward(6)
   buffer.append('c')

def chard():
   t.write('d')
   t.forward(6)
   buffer.append('d')

def chare():
   t.write('e')
   t.forward(6)
   buffer.append('e')
   
def charf():
   t.write('f')
   t.forward(4)
   buffer.append('f')

def charg():
   t.write('g')
   t.forward(6)
   buffer.append('g')

def charh():
   t.write('h')
   t.forward(6)
   buffer.append('h')

def chari():
   t.write('i')
   t.forward(3)
   buffer.append('i')

def charj():
   t.write('j')
   t.forward(3)
   buffer.append('j')

def chark():
   t.write('k')
   t.forward(5)
   buffer.append('k')

def charl():
   t.write('l')
   t.forward(3)
   buffer.append('l')

def charm():
   t.write('m')
   t.forward(9)
   buffer.append('m')

def charn():
   t.write('n')
   t.forward(6)
   buffer.append('n')
   
def charo():
   t.write('o')
   t.forward(6)
   buffer.append('o')

def charp():
   t.write('p')
   t.forward(6)
   buffer.append('p')

def charq():
   t.write('q')
   t.forward(6)
   buffer.append('q')

def charr():
   t.write('r')
   t.forward(4)
   buffer.append('r')

def chars():
   t.write('s')
   t.forward(6)
   buffer.append('s')

def chart():
   t.write('t')
   t.forward(4)
   buffer.append('t')

def charu():
   t.write('u')
   t.forward(5.5)
   buffer.append('u')

def charv():
   t.write('v')
   t.forward(5.5)
   buffer.append('v')

def charw():
   t.write('w')
   t.forward(8.5)
   buffer.append('w')

def charx():
   t.write('x')
   t.forward(7)
   buffer.append('x')

def chary():
   t.write('y')
   t.forward(6)
   buffer.append('y')

def charz():
   t.write('z')
   t.forward(6)
   buffer.append('z')
   
def charA():
   t.write('A')
   t.forward(8)
   buffer.append('A')
   
def charB():
   t.write('B')
   t.forward(7)
   buffer.append('B')

def charC():
   t.write('C')
   t.forward(7)
   buffer.append('C')

def charD():
   t.write('D')
   t.forward(7)
   buffer.append('D')

def charE():
   t.write('E')
   t.forward(6)
   buffer.append('E')

def charF():
   t.write('F')
   t.forward(6)
   buffer.append('F')
   
def charG():
   t.write('G')
   t.forward(8)
   buffer.append('G')

def charH():
   t.write('H')
   t.forward(7)
   buffer.append('H')
   
def charI():
   t.write('I')
   t.forward(3)
   buffer.append('I')

def charJ():
   t.write('J')
   t.forward(5)
   buffer.append('J')

def charK():
   t.write('K')
   t.forward(7)
   buffer.append('K')

def charL():
   t.write('L')
   t.forward(6)
   buffer.append('L')

def charM():
   t.write('M')
   t.forward(8)
   buffer.append('M')

def charN():
   t.write('N')
   t.forward(7)
   buffer.append('N')

def charO():
   t.write('O')
   t.forward(8)
   buffer.append('O')

def charP():
   t.write('P')
   t.forward(6)
   buffer.append('P')

def charQ():
   t.write('Q')
   t.forward(8)
   buffer.append('Q')

def charR():
   t.write('R')
   t.forward(7)
   buffer.append('R')

def charS():
   t.write('S')
   t.forward(7)
   buffer.append('S')

def charT():
   t.write('T')
   t.forward(6)
   buffer.append('T')
   
def charU():
   t.write('U')
   t.forward(7)
   buffer.append('U')

def charV():
   t.write('V')
   t.forward(9)
   buffer.append('V')

def charW():
   t.write('W')
   t.forward(11)
   buffer.append('W')

def charX():
   t.write('X')
   t.forward(8)
   buffer.append('X')

def charY():
   t.write('Y')
   t.forward(8)
   buffer.append('Y')

def charZ():
   t.write('Z')
   t.forward(7)
   buffer.append('Z')

def charSPACE():
    t.write(' ')
    t.forward(4)
    buffer.append(' ')

def charPERIOD():
    t.write('.')
    t.forward(2)
    buffer.append('.')
    
def char1():
    t.write('1')
    t.forward(5)
    buffer.append('1')

def char2():
    t.write('2')
    t.forward(6)
    buffer.append('2')

def char3():
    t.write('3')
    t.forward(6)
    buffer.append('3')

def char4():
    t.write('4')
    t.forward(6)
    buffer.append('4')

def char5():
    t.write('5')
    t.forward(6)
    buffer.append('5')

def char6():
    t.write('6')
    t.forward(6)
    buffer.append('6')

def char7():
    t.write('7')
    t.forward(6)
    buffer.append('7')

def char8():
    t.write('8')
    t.forward(6)
    buffer.append('8')

def char9():
    t.write('9')
    t.forward(6)
    buffer.append('9')

def char0():
    t.write('0')
    t.forward(6)
    buffer.append('0')

def charCOMMA():
    t.write(',')
    t.forward(2)
    buffer.append(',')

def charQUESTION():
    t.write('?')
    t.forward(7)
    buffer.append('?')

def charEXCLAMATION():
    t.write('!')
    t.forward(4)
    buffer.append('!')

def charQUOTATION():
    t.write('"')
    t.forward(5)
    buffer.append('"')

def charLTS():
    t.write('<')
    t.forward(6)
    buffer.append('<')

def charGTS():
    t.write('>')
    t.forward(6)
    buffer.append('>')

def charENTER():
    Ycoordinate = t.ycor()
    t.goto(-295, Ycoordinate - 12)
    if (Ycoordinate < -280):
        t.clear()
        t.goto(-295,280)


#Continue work here
def charBACKSPACE():
   if buffer:
      twos = ['.', ',']
      threes = ['i', 'j', 'l', 'I']
      fours = ['f', 'r', 't', ' ', '!']
      fives = ['k', 'J', '1', '\"']
      sixes = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'n', 'o', 'p', 'q', 's', 'y', 'z', 'E', 'F', 'L', 'P', 'T', '2', '3', '4', '5', '6', '7', '8', '9', '0', '<', '>']
      sevens = ['x', 'B', 'C', 'D', 'H', 'K', 'N', 'R', 'S', 'U', 'Z', '?']
      eights = ['A', 'G', 'M', 'O', 'Q', 'X', 'Y']
      nines = ['m', 'V']
      fivehalves = ['v', 'u']
      eighthalf = 'w'
      eleven = 'W'
      
      delchar = buffer.pop()
      backvalue = 0
      if delchar in twos:
         backvalue = 2
      elif delchar in threes:
         backvalue = 3
      elif delchar in fours:
         backvalue = 4
      elif delchar in fives:
         backvalue = 5
      elif delchar in sixes:
         backvalue = 6
      elif delchar in sevens:
         backvalue = 7
      elif delchar in eights:
         backvalue = 8
      elif delchar in nines:
         backvalue = 9
      elif delchar in fivehalves:
         backvalue = 5.5
      elif delchar == eighthalf:
         backvalue = 8.5
      elif delchar == eleven:
         backvalue = 11
      
      t.backward(backvalue)
      t.pencolor(bgcolor)
      t.write(delchar)
      t.pencolor(textcolor)
  
   

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
      ' ' : charSPACE,
      '.' : charPERIOD,
      '1' : char1,
      '2' : char2,
      '3' : char3,
      '4' : char4,
      '5' : char5,
      '6' : char6,
      '7' : char7,
      '8' : char8,
      '9' : char9,
      '0' : char0,
      ',' : charCOMMA,
      '?' : charQUESTION,
      '!' : charEXCLAMATION,
      '/"' : charQUOTATION,
      '<' : charLTS,
      '>' : charGTS,
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
    wn.onkey(charPERIOD, ".")
    wn.onkey(char1, "1")
    wn.onkey(char2, "2")
    wn.onkey(char3, "3")
    wn.onkey(char4, "4")
    wn.onkey(char5, "5")
    wn.onkey(char6, "6")
    wn.onkey(char7, "7")
    wn.onkey(char8, "8")
    wn.onkey(char9, "9")
    wn.onkey(char0, "0")
    wn.onkey(charCOMMA, ",")
    wn.onkey(charQUESTION, "?")
    wn.onkey(charEXCLAMATION, "!")
    wn.onkey(charQUOTATION, "\"")
    wn.onkey(charLTS, "<")
    wn.onkey(charGTS, ">")
    

putchar()
pizza = ''
putstring(pizza)

wn.listen()
turtle.mainloop()
