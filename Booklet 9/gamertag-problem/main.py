def game(X,Y):
  
  
  FileName = "program.txt"
  TextFile = open(FileName, "a")
  TextFile.write(" ")
  TextFile.write(X)
  TextFile.write(" ")
  TextFile.write(Y)
  TextFile.write(" ")
  TextFile.close()

def check():

  with open('program.txt') as myfile:
     if email in myfile.read():
         print('That username is taken')
         exit()

while True:
  try:
    email  = str(input("Please enter your email adress \n"))
    break
  except ValueError:
    print("please enter a valid email adress")

gamertag = input("Please enter your gamertag \n")

check()
game(gamertag,email)
