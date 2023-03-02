import sys, subprocess

class Hotel:
    def __init__(self, name, rooms, rating):
        self.name = name
        self.rooms = rooms
        self.rating = rating
        self.guests = {}
    
    def __str__(self) -> str:
        return f"{self.name} | {self.rating} star(s), {len(self.guests)} guest(s) staying."
    
    def check_in(self, guest, room_number):
        if room_number in self.guests:
            print("This room already is occupied.")
        elif room_number > self.rooms:
            print("Invalid room number. This room number doesn't exists.")
        else:
            self.guests[room_number] = guest
            print(f"{guest} has checked in to room {room_number}")
    
    def check_out(self, room_number):
        if room_number in self.guests:
            guest = self.guests.pop(room_number)
            print(f"{guest} has checked out of room {room_number}.")
        else:
            print("This room is not occupied.")
        
    def display_guests(self):
        if self.guests:
            for room_number, guest in self.guests.items():
                print(f"Room: {room_number}: {guest}")
        else:
            print("There are no guests.")
    
    def display_option(self):
        option = {
            1: 'Choose Hotel', 
            2: 'Check-in', 
            3: 'Check-out', 
            4: 'Display Guests',
            5: 'Clear Screen',
            6: 'Exit'}
        
        for key, value in option.items():
            print(key, ':', value)


createHotel = input("Do you want to create a Hotel? (Y/N): ")
if createHotel.lower() == 'n':
    exit()
else:
    name = input("Hotel name: ")
    rooms = input("Number of rooms: ")
    rating = input("Rating: ")
    hotel = Hotel(name, rooms, rating)

    print('\n\n')
    
    hotel.display_option()
    try:
        choose = int(input('>| Choose one option: '))
    except ValueError:
        print('\n!!! Please use number for option !!!')
    
    if choose == 1:

    

    