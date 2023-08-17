from Initialize import *
from ATDocumentation import AutoDocumentation
from ATErds import *
from UiTable import TableResults
from Functions import *

file_Test = Init()

# Test 1: Lock the LidLock
Test1_1  = Read ("C0", Erd_MC_LidLockFeedbackState,  "01",       file_Test)
Test1_2  = Read ("C0", Erd_MC_LidSwitchState,        "00",       file_Test)
Test1_3  = Read ("C0", Erd_MC_LidLockActualState,    "00",       file_Test)
Test1_4  = ActionDone("Press and hold the Slider (or the switch) in the LidLock",     file_Test)
Test1_5  = Read ("C0", Erd_MC_LidSwitchState,        "01",       file_Test)
Test1_6  = Write("C0", Erd_MC_LidLockRequestState,   "0001",     file_Test)
Test1_7  = ToDoTimedAction(8, "Wait 8 seconds, you will hear a click in the Lidlock", file_Test, 3)
Test1_8  = ActionDone("Release the slider (or the switch)",      file_Test)
Test1_9  = Read ("C0", Erd_MC_LidLockFeedbackState,  "00",       file_Test)
Test1_10 = Read ("C0", Erd_MC_LidLockActualState,    "01",       file_Test)
Test1_11 = Read ("C0", Erd_LidLockPtcReady,          "01",       file_Test)
Test1_12 = Read ("C0", Erd_LidLockPtcActualState,    "01",       file_Test)

# Test 2: Unlock the LidLock
Test2_1  = Write("C0", Erd_MC_LidLockRequestState,   "0000",     file_Test)
Test2_2  = Read ("C0", Erd_MC_LidLockFeedbackState,  "01",       file_Test)
Test2_3  = Read ("C0", Erd_MC_LidLockActualState,    "00",       file_Test)
Test2_4  = Read ("C0", Erd_LidLockPtcReady,          "01",       file_Test)
Test2_5  = Read ("C0", Erd_LidLockPtcActualState,    "01",       file_Test)

# Test 3: Lock the LidLock on the second tries to lock
Test3_1  = Write("C0", Erd_MC_LidLockRequestState,    "0001",     file_Test)
Test3_2  = ToDoTimedAction(8, "Verify that after 8 seconds there will be 5 tries to lock the Lidlock",   file_Test, 3)
Test3_3  = ToDoTimedAction(38, "Wait 8 + 30 seconds for the second tries to lock",                       file_Test)
Test3_4  = ActionDone("In the second tries start press and hold the Slider, wait for the tries to stop", file_Test)
Test3_5  = ActionDone("Release the slider (or the switch)",                                              file_Test)
Test3_6  = Read ("C0", Erd_MC_LidLockFeedbackState,   "00",      file_Test)
Test3_7  = Read ("C0", Erd_MC_LidLockActualState,     "00",      file_Test)
Test3_8  = Write("C0", Erd_MC_LidLockRequestState,    "0000",    file_Test)

# Test 4: Try to lock the LidLock with the door open all the time
Test4_1  = Write("C0", Erd_MC_LidLockRequestState,                  "0001",    file_Test)
Test4_2  = ToDoTimedAction(8, "Wait for the first tries to lock the Lidlock, let it stop trying",   file_Test, 3)
Test4_3  = ToDoTimedAction(38, "Wait 8 + 30 seconds for the second tries, let it stop trying",      file_Test)
Test4_4  = Read ("C0", Erd_MC_LidLockActualState,                   "02",      file_Test)
Test4_5  = Read ("C0", Erd_LevelFault_LidLockFailure,               "01",      file_Test)
Test4_6  = Read ("C0", Erd_LevelFault_CriticalLidLockFailureToLock, "01",      file_Test)
Test4_7  = Write("C0", Erd_MC_LidLockRequestState,                  "0000",    file_Test)
Test4_8  = Read ("C0", Erd_MC_LidLockActualState,                   "00",      file_Test)
Test4_9  = Read ("C0", Erd_LevelFault_LidLockFailure,               "02",      file_Test)

# Test 5: Lock the LidLock after the second tries
Test5_1  = Write("C0", Erd_MC_LidLockRequestState,                  "0001",    file_Test)
Test5_2  = ToDoTimedAction(8, "Wait for the first tries to lock the Lidlock, let it stop trying",   file_Test, 3)
Test5_3  = ToDoTimedAction(38, "Wait 8 + 30 seconds for the second tries, let it stop trying",      file_Test)
Test5_4  = Write("C0", Erd_MC_LidLockRequestState,                  "0000",    file_Test)
Test5_5  = Write("C0", Erd_MC_LidLockRequestState,                  "0001",    file_Test)
Test5_6  = ToDoTimedAction(240, "Press and hold the Slider and wait for the 4 minutes to complete", file_Test, 3)
Test5_7  = ActionDone("After the click has been listened, release the slider",                      file_Test)
Test5_8  = Read ("C0", Erd_MC_LidLockFeedbackState,                 "00",      file_Test)
Test5_9  = Read ("C0", Erd_MC_LidLockActualState,                   "01",      file_Test)
Test5_10 = Read ("C0", Erd_LevelFault_LidLockFailure,               "00",      file_Test)
Test5_11 = Read ("C0", Erd_LevelFault_CriticalLidLockFailureToLock, "00",      file_Test)
Test5_12 = Write("C0", Erd_MC_LidLockRequestState,                  "0000",    file_Test)

List_Results = [HEADERS, Test1_1, Test1_2, Test1_3, Test1_4, Test1_5, Test1_6, Test1_7, 
            Test1_8, Test1_9, Test1_10, Test1_11, Test1_12,
            Test2_1, Test2_2, Test2_3, Test2_4, Test2_5
            Test3_1, Test3_2, Test3_3, Test3_4, Test3_5, Test3_6, Test3_7, Test3_8]

List_Results2 = [HEADERS, Test4_1, Test4_2, Test4_3, Test4_4, Test4_5, Test4_6, Test4_7, Test4_8, Test4_9, 
            Test5_1, Test5_2, Test5_3, Test5_4, Test5_5, Test5_6, Test5_7, Test5_8, Test5_9, Test5_10,
            Test5_11, Test5_12]

TableResults(List_Results,  "T462: Tests form Test 1 to Test 3")
TableResults(List_Results2, "T462: Tests form Test 4 to Test 5")


texto = """ """

AutoDocumentation(texto)