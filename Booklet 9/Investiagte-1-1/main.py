def WriteData():
  FileName = "program data.txt"
  forename = input("please enter your forename \n")
  surname = input("please enter your surname \n")

  TextFile = open(FileName, "w")
  TextFile.write(forename)
  TextFile.write(surname)
  TextFile.close()


WriteData()