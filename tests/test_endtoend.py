from unittest import TestCase
from solver import Solver


class TestEndToEnd(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_solver(self):
        self.assertListEqual(Solver('{"a": 3}', '["a"]').start(), [3])
        self.assertListEqual(
            Solver('{"a": [1, 2, 3]}', '["a[0]"]').start(),
            [1]
        )
        self.assertListEqual(
            Solver('["pedro", "random"]', '["[1]"]').start(),
            ['random']
        )
        self.assertListEqual(
            Solver('["pedro", "random"]', '["no_valid_key"]').start(),
            []
        )
        self.assertListEqual(
            Solver('["pedro", "random"]', '["[5]"]').start(),
            []
        )
        self.assertListEqual(
            Solver('{"pedro": 100, "random": 200}', '["[0]"]').start(),
            []
        )