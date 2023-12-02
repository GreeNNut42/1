calibrationFile = open("./calibration", "r")
rawCalib = calibrationFile.readlines()
sumCalibrationValues = 0
for line in rawCalib :
    temp = 0
    for character in line :
        if character.isnumeric():
            temp = int(character)*10
            break
    for character in line [ : :-1]:
        if character.isnumeric():
            temp += int(character)
            break
    sumCalibrationValues += temp
            
print(sumCalibrationValues)


calibrationFile.close()