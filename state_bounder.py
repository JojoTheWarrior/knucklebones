from itertools import product

# state is length 6, [0, 1, 2] is Top and [3, 4, 5] is Bottom, -1 means it's empty
def check_valid(state: list) -> bool:
    # check whether the state matches its sorted self, to avoid counting duplicates
    sorted_state = state.copy()
    sorted_state[0:3] = sorted(sorted_state[0:3])
    sorted_state[3:6] = sorted(sorted_state[3:6])

    if not sorted_state == state:
        return False

    # check each number appears in either top or bottom
    for i in range(1, 7):
        inTop, inBottom = False, False
        for j in range(3):
            inTop |= state[j] == i
            inBottom |= state[3+j] == i
        if inTop and inBottom:
            return False
    return True


valid_counter = 0
for state in product([-1, 1, 2, 3, 4, 5, 6], repeat=6):
    if check_valid(list(state)):
        valid_counter += 1

print(valid_counter)
