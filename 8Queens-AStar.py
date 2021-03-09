from Board import Board
from queue import PriorityQueue

def trace_to_source(goal_state):
    path_to_source = []
    path_to_source.append(goal_state)
    while goal_state.get_parent() is not None:
        path_to_source.append(goal_state.get_parent())
        goal_state = goal_state.get_parent()
    return path_to_source

explored_state = []
q = PriorityQueue()
current_state = [2,8,1,3,4,6,7,5,0]
goal_state = [3,2,1,8,0,4,7,5,6]
blank_pos = current_state.index(0)
obj = Board(current_state,goal_state,None,blank_pos)
obj.calculate_costs()
q.put(obj)
solution_found = False
path_to_source = []

while not q.empty():
    prev_h_cost = obj.get_heuristic_cost()
    obj = q.get()
    curr_h_cost = obj.get_heuristic_cost()
    if prev_h_cost < curr_h_cost:
        continue
    elif obj.get_current_state() not in explored_state:
        explored_state.append(obj.get_current_state())
    else:
        continue

    if not obj.check_goal():
        obj_children_list = obj.generate_children()
        [q.put(child) for child in obj_children_list]
    else:
        solution_found = True
        path_to_source = trace_to_source(obj)
        break

if not solution_found:
    print('Failure')
else:
    path_to_source.reverse()
    for nodes in path_to_source:
        nodes.print_state()
        print('---')
