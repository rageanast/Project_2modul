import unittest
import builtins
from In_and_out import *


class FunctionReactions(unittest.TestCase):
    def test_empty_reaction_combustion(self):
        self.assertEqual(combustion(''), '')

    def test_iron_sulfide_combustion(self):
        self.assertEqual(
            combustion('FeS + O2'),
            ('4FeS + 7O2-->2Fe2O3 + 4SO2',
             'горение'))

    def test_methan_combustion(self):
        self.assertEqual(
            combustion('CH4 + O2'),
            ('1CH4 + 2O2-->1CO2 + 2H2O',
             'горение'))

    def test_KOH_HCl_neutralization(self):
        self.assertEqual(neutralization('KOH + HCl'),
                         ('1KOH + 1HCl-->1KCl + 1H2O', 'обмен'))

    def test_empty_reaction_neutralization(self):
        self.assertEqual(neutralization(''), '')

    def test_empty_reaction_substitution(self):
        self.assertEqual(substitution(''), '')

    def test_K_H2SO4_substitution(self):
        self.assertEqual(
            substitution('K + H2SO4'),
            ('2K + 1H2SO4-->1K2SO4 + 1H2',
             'замещение'))

    def test_Ba_KCl_substitution(self):
        self.assertEqual(substitution('Ba + KCl'), '')

    def test_Cl_KI_substitution(self):
        self.assertEqual(
            substitution('KI + Cl2'),
            ('2KI + 1Cl2-->2KCl + 1I2',
             'замещение'))

    def test_empty_reaction_compound(self):
        self.assertEqual(compound(''), '')

    def test_C_H_compound(self):
        self.assertEqual(compound('C + H2'), ('1C + 2H2-->1CH4', 'соединение'))

    def test_Li_H2O_compounnd(self):
        self.assertEqual(
            compound('Li + H2O'),
            ('2Li + 2H2O-->2Li(OH)1 + 1H2',
             'соединение'))

    def test_Al2O3_H2O_compound(self):
        self.assertEqual(compound('Al2O3+H2O'), '')

    def test_BaSO4_KCl_exchange(self):
        self.assertEqual(exchange('BaSO4 + KCl'), '')

    def test_AgNO3_BaCl2_exchange(self):
        self.assertEqual(
            exchange('AgNO3 + BaCl2'),
            ('2AgNO3 + 1BaCl2-->2AgCl + 1Ba(NO3)2',
             'обмен'))

    def test_Na2SO4_hydrolisys(self):
        self.assertEqual(hydrolisys('Na2SO4 + H2O'), '')

    def test_KNO2_hydrolisys(self):
        self.assertEqual(
            hydrolisys('KNO2 + H2O'),
            ('1KNO2 + 1H2O-->1KOH + 1HNO2',
             'гидролиз'))

    def test_balance_equation_fault(self):
        self.assertEqual(balance_equation('KOH'), 'Балансировка не удалась')

    def test_balance_equation_KOH_H2SO4(self):
        self.assertEqual(
            balance_equation('KOH + H2SO4-->K2SO4 + H2O'),
            '2KOH + 1H2SO4-->1K2SO4 + 2H2O')

    def test_devision_into_parts_empty(self):
        self.assertEqual(devision_into_parts(''), [''])

    def test_devision_into_parts_K_H2O_1(self):
        self.assertEqual(devision_into_parts('K + H2O'), ['K', 'H2O'])

    def test_devision_into_parts_K_H2O_2(self):
        self.assertEqual(devision_into_parts('K+ H2O'), ['K', 'H2O'])

    def test_devision_into_elements_empty(self):
        self.assertEqual(devision_into_elements(''), [])

    def test_devision_into_elements_H2SO4(self):
        self.assertEqual(devision_into_elements('H2SO4'), ['H', 'S', 'O'])

    def test_devision_into_numbers_empty(self):
        self.assertEqual(devision_into_numbers(''), [])

    def test_devision_into_numbers_H2SiO3(self):
        self.assertEqual(devision_into_numbers('H2SiO3'), ['2', '3'])

    def test_release_of_acid_redisue_fault(self):
        self.assertEqual(release_of_acid_residue('KOH'), 'Error')

    def test_release_of_acid_redisue_Li2SiO3(self):
        self.assertEqual(release_of_acid_residue('Li2SiO3'), 'SiO3')

    def test_release_of_metal_fault(self):
        self.assertEqual(release_of_metal('H2O'), 'Error')

    def test_release_of_metal_BaSiO3(self):
        self.assertEqual(release_of_metal('BaSiO3'), 'Ba')

    def test_count_result_fault(self):
        self.assertEqual(count_result(''), 'Реакция невозможна')

    def test_count_result(self):
        self.assertEqual(
            count_result('KOH + H2SO4'),
            "('2KOH + 1H2SO4-->1K2SO4 + 2H2O', 'обмен')")

    def test_balance_equation_fault(self):
        self.assertEqual(balance_equation(''), 'Балансировка не удалась')

    def test_balance_equation(self):
        self.assertEqual(balance_equation('K + I2-->KI'), ('2K + 1I2-->2KI'))


if __name__ == "__main__":
    unittest.main()
