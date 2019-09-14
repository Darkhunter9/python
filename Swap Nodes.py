def swap_nodes(a):
    result = []
    for i in range(len(a)//2):
        result.append(a[2*i+1])
        result.append(a[2*i])
    if len(a)%2:
        result.append(a[-1])
    return result


if __name__ == '__main__':
    print("Example:")
    print(list(swap_nodes([1, 2, 3, 4])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(swap_nodes([1, 2, 3, 4])) == [2, 1, 4, 3]
    assert list(swap_nodes([5, 5, 5, 5])) == [5, 5, 5, 5]
    assert list(swap_nodes([1, 2, 3])) == [2, 1, 3]
    assert list(swap_nodes([3])) == [3]
    assert list(swap_nodes(["hello", "world"])) == ["world", "hello"]
    print("Coding complete? Click 'Check' to earn cool rewards!")
