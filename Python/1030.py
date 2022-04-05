import sys


def main():
    cases = int(input())
    for case in range(cases):
        people, step = [int(x) for x in input().split()]
        people_list = [x for x in range(1, people + 1)]

        idx = 0
        while len(people_list) != 1:
            list_length_before_pop = len(people_list)
            idx_to_eliminate = cicle_idx(idx, step, list_length_before_pop)
            people_list.pop(idx_to_eliminate)
            idx = idx_to_eliminate if idx_to_eliminate != \
                list_length_before_pop - 1 else 0
        print(f'Case {case + 1}: {people_list[0]}')


def cicle_idx(idx, step, list_size):
    idx_to_eliminate = idx + step - 1
    max_idx = list_size - 1
    if idx_to_eliminate > max_idx:
        steps_taken = list_size - idx
        return cicle_idx(0, step - steps_taken, list_size)
    return idx_to_eliminate


if sys.argv[-1] == 't':
    list_test_size = 5
    steps = list(range(1, 12))
    for step, answ in zip(steps, [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0]):
        assert cicle_idx(
            0, step, list_test_size) == answ, f'Problem on step: {step}, answer: {answ}'
    for step, answ in zip(steps, [4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]):
        assert cicle_idx(
            4, step, list_test_size) == answ, f'Problem on step: {step}, answer: {answ}'
else:
    main()
