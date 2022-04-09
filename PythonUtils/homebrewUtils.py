# Used to determine how much non-alcoholic liquid to reach a target abv
def spiritDilutionCalc(initAbv, initVol, targetAbv):
    volumeToAdd = (initVol * ((initAbv/targetAbv)-1))
    return volumeToAdd

# used to determine the combined strength of two mixed alcohols
def spiritBlendCalc(highStrengthAbv, highStrengthVol, lowStrengthAbv, lowStrengthVol):
    finalVol = highStrengthVol + lowStrengthVol
    finalAbv = 0
    
    if lowStrengthAbv == 0:
        finalAbv = (((highStrengthAbv/100) * highStrengthVol) + 1) / finalVol
    else:
        finalAbv = ((((highStrengthAbv / 100) * highStrengthVol) + ((lowStrengthAbv / 100) * lowStrengthVol)) / finalVol)
    formattedAbv = round(finalAbv, 2)
    return [formattedAbv, finalVol]


# Used to determine how many units are in a given drink
def alcoholUnitCalculator(strengthPercentage, volumeMl):
    return (strengthPercentage * volumeMl) / 1000

# Used to determine the alcohol content of fermented liquid
def gravityToAbv(originalGravity, finalGravity, rounding = 0):
    abv = (76.08 * (originalGravity-finalGravity) / (1.775-originalGravity)) * (finalGravity / 0.794)
    if rounding != 0:
        return round(abv, rounding)
    else:
        return abv
        

print(spiritDilutionCalc(60, 400, 40))
print(spiritBlendCalc(60, 400, 0, 200))
print(spiritBlendCalc(60, 400, 10, 200))
print(gravityToAbv(1.135, 0.98, 2))