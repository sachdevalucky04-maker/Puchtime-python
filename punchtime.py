
for user in range(1, 3):
    print("User", user)
    for day in range(1, 8):
        print("Day", day)
        entrytime = int(input("Entry time: "))
        exittime = int(input("Exit time: "))
        if entrytime == 8 and exittime == 17:
            print("Present")
        elif entrytime > 8 and exittime == 17 or entrytime >8 and exittime >=17:
            print("late")
        elif entrytime == 0 and exittime == 0:
            print("Absent")
        elif entrytime == 8 and exittime < 17:
            print("Half day")
        elif entrytime >= 8 and exittime <= 12:
            print("Short day")
        elif entrytime < 8 and exittime == 17 or entrytime >= 8 and exittime > 17:
         print("overtime")
        else:
            print("Invalid")




