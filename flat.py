class Room1:
    def get_room(self):
        print('room1')


class Room2:
    def get_room(self):
        print('room2')

    def get_room2(self):
        print('room2 for flat')


class Kitchen:
    def get_kitchen(self):
        print('kitchen')


class Flat(Kitchen, Room1, Room2):
    ...


f = Flat()
f.get_kitchen()
f.get_room()
f.get_room2()
print(isinstance(f,Flat))
print(isinstance(f,Room1))
print(isinstance(f,Room2))