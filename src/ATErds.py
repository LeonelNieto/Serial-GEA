from datetime import datetime
import Main
import FileCsv
import time

def Read(dst, ERD, Expected_Data, Path):
    Time = datetime.now().strftime("%H:%M:%S")
    Dia = datetime.now().strftime("%d-%m-%Y")
    Data = Main.ReadErd(dst, ERD)
    Action = "READ"
    if Data == Expected_Data:
        Result = "PASS"
        Comments = "---"
    else:
        Result = "FAIL"
        if len(Data) != len(Expected_Data):
            lenData = str(int(len(Data) / 2))
            lenExpected_Data = str(int(len(Expected_Data) / 2))
            Comments = f"Length from data read {Data} ({lenData}) is diferent " +\
                        f"that expected data {Expected_Data} ({lenExpected_Data})"
        else:
            Comments = f"Expected data {Expected_Data} != Data {Data}"
    Write_Dato = "---" 
    Data_To_Write = [Dia, Time, Action, ERD, Expected_Data, Data, Write_Dato, Result, Comments]
    FileCsv.Write_Data_CSV(Path, Data_To_Write)
    print(Data_To_Write)
    return Data_To_Write
    
def Write(dst, ERD, Write_Dato ,Path):
    time.sleep(0.2)
    Time = datetime.now().strftime("%H:%M:%S")
    Dia = datetime.now().strftime("%d-%m-%Y")
    Main.WriteButton(dst, ERD, Write_Dato)
    Action = "WRITE"
    Expected_Data = "---"
    Result = "DONE"
    Data = "---"
    Comments = "---"
    Data_To_Write = [Dia, Time, Action, ERD, Expected_Data, Data, Write_Dato, Result, Comments]
    FileCsv.Write_Data_CSV(Path, Data_To_Write)
    time.sleep(0.2)
    print(Data_To_Write)
    return Data_To_Write