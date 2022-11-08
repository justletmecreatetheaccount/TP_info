"""
Mission 7
========

Groupe: Vlad Doniga - Théo Daron
Local: BARB15

Comme a notre habitude, nous avons fait usage de la lib unittest.

Nous avons également créé un Mock de l'indexer permettant de tester le tout sans avoir besoin de fichier annexe.

"""

import unittest
import search

class MockIndexer(search.Indexer):
    def _readfile(self, filename):
        return ["Turmoil has engulfed the Galactic Republic because i am a chad tptp.", "Vlad is a giga chad"]

class Tests(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.indexer = MockIndexer()
    def test_get_word(self):
        result = self.indexer._get_words ( "Turmoil has engulfed the Galactic Republic." )
        self.assertEqual(result, ["turmoil", "has", "engulfed", "the", "galactic", "republic"])
    def test_create_index(self):
        u = self.indexer.create_index("")
        self.assertEqual(u["chad"], [1,2])
        self.assertEqual(u["has"], [1])
        self.assertEqual(u["vlad"], [2])
    def test_get_lines(self):
        self.indexer.create_index("")
        result = self.indexer.get_lines(["vlad"])
        self.assertEqual(result, [2])
        result = self.indexer.get_lines(["chad"])
        self.assertEqual(result, [1,2])
        result = self.indexer.get_lines(["has"])
        self.assertEqual(result, [1])
        



if __name__ == "__main__":
    unittest.main(verbosity=1)