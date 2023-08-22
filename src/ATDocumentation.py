"""
Este módulo realiza la documentación automatica, agregando 
PASS and DONE, además de agregar el valor hexadecimal del ERD
"""
import re
from Erd_List import *

erd_dict = {key: value for key, value in locals().items() if key.startswith('Erd_')}

def AutoDocumentation(texto:str) -> None:
    """
    Función para documentar automáticamente los tickets
    
    Args:
        texto (str): Texto que se quiere documentar
        
    return:
        print() con el texto documentado
    """
    texto_modificado = re.sub(r'(?<=\b\w)(?=\b)', '- ', texto)
    for erd_nombre, erd_valor in erd_dict.items():
        erd_regex = re.compile(rf"\b{erd_nombre}\b")
        texto_modificado = erd_regex.sub(erd_nombre + " (0x" + erd_valor + ")", texto_modificado)

    lineas = texto_modificado.split('\n')
    for i in range(len(lineas)):
        if lineas[i].startswith('Read') or lineas[i].startswith('Verify'):
            lineas[i] += ' **-->PASS**'
        else:
            lineas[i] += ' **-->DONE**'

    texto_modificado = '\n'.join(lineas)
    print(texto_modificado)

texto = texto = """Test 1: New ERD Erd_MabeCommunicationRequest1Levels.
Write (0x001100) to Erd_MabeCommunicationRequest1Levels.
Verify that temperature and spin level leds shall turn on at level 1.
Write (0x002200) to Erd_MabeCommunicationRequest1Levels.
Verify that temperature and spin level leds shall turn on at level 2.
Write (0x003300) to Erd_MabeCommunicationRequest1Level.
Verify that temperature and spin level leds shall turn on at level 3.
Write (0x004400) to Erd_MabeCommunicationRequest1Levels.
Verify that temperature and spin level leds shall turn on at level 4.
Write (0x005500) to Erd_MabeCommunicationRequest1Levels.
Verify that temperature and spin level leds shall turn on at level 5.
Write (0x000000) to Erd_MabeCommunicationRequest1Levels.
Verify that temperature and spin level leds shall turn off.
Write (0x000100) to Erd_MabeCommunicationRequest1Levels.
Verify that spin level led shall turn on at level 1.
Write (0x001000) to Erd_MabeCommunicationRequest1Levels.
Verify that temperature level led shall turn on at level 1.
Write (0x000300) to Erd_MabeCommunicationRequest1Levels.
Verify that spin level led shall turn on at level 3.
Write (0x003000) to Erd_MabeCommunicationRequest1Levels.
Verify that temperature level led shall turn on at level 3.
Write (0x000500) to Erd_MabeCommunicationRequest1Levels.
Verify that spin level led shall turn on at level 5.
Write (0x005000) to Erd_MabeCommunicationRequest1Levels.
Verify that temperature level led shall turn on at level 5.

Test 2: Two points icon.
Write (0x00) to Erd_MabeCommunicationConfiguration.
Write (0x100000) to Erd_MabeCommunicationRequest2Icons.
Verify that nothings happend.
Write (0x01) to Erd_MabeCommunicationConfiguration.
Write (0x100000) to Erd_MabeCommunicationRequest2Icons.
Verify two point icon shall turn on.
Write (0x000000) to Erd_MabeCommunicationRequest2Icons.
Verify two point icon shall turn off.

Test 3: Write an specific hour in the display with two points icon.
Write (0x00) to Erd_MabeCommunicationConfiguration.
Write (0x3034323000000000) to Erd_MabeCommunicationRequest2Units.
Write (0x100000) to Erd_MabeCommunicationRequest2Icons.
Verify that nothing happend.
Write (0x01) to Erd_MabeCommunicationConfiguration.
Write (0x3034323000000000) to Erd_MabeCommunicationRequest2Units.
Write (0x100000) to Erd_MabeCommunicationRequest2Icons.
Verify display shall turn on "04:20".
Write (0x3138303900000000) to Erd_MabeCommunicationRequest2Units.
Verify display shall turn on "18:09"."""

AutoDocumentation(texto)