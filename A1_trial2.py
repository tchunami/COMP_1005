# Systolic BP 

#Blood Pressure Category Systolic mm/ Hg
#Low 40-89
#Normal 90-120
#Prehypertension 120-139
#High blood Stage 1 140-159
#High blood Stage 2 160-179
#Hypersensitive crisis 180 or higher

#bp = blood pressure

bp = int(input("Enter systolic value to determine your blood pressure case: "))

if 40 <= bp <= 89:
    print("Your systolic value of", bp, "implies that you have LOW blood pressure.")
elif 90 <= bp <= 119:
     print("Your systolic value of", bp, "implies that you have NORMAL blood pressure.")
elif 120 <= bp <= 139:
     print("Your systolic value of", bp, "implies that you have PREHYPERTENSION blood pressure.")
elif 140 <= bp <= 159:
    print("Your systolic value of", bp, "implies that you have STAGE 1 HIGH blood pressure.")
elif 160 <= bp <= 179:
    print("Your systolic value of", bp, "implies that you have STAGE 2 HIGH blood pressure.")
elif bp >= 180:
    print("Your systolic value of", bp, "implies that you have a HYPERSENSITIVE CRISIS, see a doctor ASAP!")
else:
    print("Invalid systolic value, try again.")