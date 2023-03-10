places=[]
place=input('Place: ')
while place!="":
    places.append(place)
    place=input('Place: ')
if len(places)==0:
    print('I went nowhere :(')
else:
    longest_place_name=places[0]
    print('On my holiday, I went to: ')
    for place in places:
        place=place.title()
        print(place)
        if len(place)>len(longest_place_name):
            longest_place_name=place
    print('The place with longest name was: ', longest_place_name)
