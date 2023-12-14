def longitudERD(ERD) -> str:
    """
    Función que completa el ERD con '0' a la izquierda si la 
    longitud es menor que cuatro.
    
    Args:
        ERD (str): ERD que se quiere consultar
    
    Returns:
        (str): Erd completo o Fallo
        
    Examples
    --------
    >>> longitud('02')
    '0002'
    >>> longitud('00122')
    'Fallo'
    """
    numeroCaracteres = len(ERD) 
    ERD = ERD.upper()
    return {
        1 : "000" + ERD,
        2 :  "00" + ERD,
        3 :   "0" + ERD,
        4:          ERD 
    }.get(numeroCaracteres, "Fallo")
