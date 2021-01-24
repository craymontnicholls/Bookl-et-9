def cookiewrite():
  FileName = "program data.txt"
  theme = input("Enter if you want dark or light theme \n")
  TextFile = open(FileName, "w")
  TextFile.write(theme)
  
  TextFile.close()

def cookieread():
  FileName = "program data.txt"
  TextFile = open(FileName, "r")
  Data = " "
  while(Data):
    Data = TextFile.readline()
    if Data: print("You chose {} theme".format(Data))
  TextFile.close()


cookiewrite()
cookieread()