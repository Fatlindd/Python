class Hotel:
    def __init__(self, name, rooms, rating):
        self.name = name
        self.rooms = rooms
        self.rating = rating
        self.guests = {}
    
    def __str__(self) -> str:
        return f"{self.name} | {self.rating} star(s), {len(self.guests)} guest(s) staying."