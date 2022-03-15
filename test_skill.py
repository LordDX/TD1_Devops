import unittest
import Skill


class TestSkills(unittest.TestCase):

    def testLvl(self):
        skill = Skill("test")
        with self.assertRaises(Exception):
            skill.setLvl("o")

    def testType(self):
        skill = Skill("test")
        with self.assertRaises(Exception):
            skill.setType("o")
