import turtle
import os
import shutil

#-284.00

#INITIALIZE
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

#TURTLE TEXT FUNCTIONS
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
   t.forward(9)
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

def charFORWARDSLASH():
    t.write('/')
    t.forward(4)
    buffer.append('/')

def charBACKSLASH():
    t.write('\\')
    t.forward(4)
    buffer.append('\\')

def charBRACKET1():
    t.write('[')
    t.forward(4)
    buffer.append('[')

def charBRACKET2():
    t.write(']')
    t.forward(4)
    buffer.append(']')

def charCURLY1():
    t.write('{')
    t.forward(4)
    buffer.append('{')

def charCURLY2():
    t.write('}')
    t.forward(4)
    buffer.append('}')

def charPARA1():
    t.write('(')
    t.forward(4)
    buffer.append('(')

def charPARA2():
    t.write(')')
    t.forward(4)
    buffer.append(')')

def charAT():
    t.write('@')
    t.forward(11)
    buffer.append('@')

def charPOUND():
    t.write('#')
    t.forward(6)
    buffer.append('#')

def charDS():
    t.write('$')
    t.forward(5.5)
    buffer.append('$')

def charPERCENT():
    t.write('%')
    t.forward(10)
    buffer.append('%')

def charCARET():
    t.write('^')
    t.forward(5)
    buffer.append('^')

def charAMPERSAND():
    t.write('&')
    t.forward(7)
    buffer.append('&')

def charASTERISK():
    t.write('*')
    t.forward(5)
    buffer.append('*')

def charAPOSTROPHE():
    t.write('\'')
    t.forward(3)
    buffer.append('\'')

def charGRAVE():
    t.write('`')
    t.forward(3)
    buffer.append('`')

def charTILDE():
    t.write('~')
    t.forward(5.5)
    buffer.append('~')

def charPIPE():
    t.write('|')
    t.forward(3)
    buffer.append('|')

def charCOLON():
    t.write(':')
    t.forward(3)
    buffer.append(':')

def charSEMICOLON():
    t.write(';')
    t.forward(3)
    buffer.append(';')

def charUNDERSCORE():
    t.write('_')
    t.forward(7)
    buffer.append('_')

def charHYPHEN():
    t.write('-')
    t.forward(5)
    buffer.append('-')

def charPLUS():
    t.write('+')
    t.forward(5.5)
    buffer.append('+')

def charEQUAL():
    t.write('=')
    t.forward(6)
    buffer.append('=')

def charTAB():
    t.write('    ')
    t.forward(16)
    buffer.append('    ')

def NEWLINE():
    Ycoordinate = t.ycor()
    t.goto(-295, Ycoordinate - 12)
    if (Ycoordinate < -280):
        t.clear()
        t.goto(-295,280)

def charBACKSPACE():
   if buffer:
      twos = ['.', ',']
      threes = ['i', 'j', 'l', 'I', '\'', '`', '|', ':', ';']
      fours = ['f', 'r', 't', ' ', '!', '/', '\\', '[', ']', '{', '}', '(', ')']
      fives = ['k', 'J', '1', '\"', '^', '*', '-']
      sixes = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'n', 'o', 'p', 'q', 's', 'y', 'z', 'E', 'F', 'L', 'P', 'T', '2', '3', '4', '5', '6', '7', '8', '9', '0', '<', '>', '#', '=']
      sevens = ['x', 'B', 'C', 'D', 'H', 'K', 'N', 'R', 'S', 'U', 'Z', '?', '&', '_']
      eights = ['A', 'G', 'M', 'O', 'Q', 'X', 'Y']
      nines = ['m', 'V', 'w']
      fivehalves = ['v', 'u', '$', '~', '+']
      ten = '%'
      elevens = ['W', '@']
      sixteen = '    '
      
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
      elif delchar == ten:
         backvalue = 10
      elif delchar in elevens:
         backvalue = 11
      elif delchar == sixteen:
         backvalue = 16
      
      t.backward(backvalue)
      t.pencolor(bgcolor)
      t.write(delchar)
      t.pencolor(textcolor)

#GET TURTLE CURSOR LOCATION 
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
      '\"' : charQUOTATION,
      '<' : charLTS,
      '>' : charGTS,
      '/' : charFORWARDSLASH,
      '\\' : charBACKSLASH,
      '[' : charBRACKET1,
      ']' : charBRACKET2,
      '{' : charCURLY1,
      '}' : charCURLY2,
      '(' : charPARA1,
      ')' : charPARA2,
      '@' : charAT,
      '#' : charPOUND,
      '$' : charDS,
      '^' : charCARET,
      '&' : charAMPERSAND,
      '*' : charASTERISK,
      '\'' : charAPOSTROPHE,
      '`' : charGRAVE,
      '~' : charTILDE,
      '|' : charPIPE,
      ':' : charCOLON,
      ';' : charSEMICOLON,
      '_' : charUNDERSCORE,
      '-' : charHYPHEN,
      '+' : charPLUS,
      '=' : charEQUAL,
      '    ' : charTAB,
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
    wn.onkey(charFORWARDSLASH, "/")
    wn.onkey(charBACKSLASH, "\\")
    wn.onkey(charBRACKET1, "[")
    wn.onkey(charBRACKET2, "]")
    wn.onkey(charCURLY1, "{")
    wn.onkey(charCURLY2, "}")
    wn.onkey(charPARA1, "(")
    wn.onkey(charPARA2, ")")
    wn.onkey(charAT, "@")
    wn.onkey(charPOUND, "#")
    wn.onkey(charDS, "$")
    wn.onkey(charPERCENT, "%")
    wn.onkey(charCARET, "^")
    wn.onkey(charAMPERSAND, "&")
    wn.onkey(charASTERISK, "*")
    wn.onkey(charAPOSTROPHE, "\'")
    wn.onkey(charGRAVE, "`")
    wn.onkey(charTILDE, "~")
    wn.onkey(charPIPE, "|")
    wn.onkey(charCOLON, ":")
    wn.onkey(charSEMICOLON, ";")
    wn.onkey(charUNDERSCORE, "_")
    wn.onkey(charHYPHEN, "minus")
    wn.onkey(charPLUS, "+")
    wn.onkey(charEQUAL, "=")
    wn.onkey(charTAB, "Tab")
    wn.onkey(ENTER, "Return")

