#!/usr/bin/env python3

message = 'Movie selections are: 1. Harry Potter 2. Hobbit and LotR 3. Chronicles of NArnia 4. Indiana Jones'

# wrap connection in a float() to accept decimals as numbers
movie_select  = int(input("Pick a movie, 1 to 4?"))

# if input value was higher or equal to 25
if movie_select == 1:
    message = 'Harry Potter is about a bunch of kids who do what grownups can not do for themselves'
elif movie_select == 2:
    message = 'The Hobbit and LotR is about a bunch of short, fat people kicking ass and taking names'
elif movie_select == 3:
    message = 'Chronicles of Narnia is about a bunch of kids taking orders from a talking lion without the use of psychedelics.'
elif movie_select == 4:
    message = 'Indiana Jones is about a professor who moonlights as a bull whip yielding Nazi-killer and makes archeology look cool.'
else:
    message = 'Cant help you with that.'
print(message)

