# /***********************************************************************/
# /*                                                                     */
# /*  FILE          : verifylength.py                                    */
# /*  DATE          : 17/02/2023                                         */
# /*  DESCRIPTION   : Calculate ERD length                               */
# /*                                                                     */
# /*  AUTHOR        : Leonel Nieto Lara                                  */
# /*                                                                     */
# /*  PROJECT       : GEA3 Tool                                          */
# /*  IDE           : Visual Studio Code                                 */
# /*  Python Version: 3.9.13                                             */
# */                                                                     */
# /*  Copyright 2012-2023 Mabe TyP                                       */
# /*  All rights reserved                                                */
# /*                                                                     */
# /***********************************************************************/

# /************************************************************************
#  Name:          longitudERD   
#  Parameters:    ERD
#  Returns:       Complete length or ERD
#                 Fallo
#  Called by:     ReadButton( ) from (Main.py)
#                 WriteButton( ) from (Main.py)
#  Calls:         N/A
#  Description:   Complete the ERD with 0's in the left if lenght is
#                 less than 4, if length is 4 return the same
#                 ERD, else return "Fallo"
#               
# ************************************************************************/
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
