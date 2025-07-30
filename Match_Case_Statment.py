def day_of_week(day):
    match day:
        case 1:
            return "It is Sunday"
        case 2:
            return "It is Monday"
        case 3:
            return "It is ThusDay"
        case 4:
            return "It is Wednesday"
        case 5:
            return "It is Thersday"
        case 6:
            return "It is Friday"
        case 7:
            return "It is Saturday"
        case _:
            return "Invalid Input"
print(day_of_week(2))