def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [f"Hello, my name is {name}." for name in names]

def assign_rooms(names):
    roomNum = len(names)
    assignments = []
    while roomNum > len(names):
        assignments.append(f'Hello, {names[roomNum - 1]}! You\'ll be assigned to room {roomNum}!')

    print(assignments)
    return assignments

def printer(names):
    return None
