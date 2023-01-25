def longitudERD(ERD):
    numeroCaracteres = len(ERD)
    if numeroCaracteres == 0 or numeroCaracteres > 4:
        ERD = "Fallo"
    elif numeroCaracteres == 1:
        ERD = "000" + ERD
    elif numeroCaracteres == 2:
        ERD = "00" + ERD
    elif numeroCaracteres == 3:
        ERD = "0" + ERD
    elif numeroCaracteres == 4:
        ERD = ERD
    else:
        ERD = "Fallo"

    return ERD
