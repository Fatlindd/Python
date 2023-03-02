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