def meeting(rooms, number):
    chairs = []
    if number == 0:
        return "Game On"
    else:    
        for r in rooms:
            sparechairs = r[1] - len(r[0])
            if sparechairs > 0 and number > 0:
                if sparechairs <= number:
                    chairs.append(sparechairs)
                    number -= sparechairs
                else:
                    chairs.append(number)
                    number -= number
            elif number > 0:
                chairs.append(0)
        if number == 0:
            return chairs
        else: return "Not enough!"

