def WriteData():
  FileName = "program data.txt"
  TextFile = open(FileName, "w")
  TextFile.write("Ollie\n")
  TextFile.write("Morris\n")
  TextFile.close()

def ReadData():
  FileName = "program data.txt"
  TextFile = open(FileName, "r")
  Data = " "
  while(Data):
    Data = TextFile.readline()
    if Data: print(Data)
  TextFile.close()
  
 


WriteData()
ReadData()