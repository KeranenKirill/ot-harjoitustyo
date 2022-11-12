import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)


    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
        
        
    def test_kortin_saldo_alussa_oikea(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")


    def test_rahan_ksavatus_oikein(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 15.00 euroa")
        
    
    def test_saldo_vahenee_oikein_rahaa_tarpeeksi(self):
        tulos = self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")
        self.assertEqual(tulos, True)
        
    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        tulos = self.maksukortti.ota_rahaa(2000)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 10.00 euroa")
        self.assertEqual(tulos, False)
