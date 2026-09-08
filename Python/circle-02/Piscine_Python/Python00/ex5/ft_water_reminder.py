def ft_water_reminder():
    wa = int(input("Days since last watering: "))
    if wa > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
