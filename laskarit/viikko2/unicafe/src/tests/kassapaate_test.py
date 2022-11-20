import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti
#from maksukortti_test import TestMaksukortti


class TestKassapaate(unittest.TestCase):
   def setUp(self):
      self.kassa = Kassapaate()
      self.kortti = Maksukortti(1000)
        
      #Luodun kassapäätteen rahamäärä ja myytyjen lounaiden määrä on oikea
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
   
   
   def test_edullisen_lounaan_osto_toteutuu_oikein_tarp_kat_rah(self): #TARPEEKSI KATEISTA RAHAA
      kateisen_palautus = self.kassa.syo_edullisesti_kateisella(50000)
      self.assertEqual(str(self.kassa), "Kassassa on rahaa 1002.40 euroa")
      self.assertEqual(kateisen_palautus, 49760)
      self.assertEqual(self.kassa.edulliset, 1)
      
      
   def test_edullisen_lounaan_osto_toteutuu_oikein_ei_tarp_kat_rah(self): #EI TARPEEKSI KATEISTA RAHAA
      kateisen_palautus = self.kassa.syo_edullisesti_kateisella(50)
      self.assertEqual(str(self.kassa), "Kassassa on rahaa 1000.00 euroa")
      self.assertEqual(kateisen_palautus, 50)
      self.assertEqual(self.kassa.edulliset, 0)
   
   
   #enkö voi hyödyntää maksukortti_test-tiedoston luokan TestMaksukortin metodeja??
   def test_maukkaan_lounaan_osto_toteutuu_oikein_tarp_rah_kort(self): 
      tulos = self.kortti.ota_rahaa(400)
      self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")
      if tulos == True:
         tulos = self.kassa.syo_maukkaasti_kortilla(self.kortti)
         self.assertEqual(tulos, True)
         self.assertEqual(str(self.kassa), "Kassassa on rahaa 1000.00 euroa")
         self.assertEqual(self.kassa.maukkaat, 1)
         return True
   
   #enkö voi hyödyntää maksukortti_test-tiedoston luokan TestMaksukortin metodeja??
   def test_maukkaan_lounaan_osto_toteutuu_oikein__ei_tarp_rah_kort(self):
      kortti = Maksukortti(100)
      tulos = kortti.ota_rahaa(400)
      self.assertEqual(str(kortti),"Kortilla on rahaa 1.00 euroa")
      if tulos == False:
         tulos = self.kassa.syo_maukkaasti_kortilla(kortti)
         self.assertEqual(tulos, False)
         self.assertEqual(str(self.kassa), "Kassassa on rahaa 1000.00 euroa")
         self.assertEqual(self.kassa.maukkaat, 0)
         return False
   
   
   def test_edullisen_lounaan_osto_toteutuu_oikein_tarp_rah_kort(self):
      tulos = self.kortti.ota_rahaa(240)
      self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.60 euroa")
      if tulos == True:
         tulos = self.kassa.syo_edullisesti_kortilla(self.kortti)
         self.assertEqual(tulos, True)
         self.assertEqual(str(self.kassa), "Kassassa on rahaa 1000.00 euroa")
         self.assertEqual(self.kassa.edulliset, 1)
         return True
      
   
   def test_edullisen_lounaan_osto_toteutuu_oikein_ei_tarp_rah_kort(self):
      kortti = Maksukortti(100)
      tulos = kortti.ota_rahaa(400)
      self.assertEqual(str(kortti),"Kortilla on rahaa 1.00 euroa")
      if tulos == False:
         tulos = self.kassa.syo_edullisesti_kortilla(kortti)
         self.assertEqual(tulos, False)
         self.assertEqual(str(self.kassa), "Kassassa on rahaa 1000.00 euroa")
         self.assertEqual(self.kassa.edulliset, 0)
         return False
   
   def test_kortille_rahan_lataaminen_onnistuu(self):
      self.kassa.lataa_rahaa_kortille(self.kortti, 200)
      self.assertEqual(str(self.kortti), "Kortilla on rahaa 12.00 euroa")
      self.assertEqual(str(self.kassa), "Kassassa on rahaa 1002.00 euroa")
      
   def test_kortille_rahan_lataaminen_onnistuu_sum_neg(self):
      tulos = self.kassa.lataa_rahaa_kortille(self.kortti, -200)
      self.assertEqual(str(self.kortti), "Kortilla on rahaa 10.00 euroa")
      self.assertEqual(str(self.kassa), "Kassassa on rahaa 1000.00 euroa")
      self.assertEqual(tulos, False)