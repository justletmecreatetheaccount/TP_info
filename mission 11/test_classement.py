import classement as cls
import ordered_linked_list as lkl
import unittest as uni
import coureur as cour
import temps as tmp
import resultat as res
class Classement__test(uni.TestCase):
    def setUp(self) -> None:
        self.classement = cls.Classement()
        self.classement.add(res.Resultat(cour.Coureur("Emile", 25), tmp.Temps(2000)))
        self.classement.add(res.Resultat(cour.Coureur("Roger", 25), tmp.Temps(1000)))
        self.classement.add(res.Resultat(cour.Coureur("Vlad", 25), tmp.Temps(4000)))
        self.classement.add(res.Resultat(cour.Coureur("Theo", 25), tmp.Temps(3000)))
    def test_str(self):
        self.assertEqual(self.classement.__str__(),'  1 > Roger      : 1000:00:00\n  2 > Emile      : 2000:00:00\n  3 > Theo       : 3000:00:00\n  4 > Vlad       : 4000:00:00\n','test 1')
    def test_get(self):
        self.assertEqual(self.classement.get(cour.Coureur("Vlad",25)).__str__(),'Vlad       : 4000:00:00','test 2')
    def test_get_pos(self):
        self.assertEqual(self.classement.get_position(cour.Coureur("Vlad", 25)),4,'test 3')