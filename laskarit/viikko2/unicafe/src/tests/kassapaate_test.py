import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti
#from maksukortti_test import TestMaksukortti


class TestKassapaate(unittest.TestCase):
   def setUp(self):
      self.kassa = Kassapaate()
      self.kortti = Maksukortti(1000)
        
        
   def test_kassapaatteen_saldo_alussa_oikea(self):
      self.assertEqual(str(self.kassa), "Kassassa on rahaa 1000.00 euroa")
      
      
   def test_maukkaan_lounaan_osto_toteutuu_oikein_tarp_kat_rah(self): #TARPEEKSI KATEISTA RAHAA
      kateisen_palautus = self.kassa.syo_maukkaasti_kateisella(50000)
      self.assertEqual(str(self.kassa), "Kassassa on rahaa 1004.00 euroa")
      self.assertEqual(kateisen_palautus, 49600)
      self.assertEqual(self.kassa.maukkaat, 1)
      
      
   def test_maukkaan_lounaan_osto_toteutuu_oikein_ei_tarp_kat_rah(self): #EI TARPEEKSI KATEISTA RAHAA
      kateisen_palautus = self.kassa.syo_maukkaasti_kateisella(50)
      self.assertEqual(str(self.kassa), "Kassassa on rahaa 1000.00 euroa")
      self.assertEqual(kateisen_palautus, 50)
      self.assertEqual(self.kassa.maukkaat, 0)
      
   #enkö voi hyödyntää maksukortti_test-tiedoston luokan TestMaksukortin metodeja??
   def test_saldo_vahenee_kortilta_oikein_tarp_rah(self): 
      tulos = self.kortti.ota_rahaa(500)
      self.assertEqual(str(self.kortti), "Kortilla on rahaa 5.00 euroa")
      self.assertEqual(tulos, True)
      self.assertEqual(self.kassa.kassassa_rahaa, 100000)
      return True
   
   #enkö voi hyödyntää maksukortti_test-tiedoston luokan TestMaksukortin metodeja??
   def test_saldo_ei_muutu_jos_rahaa_ei_tarp_rah(self):
      tulos = self.kortti.ota_rahaa(2000)
      self.assertEqual(str(self.kortti),"Kortilla on rahaa 10.00 euroa")
      self.assertEqual(tulos, False)
      self.assertEqual(self.kassa.kassassa_rahaa, 100000)
      return False