#TURTLE OS FUNCTIONS
def colormessage(text, color):
   t.pencolor(color)
   putstring(text)
   t.pencolor(textcolor)

def TurtleIntro():
   os.chdir(os.getcwd() + "\\root")
   colormessage("Welcome to Turtle OS, enter \"menu\" to see all commands implemented", "Yellow")
   NEWLINE()
   colormessage(pwd(), "Blue")
   putstring(" $ ")
   buffer.clear()

def ENTER():
   command = ReadBuffer()
   ProcessCommand(command)
   NEWLINE()
   colormessage(pwd(), "Blue")
   putstring(" $ ")
   buffer.clear()

def ReadBuffer():
   bufferstring = ""
   for items in buffer:
      bufferstring = bufferstring + items
   print(bufferstring)
   return bufferstring

def ProcessCommand(c):
   NEWLINE()
   commandstring = c.split()
   initialCommand = commandstring.pop(0)
   if initialCommand == "menu":
      menu()
   elif initialCommand == "ls":
      ls()
   elif initialCommand == "clear":
      clear()
   elif initialCommand == "touch":
      touch(commandstring)
   elif initialCommand == "pwd":
      putstring(pwd())
   elif initialCommand == "mkdir":
      mkdir(commandstring)
   elif initialCommand == "cd":
      cd(commandstring)
   elif initialCommand == "rm":
      rm(commandstring)
   elif initialCommand == "rmdir":
      rmdir(commandstring)
   elif initialCommand == "exit":
      turtleEXIT()
   elif initialCommand == "cat":
      cat(commandstring)
   elif initialCommand == "cp":
      cp(commandstring)
   elif initialCommand == "mv":
      mv(commandstring)
   else:
      colormessage("Invalid Command: " + "\"" + c + "\" enter \"menu\" to see all valid commands", "Red")

def menu():
   putstring("ls")
   NEWLINE()
   putstring("clear")
   NEWLINE()
   putstring("touch")
   NEWLINE()
   putstring("pwd")
   NEWLINE()
   putstring("mkdir")
   NEWLINE()
   putstring("cd")
   NEWLINE()
   putstring("rm")
   NEWLINE()
   putstring("rmdir")
   NEWLINE()
   putstring("exit")
   NEWLINE()
   putstring("cat")
   NEWLINE()
   putstring("cp")
   NEWLINE()
   putstring("mv")

def ls():
   path = os.getcwd()
   dir_list = os.listdir(path)  
   for items in dir_list:
      if os.path.isdir(items):
         colormessage(items, "#17ff00")
         NEWLINE()
      else:
         putstring(items)
         NEWLINE()
      
def clear():
   t.clear()
   t.goto(-295,292)
   
def touch(c):
   for items in c:
      f = open(""+(items), "w")
      f.close()

def pwd():
   path = os.getcwd()
   newpath = path.split('\\')
   dirs = ""
   displaypath = []
   result = ""
   while(newpath[-1] != "TurtleOS"):
      displaypath.append(newpath.pop())
   while(displaypath):
      result = result + "\\" + displaypath.pop()
   return result

def mkdir(c):
   for items in c:
      os.mkdir(items)
      
def cd(c):
   if c:
      path = c[0]
      try:
         os.chdir(path)
      except OSError as error:
         colormessage("ERROR: Invalid path", "Red")
   else:
         colormessage("ERROR: Missing arguments after \"cd\"", "Red")

def rm(c):
      if c:
         path = c[0]
         print(path)
         if os.path.exists(path):
            os.remove(path)
         else:
            colormessage("ERROR: Invalid path", "Red")

def rmdir(c):
      if c:
         path = c[0]
         if os.path.exists(path):
            os.rmdir(path)
         else:
            colormessage("ERROR: Invalid path", "Red")

def turtleEXIT():
   try:
      turtle.bye()
   except Exception:
      pass
   
def cat(c):
   catREAD(c)

def catREAD(c):
   for items in c:
      try:
         myfile = open(items)
         txt = myfile.read()
         for parts in txt:
            for chars in parts:
               if '\n' in chars:
                  NEWLINE()
               else:
                  putstring(chars)
         myfile.close()
         NEWLINE()
      except OSError as error:
         colormessage("ERROR: Invalid path", "Red")

def cp(c):
   if c:
      dest = c.pop()
      if c:
         source = c.pop()
         try:
            shutil.copyfile(source, dest)
         except OSError as error:
            colormessage("ERROR: \"" + source + "\" Does not exist", "Red")
      else:
         colormessage("ERROR: requires two arguments only one was provided", "Red")
         
   else:
      colormessage("ERROR: Missing arguments", "Red")

def mv(c):
   if c:
      rmfile = []
      rmfile.append(c[0])
      cp(c)
      rm(rmfile)
   else:
      colormessage("ERROR: Missing arguments", "Red")
   
   
TurtleIntro()
putchar()

wn.listen()
turtle.mainloop()
