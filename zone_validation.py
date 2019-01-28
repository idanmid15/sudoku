
from board import empty_sign


def is_valid(zone):
    """
    A zone represents an area in which, in a correct solution, each digit out of 1-9 appears exactly once.
    A zone may be a row, a column or a 3x3 square.
    :param zone: a list of 9 digits or '-'
    :return: if the zone is valid or not
    """
    map_of_counts = {}
    for value in zone:
        map_of_counts[value] = map_of_counts[value] + 1 if value in map_of_counts else 1
    for key, value in map_of_counts.items():
        if key != empty_sign and value > 1:
            return False
    return True


if __name__ == '__main__':
    print(is_valid([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # t
    print(is_valid([1, empty_sign, empty_sign, 2, empty_sign, empty_sign, 7, empty_sign, 3]))  # t
    print(is_valid([1, empty_sign, 3, 2, empty_sign, empty_sign, 7, empty_sign, 3]))  # f
    print(is_valid([1, 2, 3, 4, empty_sign, 6, 7, 1, 1]))  # f
    print(is_valid([empty_sign for _ in range(9)]))  # t
