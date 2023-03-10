def minutes_to_minandsec(time_in_sec):
    total_min=int(time_in_sec/60)
    total_sec=time_in_sec-(total_min*60)
    time=f'{total_min} minutes and {total_sec} seconds'
    return time


def main():
    for sec in range(0,3176,635):
        time=minutes_to_minandsec(sec)
        print(f'{sec} is {time}')
    favourite_time=int(input('Favourite duration in seconds: '))
    favourite=minutes_to_minandsec(favourite_time)
    print(f'You Love {favourite}')


main()
