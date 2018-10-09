def checkio(numbers):
    last = numbers[-1]
    traces = [[numbers.pop(0)]]
    while not any(last in t for t in traces):
        i = 0
        new_traces = []
        while i < len(numbers):
            for t in traces:
                if sum(a != b for a, b in zip(str(t[-1]), str(numbers[i]))) == 1:
                    new_traces.append(t + [numbers.pop(i)])
                    break
            else:
                i += 1
        traces = new_traces
    return traces[-1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"