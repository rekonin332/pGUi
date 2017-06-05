'''
Created on 2017年5月24日

@author: Todd
'''

from enum import Enum


class MapSite(object):
    def Enter(self):
        raise NotImplementedError('Abstract Base Class Method')
    
class Direction(Enum):
    North = 0
    East = 1
    South = 2
    West = 3
    

class Room(MapSite):
    def __init__(self, roomNo):
        self._sides = [MapSite] * 4
        self._roomNumber = int(roomNo)
        
    def Enter(self):
        print('    You have entered room :' + str(self._roomNumber))
    
    def SetSide(self, Direction, MapSite):
        self._sides[Direction] = MapSite
    
    def GetSide(self, Direction):
        return self._sides[Direction]
    
class Wall(MapSite):
    def Enter(self):
        print('    You just ran into a Wall...')
        
class Door(MapSite):
    def __init__(self,Room1=None, Room2=None):
        self._room1 = Room1
        self._room2 = Room2
        self._isOpen = False
    
    def OtherSideFrom(self, Room):
        print('\tDoor obj: This door is a side of Room:{}'.format(Room._roomNumber))
        if 1 == Room._roomNumber:
            other_room = self._room2
        else:
            other_room = self._room1
            
        return other_room
    
    def Enter(self):
        if self._isOpen: print('    **** You have pass through this door...')
        else: print('    ** This door needs to be opened before you can pass through it...')
        

class Maze():
    def __init__(self):
        self._rooms = {}
    
    def AddRoom(self, room):
        self._rooms[room._roomNumber] = room
    
    def RoomNo(self, n):
        return self._rooms[n]
    
class MazeBuilder():
    def __init__(self):
        pass
    
    def BuildMaze(self):
        pass
    
    def BuildRoom(self, n):
        pass
    def BuildDoor(self, r1, r2):
        pass
#     def BulidlWall(self):
#         pass

    def GetMaze(self):
        return None
    

class MazeGame():
    def CreateMaze(self, builder):
        builder.BuildMaze()
        
        builder.BuildRoom(1)
        builder.BuildRoom(2)
        
        builder.BuildDoor(1,2)
        
        return builder.GetMaze()
    
    def CreateComplexMaze(self, builder):
        builder.BuildRoom(1)
        # ...
        builder.BuildRoom(1001)
        return builder.GetMaze()
    
    
# interface definition
class Interface_StandardMazeBuilder(MazeBuilder):
    def __init__(self): pass
    def BuildMaze(self):
        pass

#implement
class StandardMazeBuilder(MazeBuilder):
    def __init__(self):
        self._currentMaze = None # Member to hold a Maze
        
    def BuildMaze(self):
        self._currentMaze = Maze()
        
    
    def BuildRoom(self, roomNumber):
        try: self._currentMaze.RoomNo(roomNumber)
        except:
            print('Room {} does not eixst - building this room.'.format(roomNumber))
            room = Room(roomNumber)            
            self._currentMaze.AddRoom(room)
            
            room.SetSide(Direction.East.value, Wall())
            room.SetSide(Direction.South.value, Wall())
            room.SetSide(Direction.North.value, Wall())
            room.SetSide(Direction.West.value, Wall())
            
            
        
    def BuildDoor(self, n1, n2):
        r1 = self._currentMaze.RoomNo(n1)
        r2 = self._currentMaze.RoomNo(n2)
        
        d = Door(r1, r2)
        
        r1.SetSide(self.CommonWall(r1, r2), d)
        r2.SetSide(self.CommonWall(r2, r1), d)
        
        print()
        
        for side in range(4):
            if 'Door' in str(r1._sides[side]):
                print('Room1: ', r1._sides[side], Direction(side))
            if 'Door' in str(r2._sides[side]):
                print('Room2: ', r2._sides[side], Direction(side))
                
        
    def GetMaze(self):
        return self._currentMaze
    
    def CommonWall(self, room1, room2):
        # layout: room1, room2 etc. from left (West) ot right (East)
        if room1._roomNumber < room2._roomNumber:
            return Direction.East.value
        else:
            return Direction.West.value
    
    
class Interface_CountingMazeBuilder(MazeBuilder):
    def __init__(self):
        self._doors
        self._rooms
    
    def BuildMaze(self):
        pass
    def BuildRoom(self, n):
        pass
    def BuildDoor(self, r1, r2):
        pass
    
    def AddWall(self, n, Direction):
        pass
    
    def GetCount(self):
        return tuple()
    

class CountingMazeBuilder(MazeBuilder):
    def __init__(self):
        self._doors = 0
        self._rooms = 0
    
    def BuildDoor(self, r1, r2):
        self._doors += 1
        
    def BuildRoom(self, n):
        self._rooms += 1
    
    def GetCount(self):
        return self._doors, self._rooms
    


if __name__ == '__main__':
    
    print('*' * 21)
    print('*** The Maze Game ***')    
    print('*' * 21)
    
    maze = Maze
    game = MazeGame()
    builder = StandardMazeBuilder()
    
    game.CreateMaze(builder)
    maze = builder.GetMaze()
    
    print('\n')
    print('*' * 21)
    print('*** The Maze Game ***')    
    print('*' * 21)
    
    game = MazeGame()
    builder = CountingMazeBuilder()
    
    game.CreateMaze(builder=builder)
#     door, room = builder._doors,builder._rooms
    door, room = builder.GetCount()
    print('door {}, room {}'.format(door, room))
        