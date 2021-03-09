class Board:
    def __lt__(self, other):
        selfPriority = (self.get_functional_cost())
        otherPriority = (other.get_functional_cost())
        return selfPriority < otherPriority

    def get_current_state(self):
        return self.current_state

    def calculate_heuristic_cost(self):
        # calculate horizontal plus vertical distance - this will give the total heuristic cost, that is, Manhattan
        # distance.
        heuristic_cost = sum(abs(b % 3 - g % 3) + abs(b // 3 - g // 3) for b, g in
                             ((self.current_state.index(i), self.goal_state.index(i)) for i in range(1, 9)))
        return heuristic_cost

    def get_heuristic_cost(self):
        return int(self.heuristic_cost)

    def get_path_cost(self):
        return self.self_cost

    def get_functional_cost(self):
        return self.total_cost

    def get_parent(self):
        return self.parent_node

    def move_blank(self, parent_blank_pos):
        self.current_state[self.blank_pos], self.current_state[parent_blank_pos] = self.current_state[parent_blank_pos], self.current_state[self.blank_pos]

    def calculate_costs(self):
        self.heuristic_cost = self.calculate_heuristic_cost()
        self.total_cost = self.heuristic_cost + self.self_cost

    def __init__(self, current_state, goal_state, parent_node, blank_pos):
        self.current_state = current_state
        self.goal_state = goal_state
        self.parent_node = parent_node
        if parent_node is not None:
            self.parent_cost = parent_node.get_path_cost()
        else:
            self.parent_cost = -1
        self.self_cost = self.parent_cost + 1
        self.blank_pos = blank_pos

    def print_state(self):
        print(self.current_state)
        print("Blank_Pos",self.blank_pos)
        print("Heuristic cost:",self.heuristic_cost)
        print("Self Cost", self.self_cost)
        print("Total Cost:", self.total_cost)

    def check_goal(self):
        if self.current_state == self.goal_state:
            return True
        else:
            return False

    def generate_children(self):
        child_node_list = []
        if self.blank_pos % 3 != 0:
            left_move_child = Board(self.current_state[:], self.goal_state, self, self.blank_pos - 1)
            left_move_child.move_blank(self.blank_pos)
            left_move_child.calculate_costs()
            child_node_list.append(left_move_child)

        if self.blank_pos % 3 != 2:
            right_move_child = Board(self.current_state[:], self.goal_state, self, self.blank_pos + 1)
            right_move_child.move_blank(self.blank_pos)
            right_move_child.calculate_costs()
            child_node_list.append(right_move_child)

        if self.blank_pos > 2:
            up_move_child = Board(self.current_state[:], self.goal_state, self, self.blank_pos - 3)
            up_move_child.move_blank(self.blank_pos)
            up_move_child.calculate_costs()
            child_node_list.append(up_move_child)

        if self.blank_pos < 6:
            down_move_child = Board(self.current_state[:], self.goal_state, self, self.blank_pos + 3)
            down_move_child.move_blank(self.blank_pos)
            down_move_child.calculate_costs()
            child_node_list.append(down_move_child)

        return child_node_list

