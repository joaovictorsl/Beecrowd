class CircularList():
    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        key = self.__make_key_valid(key)
        return self.values[key]

    def get_in_range_idx(self, idx):
        return self.__make_key_valid(idx)

    def __make_key_valid(self, key):
        is_positive = key >= 0
        is_out_of_range = key >= len(
            self.values) if is_positive else key < len(self.values) * (-1)
        if is_out_of_range:
            if is_positive:
                return self.__make_positive_valid(key)
            return self.__make_negative_valid(key)
        return key

    def __make_positive_valid(self, key):
        max_idx = len(self.values) - 1
        valid_key = key - max_idx - 1
        if valid_key >= len(self.values):
            return self.__make_positive_valid(valid_key)
        return valid_key

    def __make_negative_valid(self, key):
        max_idx = len(self.values) * (-1)
        valid_key = key - max_idx
        if valid_key < max_idx:
            return self.__make_negative_valid(valid_key)
        return valid_key

    def __setitem__(self, key, value):
        key = self.__make_key_valid(key)
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return self.__circular()

    def __circular(self):
        idx = 0
        while True:
            yield self.__getitem__(idx)
            idx += 1

    def __reversed__(self):
        return reversed(self.values)

    def append(self, value):
        self.values.append(value)

    def pop(self, idx):
        idx = self.__make_key_valid(idx)
        self.values.pop(idx)


if __name__ == '__main__':
    test = CircularList([1, 2, 3, 4, 5])
    i = 0
    for num in test:
        if i > 50:
            break
        print(num)
        i += 1
    # Positive idxs
    for idx, answ in zip(list(range(11)), [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]):
        assert test[idx] == answ
    # Negative idxs
    for idx, answ in zip(list(range(-1, -12, -1)), [5, 4, 3, 2, 1, 5, 4, 3, 2, 1, 5]):
        assert test[idx] == answ
    # SetItem idxs
    test[-6] = -1
    assert test.values == [1, 2, 3, 4, -1]
    test[-7] = -1
    assert test.values == [1, 2, 3, -1, -1]
    test[6] = -1
    assert test.values == [1, -1, 3, -1, -1]
    test[12] = -1
    assert test.values == [1, -1, -1, -1, -1]
    assert test.get_in_range_idx(12) == 2
    assert test.get_in_range_idx(11) == 1
    assert test.get_in_range_idx(10) == 0
    assert test.get_in_range_idx(5) == 0
