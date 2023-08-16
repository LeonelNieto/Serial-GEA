from Initialize import *
from ATDocumentation import AutoDocumentation
from ATErds import *
from UiTable import TableResults
from Functions import *

file_Test = Init()

Test1_1  = Write("C0", Erd_MabeCommunicationConfiguration,  "01",     file_Test)
Test1_2  = Write("C0", Erd_MabeCommunicationRequest1Levels, "0011",   file_Test)
Test1_3  = ActionPassOrFail("Temp and spin level leds shall turn on in level 1")
Test1_4  = Write("C0", Erd_MabeCommunicationRequest1Levels, "0022",   file_Test)
Test1_5  = ActionPassOrFail("Temp and spin level leds shall turn on in level 2")
Test1_6  = Write("C0", Erd_MabeCommunicationRequest1Levels, "0033",   file_Test)
Test1_7  = ActionPassOrFail("Temp and spin level leds shall turn on in level 3")
Test1_8  = Write("C0", Erd_MabeCommunicationRequest1Levels, "0044",   file_Test)
Test1_9  = ActionPassOrFail("Temp and spin level leds shall turn on in level 4")
Test1_10 = Write("C0", Erd_MabeCommunicationRequest1Levels, "0055",   file_Test)
Test1_11 = ActionPassOrFail("Temp and spin level leds shall turn on in level 5")
Test1_12 = Write("C0", Erd_MabeCommunicationRequest1Levels, "0000",   file_Test)
Test1_13 = ActionPassOrFail("Temp and spin level leds shall turn off")
Test1_14 = Write("C0", Erd_MabeCommunicationRequest1Levels, "0001",   file_Test)
Test1_15 = ActionPassOrFail("Spin level led shall turn on in level 1")
Test1_16 = Write("C0", Erd_MabeCommunicationRequest1Levels, "0010",   file_Test)
Test1_17 = ActionPassOrFail("Temp level led shall turn on in level 1")
Test1_18 = Write("C0", Erd_MabeCommunicationRequest1Levels, "0030",   file_Test)
Test1_19 = ActionPassOrFail("Temp level led shall turn on in level 3")
Test1_20 = Write("C0", Erd_MabeCommunicationRequest1Levels, "0003",   file_Test)
Test1_21 = ActionPassOrFail("Spin level led shall turn on in level 3")
Test1_22 = Write("C0", Erd_MabeCommunicationRequest1Levels, "0005",   file_Test)
Test1_23 = ActionPassOrFail("Spin level led shall turn on in level 5")
Test1_24 = Write("C0", Erd_MabeCommunicationRequest1Levels, "0050",   file_Test)
Test1_25 = ActionPassOrFail("Temp level led shall turn on in level 5")

Test2_1  = Write("C0", Erd_MabeCommunicationConfiguration,  "00",         file_Test)
Test2_2  = Write("C0", Erd_MabeCommunicationRequest2Icons,  "100000",     file_Test)
Test2_3  = ActionPassOrFail("Verify nothing happen")
Test2_4  = Write("C0", Erd_MabeCommunicationConfiguration,  "01",         file_Test)
Test2_5  = Write("C0", Erd_MabeCommunicationRequest2Icons,  "100000",     file_Test)
Test2_6  = ActionPassOrFail("Two points Icon shall turn on")

Test3_1  = Write("C0", Erd_MabeCommunicationConfiguration,  "00",               file_Test)
Test3_2  = Write("C0", Erd_MabeCommunicationRequest2Units,  "3034323000000000", file_Test) 
Test3_3  = ActionPassOrFail("Verify nothing happen")
Test3_4  = Write("C0", Erd_MabeCommunicationConfiguration,  "01",               file_Test)
Test3_5  = Write("C0", Erd_MabeCommunicationRequest2Units,  "3034323000000000", file_Test) 
Test3_6  = ActionPassOrFail("Display shall turn on '04:20'")
Test3_7  = Write("C0", Erd_MabeCommunicationRequest2Units,  "3138303900000000", file_Test) 
Test3_8  = ActionPassOrFail("Display shall turn on '18:09'")


lst = [HEADERS, Test1_1, Test1_2, Test1_3, Test1_4, Test1_5, Test1_6, Test1_7, Test1_8,
        Test1_9, Test1_10, Test1_11, Test1_12, Test1_13, Test1_14, Test1_15, Test1_16, 
        Test1_17, Test1_18, Test1_19, Test1_20, Test1_21, Test1_22, Test1_23, Test1_24, Test1_25,
        Test2_1, Test2_2, Test2_3, Test2_4, Test2_5, Test2_6,
        Test3_1, Test3_2, Test3_3, Test3_4, Test3_5, Test3_6, Test3_7, Test3_8]

TableResults(lst, "T481")

texto = """"""

AutoDocumentation(texto)