# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertNotEqual("fixme", items[0].name)

# All items have a SellIn value which denotes the number of days we have to sell the item
# All items have a Quality value which denotes how valuable the item is At the end of each day
# our system lowers both values for every item
# input: to new item: name, sell_in, quality

class EveryItemDecrements(unittest.TestCase):
    def test_name_f(self):
        items = [Item("milk", 5, 10)]
        gilded_rose = GildedRose(items)

        # make time pass one day
        gilded_rose.update_quality()

        # ssert the name is something else
        # must fail
        self.assertNotEqual("bif", items[0].name)

    def test_name_p(self):
        items = [Item("milk", 5, 10)]
        gilded_rose = GildedRose(items)

        # make time pass one day
        gilded_rose.update_quality()

        # ssert the name is the same
        # must pass
        self.assertEqual("milk", items[0].name)


    def test_sell_in(self):
        items = [Item("milk", 5, 10)]
        gilded_rose = GildedRose(items)

        # test what we set
        self.assertEqual(5, items[0].sell_in)

        # make time pass one day
        gilded_rose.update_quality()

        # assert the amount
        # must F
        self.assertEqual(4, items[0].sell_in)
        # assert the amount
        # must P
        self.assertNotEqual(5, items[0].sell_in)
        # assert the amount
        # must F
        self.assertNotEqual(6, items[0].sell_in)




if __name__ == '__main__':
    unittest.main()
