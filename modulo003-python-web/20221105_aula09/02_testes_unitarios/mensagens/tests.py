from django.test import TestCase

# sempre iniciar o nome da classe de teste com Test....
class TestAleatorio(TestCase):

    def setUp(self) -> None:
        pass


    def tearDown(self) -> None:
        pass


    def setUpTestData(cls):
        pass

    def test_soma_de_1_mais_1_deve_ser_2(self):
        self.assertEqual(1 + 1, 2)

