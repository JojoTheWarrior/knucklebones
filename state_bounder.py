from itertools import product

# state is length 6, [0, 1, 2] is Top and [3, 4, 5] is Bottom, -1 means it's empty
def check_valid(state: list) -> bool:
    # check whether the state matches its sorted self, to avoid counting duplicates
    sorted_state = state.copy()
    sorted_state[0:3] = sorted(sorted_state[0:3])
    sorted_state[3:6] = sorted(sorted_state[3:6])

    print(f"state {state}\nsorted_state {sorted_state}")

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


# tests
check_valid([-1, 2, -1, 3, 2, 1])