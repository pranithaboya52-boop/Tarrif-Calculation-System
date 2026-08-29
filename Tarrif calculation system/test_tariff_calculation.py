import unittest
from tariff_calculation import TariffCalculator


class TestTariffCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = TariffCalculator()

    def test_100_units(self):
        energy, total = self.calculator.calculate_bill(100)

        self.assertEqual(energy, 200)
        self.assertEqual(total, 250)

    def test_200_units(self):
        energy, total = self.calculator.calculate_bill(200)

        self.assertEqual(energy, 500)
        self.assertEqual(total, 550)

    def test_300_units(self):
        energy, total = self.calculator.calculate_bill(300)

        self.assertEqual(energy, 1000)
        self.assertEqual(total, 1050)

    def test_600_units(self):
        energy, total = self.calculator.calculate_bill(600)

        self.assertEqual(energy, 2800)
        self.assertEqual(total, 2850)

    def test_negative_units(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate_bill(-10)


