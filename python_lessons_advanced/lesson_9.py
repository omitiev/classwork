def grouper (data, n):
    data = [iter(data)] * n
    return zip(*data)


print(list(grouper(range(10), 2)))


def test_grouper():
    actual_result = list(grouper(range(10), 2))
    expected_result = [(0, 1),
                       (2, 3),
                       (4, 5),
                       (6, 7),
                       (8, 9)]
    assert actual_result == expected_result


def test_grouper_group_count():
    group_count = 2
    actual_result = list(grouper(range(10), group_count))
    assert all(list(map(lambda x: len(x) == group_count, actual_result)))


def test_grouper_fails():
    with AssertRaises(TypeError):
        grouper(range(10), None)

    with AssertRaises(TypeError):
        grouper(range(10), 'foo')

    with AssertRaises(TypeError):
        grouper(range(10), {"foo": "bar"})


class AssertRaises:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        assert exc_type
        assert issubclass(exc_type, self.exception)
        return True
        # assert self.exception == exc_type
        # return True


test_grouper()
test_grouper_group_count()
test_grouper_fails()
