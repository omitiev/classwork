import unittest


def grouper(data, n):
    data = [iter(data)] * n
    return zip(*data)


class TestGrouper(unittest.TestCase):

    bad_params = (
        (range(10), None),
        (range(10), 'foo'),
        (range(10), {"foo": "bar"})
    )

    def test_grouper(self):
        actual_result = list(grouper(range(10), 2))
        expected_result = [(0, 1),
                           (2, 3),
                           (4, 5),
                           (6, 7),
                           (8, 9)]
        self.assertEqual(actual_result, expected_result)

    def test_grouper_group_count(self):
        group_count = 2
        actual_result = list(grouper(range(10), group_count))
        assert all(list(map(lambda x: len(x) == group_count, actual_result)))

    def test_grouper_fails_if_groups_invalid(self):
        with self.assertRaises(TypeError):
            for bad_param in self.bad_params:
                grouper(*bad_param)
