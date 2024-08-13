import unittest
from teste1 import sobrenomeNaOrdem

class NomeTest(unittest.TestCase):
    #testes para a função sobrenomeNaOrdem

    def test_sobrenomeNaOrdem(self):
        #Nomes como Joao Madureira Silva funcionam?

        nomeCompleto = sobrenomeNaOrdem("load", "Madureira", "Silva") 
        self.assertEqual(nomeCompleto, "Joao Silva Madureira")

unittest.main(argv=[''], exit=False)