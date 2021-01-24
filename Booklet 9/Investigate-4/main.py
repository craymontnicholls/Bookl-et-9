def ReadData():
  FileName = "program data 2.txt"
  try:
    TextFile = open(FileName, "r")
    Data = " "
    while(Data):
      Data = TextFile.readline()
      if Data: print(Data)
    TextFile.close()

  except:
    print("File not Found {}".format(FileName))

ReadData()