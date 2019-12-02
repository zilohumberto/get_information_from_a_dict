from unittest import TestCase
from app.utils import Utils


class TestEndToEnd(TestCase):

    def test_get_dots(self):
        self.assertListEqual(
            Utils.get_dots("hola.mundo.word"),
            ['hola', 'mundo', 'word']
        )
        self.assertEqual(
            len(Utils.get_dots("hola.mundo.word")),
            3
        )
        self.assertListEqual(
            Utils.get_dots("hola.mundo.word[44]"),
            ['hola', 'mundo', 'word[44]']
        )
        self.assertListEqual(
            Utils.get_dots("hola[3].mundo.word[44]"),
            ['hola[3]', 'mundo', 'word[44]']
        )
        self.assertListEqual(
            Utils.get_dots("hola.word[44]"),
            ['hola', 'word[44]']
        )

    def test_get_array(self):
        self.assertListEqual(
            Utils.get_array("weare[3]"),
            ['[3]']
        )
        self.assertListEqual(
            Utils.get_array("[4]"),
            ['[4]']
        )
        self.assertListEqual(
            Utils.get_array("[4][0]"),
            ['[4]', '[0]']
        )
        self.assertListEqual(
            Utils.get_array("we.are.h.t[4][0]"),
            ['[4]', '[0]']
        )

    def test_get_index(self):
        self.assertEqual(
            Utils.get_index("[3]"), 3
        )
        self.assertEqual(
            Utils.get_index("[1]"), 1
        )
        self.assertEqual(
            Utils.get_index("[44]"), 44
        )
        self.assertEqual(
            Utils.get_index("[999]"), 999
        )

    def test_get_key(self):
        self.assertEqual(
            Utils.get_key("we_are[5]"),
            "we_are"
        )
        self.assertEqual(
            Utils.get_key("we_are[5][0]"),
            "we_are"
        )
        self.assertEqual(
            Utils.get_key("we_are"),
            "we_are"
        )

    def test_is_valid_iterable(self):
        self.assertTrue(
            Utils.is_valid_iterable(0, [3])
        )
        self.assertFalse(
            Utils.is_valid_iterable(1, [3])
        )
        self.assertFalse(
            Utils.is_valid_iterable(3, [3])
        )
        self.assertTrue(
            Utils.is_valid_iterable(2, [3, 4, 8])
        )
        self.assertFalse(
            Utils.is_valid_iterable(0, {0: "we"})
        )

    def test_is_valid_dict(self):
        self.assertTrue(Utils.is_valid_dict('we', dict(we=3)))
        self.assertTrue(Utils.is_valid_dict('at', dict(we=3, at="be")))
        self.assertFalse(Utils.is_valid_dict('at', []))
        self.assertFalse(Utils.is_valid_dict('be', dict(we=3, at="be")))
