'''
Created on 2017年5月24日

@author: Todd
'''

from enum import Enum
from copy import deepcopy
from MazeAbstractFactoryPattern import MazeFactory

class MapSite(object):
    def Enter(self):
        raise NotImplementedError('Abstract Base Class Method')
    
class Direction(Enum):
    North = 0
    East = 1
    South = 2
    West = 3
#===============================================================
#    Prototype definition of Door
#===============================================================
        
class Door(MapSite):
    def __init__(self, other=None):        
        self._isOpen = False
        if other:
            self._room1 = other._room1
            self._room2 = other._room2
        else:
            self._room1 = None
            self._room2 = None
            
    def Initialize(self, r1, r2):
        self._room1 = r1
        self._room2 = r2
        
    def Clone(self):
        return Door(self)
    
    
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
            

class Room(MapSite):
    def __init__(self, roomNo=0):
        self._sides = [MapSite] * 4
        self._roomNumber = int(roomNo)
        
    def Enter(self):
        print('    You have entered room :' + str(self._roomNumber))
    
    def SetSide(self, Direction, MapSite):
        self._sides[Direction] = MapSite
    
    def GetSide(self, Direction):
        return self._sides[Direction]
    
    def Clone(self):
        return deepcopy(self)
    
    def Initialize(self, roomNo):
        self._roomNumber = int(roomNo)    
    
class Wall(MapSite):
    def Enter(self):
        print('    You just ran into a Wall...')
        
    def Clone(self):
        return deepcopy(self)


class MazePrototypeFactory(MazeFactory):
    def __init__(self, m, w, r, d):
        #these variables hold class instances of Maze, Walls etc.
        self._prototypeMaze = m
        self._prototypeWall = w
        self._prototypeRoom = r
        self._prototypeDoor = d
        
        self.prototype_manager_registry = {} # store of created objects
        
    def register_prototype(self, key, prototype):
        self.prototype_manager_registry[key] = prototype
        
    def unregister_prototype(self, key):
        del self.prototype_manager_registry[key]
        
    def MakeWall(self):
        return self._prototypeWall.Clone() #call Clone() method on prototype
    
    def MakeDoor(self, r1, r2):
        door = self._prototypeDoor.Clone()
        door.Initialize(r1, r2)
        return door
    
    def MakeRoom(self, roomNumber):
        room = self._prototypeRoom.Clone()
        room.Initialize(roomNumber)
        return room
    
    
        
        
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
    
    

if __name__ == '__main__':
    
    print('*' * 21)
    print('*** The Maze Game ***')    
    print('*' * 21)
    
    maze = Maze
    game = MazeGame()
    

        