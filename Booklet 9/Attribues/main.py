


def WriteData():

  
  
  FileName = "program data.txt"
  TextFile = open(FileName, "w")
  TextFile.write("Name:{}".format(name))
  TextFile.write("Attack:{}".format(attack))
  TextFile.write("Defence:{}".format(defence))

name = input("Please enter your charater's name \n")
while True:
  try:
    attack = int(input("Please enter your charater's attack between 1-100 \n"))
    break

  except ValueError:
    print("Sorry, Please enter a number \n")

while True:
  try:
    defence = int(input("Please enter your charater's defence between 1-100 \n"))
    break

  except ValueError:
    print("Please enter a number")

WriteData()


