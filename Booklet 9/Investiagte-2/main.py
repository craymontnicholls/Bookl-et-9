def WriteData():
  FileName = "program data.txt"
  TextFile = open(FileName, "w")
  TextFile.write("An item of data")
  TextFile.close()

def ReadData():
  FileName = "program data.txt"
  TextFile = open(FileName, "r")
  Data = TextFile.readline()
  TextFile.close
  print("{} was read from the file: {}".format(Data, FileName))


WriteData()
ReadData()