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
        Comments = "N/A"
    else:
        Result = "FAIL"
        if len(Data) != len(Expected_Data):
            lenData = str(int(len(Data) / 2))
            lenExpected_Data = str(int(len(Expected_Data) / 2))
            Comments = f"Length from data read {Data} ({lenData}) is diferent " +\
                        f"that expected data {Expected_Data} ({lenExpected_Data})"
        else:
            Comments = "Value is diferent"
    Write_Dato = "---" 
    Data_To_Write = [Dia, Time, Action, ERD, Expected_Data, Data, Write_Dato, Result ,Comments]
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