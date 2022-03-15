import Classe
import unittest


class TestClasse(unittest.TestCase):

    def testLvl(self):
        classe = Classe("test")
        classe.setFailing("Frc")
        with self.assertRaises(Exception):
            classe.setAsset("Frc")
