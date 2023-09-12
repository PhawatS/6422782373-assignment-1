def initial_state():
    return (8, 0, 0)

def is_goal(state):
    a, b, _ = state
    return a == 4 and b == 4

def successors(state):
    a, b, c = state
    successors_list = []

 # Pour from A to B
    if a > 0 and b < 5:
        pour_amount = min(a, 5 - b)
        new_state = (a - pour_amount, b + pour_amount, c)
        cost = pour_amount
        successors_list.append((new_state, "Pour A to B", cost))

    # Pour from A to C
    if a > 0 and c < 3:
        pour_amount = min(a, 3 - c)
        new_state = (a - pour_amount, b, c + pour_amount)
        cost = pour_amount
        successors_list.append((new_state, "Pour A to C", cost))

    # Pour from B to A
    if b > 0 and a < 8:
        pour_amount = min(b, 8 - a)
        new_state = (a + pour_amount, b - pour_amount, c)
        cost = pour_amount
        successors_list.append((new_state, "Pour B to A", cost))

    # Pour from B to C
    if b > 0 and c < 3:
        pour_amount = min(b, 3 - c)
        new_state = (a, b - pour_amount, c + pour_amount)
        cost = pour_amount
        successors_list.append((new_state, "Pour B to C", cost))

    # Pour from C to A
    if c > 0 and a < 8:
        pour_amount = min(c, 8 - a)
        new_state = (a + pour_amount, b, c - pour_amount)
        cost = pour_amount
        successors_list.append((new_state, "Pour C to A", cost))

    # Pour from C to B
    if c > 0 and b < 5:
        pour_amount = min(c, 5 - b)
        new_state = (a, b + pour_amount, c - pour_amount)
        cost = pour_amount
        successors_list.append((new_state, "Pour C to B", cost))

    return successors_list

def print_solution(node):
    if node is None:
        print("No solutions found")
    else:
        path = []
        while node:
            state, _, action, _, _ = node
            path.append((state, action))
            node = node[1]
        path.reverse()
        for state, action in path:
            print(f"Action: {action}, State: {state}")