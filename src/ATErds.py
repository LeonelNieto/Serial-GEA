from datetime import datetime
import Main
import FileCsv
import time

def Read(dst:str, ERD:str, Expected_Data:str, Path="", board=1):
    Main.SetBoard(board)
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
            Comments = f"Lenght {Expected_Data} ({lenExpected_Data}) != " +\
                        f"{Data} ({lenData})"
        else:
            Comments = f"{Expected_Data} != {Data}"
    Write_Dato = "---" 
    Data_To_Write = [Dia, Time, Action, ERD, Expected_Data, Data, Write_Dato, Result, Comments]
    if len(Path) != 0:
        FileCsv.Write_Data_CSV(Path, Data_To_Write)
    Main.ser.close()
    print(Data_To_Write)
    return Data_To_Write
    
def Write(dst:str, ERD:str, Write_Dato:str, Path="", board=1):
    Main.SetBoard(board)
    time.sleep(0.3)
    Time = datetime.now().strftime("%H:%M:%S")
    Dia = datetime.now().strftime("%d-%m-%Y")
    Main.WriteButton(dst, ERD, Write_Dato)
    Action = "WRITE"
    Expected_Data = "---"
    Result = "DONE"
    Data = "---"
    Comments = "---"
    Data_To_Write = [Dia, Time, Action, ERD, Expected_Data, Data, Write_Dato, Result, Comments]
    if len(Path) != 0:
        FileCsv.Write_Data_CSV(Path, Data_To_Write)
    time.sleep(3.4)
    print(Data_To_Write)
    Main.ser.close()
    return Data_To_Write
