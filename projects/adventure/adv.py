from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
map_file = "maps/test_loop.txt"
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

# player.current_room.id
# player.current_room.get_exits()
# player.travel(direction)

# starting in room 0 of graph 
# graph[0]





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
visited_rooms = set()
# while visited:
#     pass

# search: return paths bfs()/dfs()
def depth_first_search(start_node, graph={}):
    if start_node is None or start_node not in graph:
        return "No start node found"

    path = traversal_path
    stack = [start_node]

    while len(stack) != 0:
        s = stack.pop()

        if s not in path:
            path.append(s)

        if s not in graph:
            continue


        for neighbor in graph[s]:
            print(neighbor)

    return " ".join(path)

# depth_first_search(0, map_file)
# def bfs(room_graph, start_node, path=traversal_path):
#    """ Using Queue to implement BFS """
#    queue = [start_node]
#    while queue:
#        vertex = queue.pop(0)
#        if vertex not in path:
#            path.append(vertex)
#            queue = room_graph[vertex]+queue
#            print(path)
           
#            return path

# bfs(room_graph, 0)
    #once we have at least one node enqueued and queue is not empty
    # we can visit nodes and enqueue their children
    # while len(queue) > 0:
    #     new_node = queue[0]

    #     for adjecent of new_node.neighbors:
    #         if adjecent 
    # if node not in discovered_nodes
        # add node to discovered_nodes 

# def dfs(room_graph, start_node, path=traversal_path):
#     stack = [start_node]
#     while stack:
#         vertex = stack.pop(0)
#         if not vertex in path:
#             path.append(vertex)
#             stack = stack+room_graph[vertex]
#             print(path)
#             return path

# dfs(room_graph, 0)

# iteration: for n in directions: walk()

# traverse: explore paths bft() dft()
def bft(): 
    pass

def dft():
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
        traversal_path.append(cmds[0])
        print(player.current_room.id)
        print(room_graph[player.current_room.id])
        print(traversal_path)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
