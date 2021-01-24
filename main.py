def takeinput():
  Valid_input = False
  while Valid_input == False:
    user_input = input("> ") 
    try:
      user_input.lower()
      Valid_input = True
      return user_input
    except ValueError:
      print("please enter a string.")


def create():
  global FileName
  while True:
    try:
      FileName = input("Enter the filename you want to make")
      break
    except ValueError :
      print("A file with this name already exists choose another")

  f = open(FileName , "x")

def add():
  items = input("please enter your items with a ',' between each one \n")
  f = open(FileName, "a")
  f.write(items)
  f.close()

def remove():
  f = open(FileName, 'r+')
  f.truncate(0)
  


def output():
  
  TextFile = open(FileName, "r")

  Data = " "
  while(Data):
    Data = TextFile.readline()
    if Data: print(Data)
  TextFile.close()

def Action(action):
  action = action.lower()
  if action == "add":
    add()
  elif action == "create":
    create()
  elif action == "print":
    output()

def access():
  
  valid_action = False

  while valid_action == False:

    action = input("Select an action \n")
    try:
      action = action.lower()
    except ValueError: 
      print("\n Please enter an action")

    if action == "add" or action == "create" or action == "print" or action == "remove":
      Action(action)
    else:
      print("please select a valid action \n \n")


access()
