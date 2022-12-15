import ordered_linked_list as lkl
import unittest as uni
import coureur as cour
import temps as tmp
import resultat as res


class Linked_list_test(uni.TestCase):
    def setUp(self) -> None:
        self.list = lkl.OrderLinkedList()
        t1 = tmp.Temps()
        t2 = tmp.Temps()
        t3 = tmp.Temps()
        t1.add_secondes(1000)
        t2.add_secondes(100)
        t3.add_secondes(2000)
        self.list.add(res.Resultat(cour.Coureur("Jamy", 25), t1))
        self.list.add(res.Resultat(cour.Coureur("Roger", 24), t2))
        self.list.add(res.Resultat(cour.Coureur("Patrick", 22), t3))

    def test_str(self):
        self.assertEqual(self.list.first().value(), res.Resultat('c',tmp.Temps(00,1,40)))
        self.assertEqual(self.list.first().next().value(), res.Resultat('c',tmp.Temps(00,16,40)))
        self.assertEqual(self.list.first().next().next().value(), res.Resultat('c',tmp.Temps(00,33,20)))

