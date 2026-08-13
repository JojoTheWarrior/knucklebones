from itertools import product, combinations_with_replacement

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

class Column:
    columns = [list(state) for state in product([-1] + list(range(1, 7)), repeat=6) if check_valid(list(state))]
    rev_columns = {tuple(column) : i for i, column in enumerate(columns)} # note that lists are unhashable in python

    print(rev_columns[(-1, -1, 1, 2, 3, 4)])

# says C = 3067
valid_counter = 0
for state in product([-1, 1, 2, 3, 4, 5, 6], repeat=6):
    if check_valid(list(state)):
        valid_counter += 1

print(valid_counter)
