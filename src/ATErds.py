from datetime import datetime
import Main
import FileCsv


Main.SetBoard(0)

def Read(dst, ERD, Expected_Data, Path):
    Time = datetime.now().strftime("%H:%M:%S")
    Dia = datetime.now().strftime("%d-%m-%Y")
    Data = Main.ReadErd(dst, ERD)
    Action = "READ"
    if Data == Expected_Data:
        Result = "PASS"
    else:
        Result = "FAIL"
    Write_Dato = "---" 
    Data_To_Write = [Dia, Time, Action, ERD, Expected_Data, Data, Write_Dato ,Result]
    FileCsv.Write_Data_CSV(Path, Data_To_Write)
    print(Data_To_Write)
    
def Write(dst, ERD, Write_Dato ,Path):
    Time = datetime.now().strftime("%H:%M:%S")
    Dia = datetime.now().strftime("%d-%m-%Y")
    Main.WriteButton(dst, ERD, Write_Dato)
    Action = "WRITE"
    Expected_Data = "---"
    Result = "DONE"
    Data = "---"
    Data_To_Write = [Dia, Time, Action, ERD, Expected_Data, Data, Write_Dato ,Result]
    FileCsv.Write_Data_CSV(Path, Data_To_Write)
    print(Data_To_Write)