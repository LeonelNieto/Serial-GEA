import re
from Erd_List import *

texto = '''Read Erd_UI_CycleSelection, shall be (00)
Read Erd_MC_CycleEngineRequestState shall be (000005):
Read Erd_UI_MachineStateEnter, shall be (00)
Read Erd_UI_MachineStateExit, shall be (00)
Read Erd_MC_CycleCount, shall be (0A)
Write (01) to Erd_UI_CycleSelection
Read Erd_LaundryCurrentSelectedCycle, shall be (05)
Read Erd_MC_CycleEngineRequestState shall be (000105):
Read Erd_MC_CycleEngineActualState (010A):
Write UiState_Run (08) to Erd_UI_MachineStateEnter
Read Erd_UI_CycleSelection, shall be (01)
Read Erd_MC_CycleEngineRequestState shall be (000101)
Read Erd_MC_CycleEngineActualState shall be (0106)
Read Erd_AutoSoakLevelOption, shall be AutoSoakLevel_0_Off (00)
Read Erd_DeepFillIncrementalOption, shall be DeepFillIncremental_Off  (00)
Read Erd_ExtraRinseOption, shall be ExtraRinse_Disable (00)
Read Erd_SoilLevelOption, shall be SoilLevel_Normal (03)
Read Erd_StainRemovalGuideOption, shall be StainRemovalGuideOption_Off  (00)
Read Erd_WaterOnDemandSoapDispenseOption, shall be WaterOnDemandSoapDispenseOption_Disabled  (00)
Read Erd_ControlLockOption, shall be ControlLockOption_Disable (00)
Read Erd_DelayWashOption, shall be DelayWashOption_Disabled (00)
Read Erd_FabricSoftenerOption, shall be FabricSoftener_Disable (00)
Read Erd_SpinLevelOption, shall be SpinLevel_Normal(03)
Read Erd_WarmRinseOption, shall be WarmRinse_Disable (00)
Read Erd_WaterTemperatureOption, shall be WaterTemp_Cool (02)
Write (03) to Erd_UI_CycleSelection
Read Erd_LaundryCurrentSelectedCycle, shall be CycleSelected_BulkyItems (04)
Read Erd_MC_CycleEngineRequestState shall be (000305)
Read Erd_MC_CycleEngineActualState shall be (030A)
Read Erd_AutoSoakLevelOption, shall be AutoSoakLevel_1 (01)
Read Erd_DeepFillIncrementalOption, shall be DeepFillIncremental_MaxFill (02)
Read Erd_ExtraRinseOption, shall be ExtraRinse_Disable (00)
Read Erd_SoilLevelOption, shall be SoilLevel_Light (02)
Read Erd_StainRemovalGuideOption, shall be StainRemovalGuideOption_Beverages (05)
Read Erd_WaterOnDemandSoapDispenseOption, shall be WaterOnDemandSoapDispenseOption_Disabled (00)
Read Erd_ControlLockOption, shall be ControlLockOption_Unlocked (01)
Read Erd_DelayWashOption, shall be DelayWashOption_Disabled (00)
Read Erd_FabricSoftenerOption, shall be FabricSoftener_Disable (00)
Read Erd_SpinLevelOption, shall be SpinLevel_NoSpin(01)
Read Erd_WarmRinseOption, shall be WarmRinse_Enable (01)
Read Erd_WaterTemperatureOption, shall be WaterTemp_Hot (05)
Read Erd_MC_CycleCount, shall be (0A)'''

erd_dict = {key: value for key, value in locals().items() if key.startswith('Erd_')}

texto_modificado = re.sub(r'(?<=\b\w)(?=\b)', '- ', texto)

for erd_nombre, erd_valor in erd_dict.items():
    erd_regex = re.compile(rf"\b{erd_nombre}\b")
    texto_modificado = erd_regex.sub(erd_nombre + " (0x" + erd_valor + ")", texto_modificado)

# Agregar PASS o DONE al final de cada oración
lineas = texto_modificado.split('\n')
for i in range(len(lineas)):
    if lineas[i].startswith('Read'):
        lineas[i] += ' **-->PASS**'
    else:
        lineas[i] += ' **-->DONE**'

texto_modificado = '\n'.join(lineas)

print(texto_modificado)



