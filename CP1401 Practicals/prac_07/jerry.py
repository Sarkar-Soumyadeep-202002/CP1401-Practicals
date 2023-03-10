def km_to_miles(dist_inkilo):

    conversionrate=0.621371
    dist_inmiles=dist_inkilo*conversionrate
    return dist_inmiles


def determine_fine():
    speed_limit=float(input('Enter your speed limit in km/hr: '))
    speed_limit=km_to_miles(speed_limit)
    speed=float(input('Enter your speed in miles/hr: '))
    if speed<(speed_limit+13):
        fine=0

    elif speed>(speed_limit+13) and speed<(speed_limit+20):
        fine=266

    elif speed>=(speed_limit+20) and speed<(speed_limit+30):
        fine=444

    elif speed>=(speed_limit+30) and speed<(speed_limit+40):
        fine=622

    elif speed>=(speed_limit+40):
        fine=1245

    return fine


def main():
    bank_balance=int(input('Enter your bank balance:$ '))
    fine=determine_fine()
    bank_balance-=fine
    print('Fine payable is :$', fine )
    print('The bank balance is: ', bank_balance)


main()
