from utils.CircularList import CircularList


def main():
    cases = int(input())
    for case in range(cases):
        people, step = [int(x) for x in input().split()]
        people_list = CircularList([x for x in range(1, people + 1)])

        idx = 0
        while len(people_list) != 1:
            idx_to_eliminate = idx + step - 1
            idx = people_list.get_in_range_idx(idx_to_eliminate)
            people_list.pop(idx_to_eliminate)
        print(f'Case {case + 1}: {people_list[0]}')


main()
