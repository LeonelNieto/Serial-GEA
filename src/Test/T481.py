from Initialize import *
from ATDocumentation import AutoDocumentation
from ATErds import *
from UiTable import TableResults
from Functions import *

file_Test = Init()

# Test 1: New ERD Erd_MabeCommunicationRequest1Levels.
Test1_1  = Write("C0", Erd_MabeCommunicationConfiguration,  "01",       file_Test)
Test1_2  = Write("C0", Erd_MabeCommunicationRequest1Levels, "001100",   file_Test)
Test1_3  = ActionPassOrFail("Temp and spin level leds shall turn on in level 1")
Test1_4  = Write("C0", Erd_MabeCommunicationRequest1Levels, "002200",   file_Test)
Test1_5  = ActionPassOrFail("Temp and spin level leds shall turn on in level 2")
Test1_6  = Write("C0", Erd_MabeCommunicationRequest1Levels, "003300",   file_Test)
Test1_7  = ActionPassOrFail("Temp and spin level leds shall turn on in level 3")
Test1_8  = Write("C0", Erd_MabeCommunicationRequest1Levels, "004400",   file_Test)
Test1_9  = ActionPassOrFail("Temp and spin level leds shall turn on in level 4")
Test1_10 = Write("C0", Erd_MabeCommunicationRequest1Levels, "005500",   file_Test)
Test1_11 = ActionPassOrFail("Temp and spin level leds shall turn on in level 5")
Test1_12 = Write("C0", Erd_MabeCommunicationRequest1Levels, "000000",   file_Test)
Test1_13 = ActionPassOrFail("Temp and spin level leds shall turn off")
Test1_14 = Write("C0", Erd_MabeCommunicationRequest1Levels, "000100",   file_Test)
Test1_15 = ActionPassOrFail("Spin level led shall turn on in level 1")
Test1_16 = Write("C0", Erd_MabeCommunicationRequest1Levels, "001000",   file_Test)
Test1_17 = ActionPassOrFail("Temp level led shall turn on in level 1")
Test1_18 = Write("C0", Erd_MabeCommunicationRequest1Levels, "003000",   file_Test)
Test1_19 = ActionPassOrFail("Temp level led shall turn on in level 3")
Test1_20 = Write("C0", Erd_MabeCommunicationRequest1Levels, "000300",   file_Test)
Test1_21 = ActionPassOrFail("Spin level led shall turn on in level 3")
Test1_22 = Write("C0", Erd_MabeCommunicationRequest1Levels, "000500",   file_Test)
Test1_23 = ActionPassOrFail("Spin level led shall turn on in level 5")
Test1_24 = Write("C0", Erd_MabeCommunicationRequest1Levels, "005000",   file_Test)
Test1_25 = ActionPassOrFail("Temp level led shall turn on in level 5")

# Test 2. Two points icon
Test2_1  = Write("C0", Erd_MabeCommunicationConfiguration,  "00",         file_Test)
Test2_2  = Write("C0", Erd_MabeCommunicationRequest2Icons,  "100000",     file_Test)
Test2_3  = ActionPassOrFail("Verify nothing happend")
Test2_4  = Write("C0", Erd_MabeCommunicationConfiguration,  "01",         file_Test)
Test2_5  = Write("C0", Erd_MabeCommunicationRequest2Icons,  "100000",     file_Test)
Test2_6  = ActionPassOrFail("Two points Icon shall turn on")
Test2_7  = Write("C0", Erd_MabeCommunicationRequest2Icons,  "000000",     file_Test)
Test2_8  = ActionPassOrFail("Two points Icon shall turn off")

# Test 3: Write an specific hour in the display with two points icon
Test3_1  = Write("C0", Erd_MabeCommunicationConfiguration,  "00",               file_Test)
Test3_2  = Write("C0", Erd_MabeCommunicationRequest2Units,  "3034323000000000", file_Test)
Test3_3  = Write("C0", Erd_MabeCommunicationRequest2Icons,  "100000",           file_Test) 
Test3_4  = ActionPassOrFail("Verify nothing happend")
Test3_5  = Write("C0", Erd_MabeCommunicationConfiguration,  "01",               file_Test)
Test3_6  = Write("C0", Erd_MabeCommunicationRequest2Units,  "3034323000000000", file_Test)
Test3_7  = Write("C0", Erd_MabeCommunicationRequest2Icons,  "100000",           file_Test)  
Test3_8  = ActionPassOrFail("Display shall turn on '04:20'")
Test3_9  = Write("C0", Erd_MabeCommunicationRequest2Units,  "3138303900000000", file_Test) 
Test3_10 = ActionPassOrFail("Display shall turn on '18:09'")

lst = [HEADERS, Test1_1, Test1_2, Test1_3, Test1_4, Test1_5, Test1_6, Test1_7, Test1_8,
        Test1_9, Test1_10, Test1_11, Test1_12, Test1_13, Test1_14, Test1_15, Test1_16, 
        Test1_17, Test1_18, Test1_19, Test1_20, Test1_21, Test1_22, Test1_23, Test1_24, Test1_25,
        Test2_1, Test2_2, Test2_3, Test2_4, Test2_5, Test2_6, Test2_7, Test2_8,
        Test3_1, Test3_2, Test3_3, Test3_4, Test3_5, Test3_6, Test3_7, Test3_8]

TableResults(lst, "T481")

texto = """Test 1: New ERD Erd_MabeCommunicationRequest1Levels.
Write (0x01) to Erd_MabeCommunicationConfiguration.
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