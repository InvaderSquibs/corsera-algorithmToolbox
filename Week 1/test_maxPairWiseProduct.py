from unittest import TestCase
from .maxPairWiseProduct import maxPairWiseProduct as pw


class TestMaxPairWise(TestCase):
    def test_find_max_pair_wise(self):
        expectOne = 6
        expectTwo = 25
        expectThree = 9000000000

        actualOne = pw.find_max_pair_wise([1, 2, 3, 2, 1])
        actualTwo = pw.find_max_pair_wise([4, 5, 3, 5, 2, 1])
        actualThree = pw.find_max_pair_wise([100000, 90000])

        self.assertEqual(expectOne, actualOne)
        self.assertEqual(expectTwo, actualTwo)
        self.assertEqual(expectThree, actualThree)

