import csv

def Write_Data_CSV(PathFile, Data):
    with open(PathFile, "a") as file: 
        file = csv.writer(file, delimiter=",",
                            quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
        file.writerow(Data)

