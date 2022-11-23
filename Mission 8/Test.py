import unittest
import mission8

class TestingTime(unittest.TestCase):
    def test_init_over_h(self):
        with self.assertRaises(ValueError):
            mission8.Duree(25,0,0)
    def test_init_neg_m(self):
        with self.assertRaises(ValueError):
            mission8.Duree(0,-1,0)
    def test_init_neg_h(self):
        with self.assertRaises(ValueError):
            mission8.Duree(-1,0,0)
    def test_init_over_s(self):
        with self.assertRaises(ValueError):
            mission8.Duree(0,0,70)
    def test_init_over_m(self):
        with self.assertRaises(ValueError):
            mission8.Duree(0,60,0)
    def test_init_type(self):
        with self.assertRaises(TypeError):
            mission8.Duree('taylor', 'azefrgub', 'grzbc')
    def test_to_seconds(self):
       self.assertEqual(mission8.Duree(8,6,1).to_seconds(),29161)
    def test_apres_a(self):
        self.assertEqual(mission8.Duree.apres(mission8.Duree(8,0,0), mission8.Duree(7,0,0)), True)
    def test_apres_b(self):
        self.assertEqual(mission8.Duree.apres(mission8.Duree(7,0,0), mission8.Duree(8,0,0)), False)
    def test_apres_b(self):
        self.assertEqual(mission8.Duree.apres(mission8.Duree(8,0,0), mission8.Duree(8,0,0)), False)
    def test_ajouter(self):
        self.assertEqual(mission8.Duree.ajouter(mission8.Duree(4,14,7), mission8.Duree(7,9,13)).to_seconds(), mission8.Duree(11,23,20).to_seconds())
    def test_print(self):
        self.assertEqual(mission8.Duree(9,50,14).__str__(), "09::50::14")

class TestingSongs(unittest.TestCase):
    def test_print(self):
        self.assertEqual(mission8.chanson("I'll always be loving thou", "Vlad", mission8.Duree(24,59,59)).__str__(), "24::59::59 - Vlad - I'll always be loving thou")
    
class Testing_albums(unittest.TestCase):
    def test_add_raw_1(self):
        self.assertEqual(mission8.album.add(mission8.album(1), mission8.chanson("Me'n'you Ohhh", "Vlad", mission8.Duree(00,2,59))), True)
    def test_add_raw_2(self):
        a = mission8.album(2)
        while a.add(mission8.chanson("You'n'me", "Vlad", mission8.Duree(0,2,59))) == True:
            pass
        self.assertEqual(a.add(mission8.chanson("You'n'me", "Vlad", mission8.Duree(0,2,59))), False)
    def test_print(self):
        a_2 = mission8.album(3)
        a_2.add(mission8.chanson("Never gonna give you up", "Rick Astley", mission8.Duree(0, 3, 32)))
        self.assertEqual(a_2.__str__(), "Album n°3 - 1 chansons - 00::03::32\n\n01 - Rick Astley - Never gonna give you up - 00::03::32 \n\n")
        

unittest.main(verbosity=3)