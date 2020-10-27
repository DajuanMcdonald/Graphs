from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# directions: north south east west [string]
directions = list(['n', 's', 'e', 'w'])

# destinations: rooms [string]
# when we find one, check if already searched and check if already visited
# if already searched - check dictionary for paths explored/not-explored

# dictionary: algorithm to map possible paths
# rooms
possible_paths = dict()

# paths: [count, searched, exit]

# visit: Boolean
# visit of rooms
# visited = set()
# while visited:
#     pass

# search: return paths bfs()/dfs()
# def bfs(self, room):
#     # while in a room
#     while room:
#         # if room has greater than 2 exits
#             # iterate directions
#         # check if  is in cache of explored rooms
#         # if yes, iterate directions and add exit to 
#     pass

# 
#  

# iteration: for n in directions: walk()

# traverse: explore paths bft() dft()
def bft(self, start):
    

    pass

def bfs(self, current_room, exits):
    """ breath-first search algorithm  """
    
    # create an empty queue and add path to starting vertex
    que = [ [current_room.id] ]
    visited_rooms = set()

    # set up visited

    # fill traveral path
    while len(que) > 0:
        traversal_path = que.pop(0)

        current_room = traversal_path[- 1]

        #check for visited vertex
        if current_room.id not in visited_rooms:
            visited_rooms.add(player.current_room)

            # check if current vertex has no more exits
            if player.current_room.get_exits() == True:
                player.travel(exits)



    pass


for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
