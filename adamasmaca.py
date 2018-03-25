import random,time,re,os,sys,time
pics =[ r"""
   +---+
   |   |
       |
       |
       |
       |
=========""",r"""
   +---+
   |   |
   O   |
       |
       |
       |
=========""",r"""
   +---+
   |   |
   O   |
   |   |
       |
       |
=========""",r"""
   +---+
   |   |
   O   |
  /|   |
       |
       |
=========""",r"""
   +---+
   |   |
   O   |
  /|\  |
       |
       |
=========""",r"""
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
========="""]
kelimeler={
"İşletim Sistemleri":[
"KALI LINUX","UBUNTU","WINDOWS","BACKTRACK","MAC OS"
],
"Yazılım Dilleri":[
"JAVA","PYTHON","C","RUBY","SWIFT","PERL","ASSEMBLY"
],
"Sayı Sistemleri":[
"HEXADEMICAL","BINARY","DEMICAL"
],
"Filmler":[
"ESARETIN BEDELI","YÜZÜKLERIN EFENDISI","KARA ŞÖVALYE","BABA","BAŞLANGIÇ","DÖVÜŞ KULÜBÜ","STAR WARS","HARRY POTTER","X MEN","HIZLI VE ÖFKELI","BUZ DEVRI"
],
"Çizgi Roman Karakterleri":[
"SUPERMAN","HULK","DEADPOOL","SPIDER MAN","FLASH","KAPTAN AMERIKA","KAPTAN MARVEL","JOKER","BATMAN","AQUAMAN"
],
"Hayvanlar":[
"KOPEK","KEDI","KELEBEK","KERTENKELE","FIL","DINAZOR","AYI","FARE","DENIZ ANASI"
],
"Şehirler":[
"ISTANBUL","ISPARTA","ANKARA","KILIS","SIIRT","LONDRA","PARIS","SIDNEY","BAĞDAT","TOKYO","PEKIN","AMSTERDAM","IZMIR","ŞIRNAK"
],
"Futbolcular":[
"CRISTIANO RONALDO","LIONEL MESSI","SABRI SARIOĞLU","OZAN TUFAN","MEHMET TOPAL","NEYMAR","WELBECK"
],
"Markalar":[
"ADIDAS","NIKE","LACOSTE","PUMA","POLARIS","KINETIX","DE FACTO","MC DONALDS","BURGER KING","APPLE",
"SAMSUNG","COCA COLA","YAHOO","CHEVROLET",
"UNILEVER","STARBUCKS","YOUTUBE","GOOGLE"
]}
class Oyuncu(object):
	@classmethod
	def isim_al(cls):
		cls.ekranı_temizle()
		return input("Adınızı giriniz:\n")
	def hoşgeldin(self):
		self.ekranı_temizle()
		time.sleep(0.5)
		print("{}, adam asmaca oyununa hoşgeldin".format(self.isim.title()))
		print("1","sesli hakkın var\nKelimeyi tahmin etmek istediğinde harf bölümüne 'tahmin' yaz\nYenilemek istediğinde ise 'yenile' yaz")
		time.sleep(1)
		input("Başla?")
	def __init__(self,isim):
		self.sesli_hakkı=True
		self.kazandı=None
		self.haklar = []
		self.tahminler = []
		self.puan=0
		self.doğru_harfler= []
		self.bitti=False
		self.tüm_harfler = frozenset("abcçdefgğhıijklmnoöprsştuüvyzxwq" + "abcçdefgğhıijklmnoöprsştuüvyzxwq".upper())
		self.sesli_harfler= frozenset("aeıioöuü" + "aeıioöuü".upper())
		self.isim=isim
		self.ekranı_temizle()
		self.hoşgeldin()
		self.başarı_tablosu = {0:"Bu Ne Lan",1:"Vasat",2:"Eh İşte",3:"İyi",4:"Harika",5:"Mükemmel",6:"Efsane"}
		self.tahmin_tablosu = {0:"Tek Attı",1:"Efsanesin",2:"Gayet İyi",3:"Fena Değil",4:"Eh Neyse İyi Yani",5:"Fazla",6:"Çok Çok Fazla"}
		self.devam_durumu=True
		self.rastgele_kelime_bul()
		self.cizgili_kelime()
		self.devam_durumu = True
		self.oyun()
	def rastgele_kelime_bul(self):
		_anahtar=random.choice(list(kelimeler.keys()))
		_numara = random.randrange(0, len(kelimeler[_anahtar]))
		self.gizli_kelime = kelimeler[_anahtar][_numara]
		self.gizli_anahtar = _anahtar
		return self.gizli_kelime
		return self.gizli_anahtar
	def cizgili_kelime(self):
		self.çizgili_kelime = re.compile("[ABCÇDEFGĞHIIJKLMNOÖPRSŞTUÜVYZXWQ]",re.I).sub("_",self.gizli_kelime.replace(" ","/"))
		return self.çizgili_kelime
	def son_yazı(self):
		time.sleep(0.4)
		self.ekranı_temizle()
		print("""Kelime '{}' idi. Oyunu kazandınız!
Kalan haklar:\t{}
{}
Yanlış Tahmin Sayısı:\t{}
{}""".format(self.gizli_kelime,
len(pics)-len(self.haklar),
self.başarı_tablosu[len(pics)-len(self.haklar)],
len(self.tahminler),
self.tahmin_tablosu[len(self.tahminler)]))
	def tahmin_yap(self):
		while self.devam_durumu:
			self.tahmin = tahmin = input("Harf?\n").upper()
			if len(tahmin) != 1 and tahmin.lower()!="tahmin" and tahmin.lower()!="yenile":
				print("Lütfen sadece bir karakter giriniz..")
			elif len(tahmin) != 1 and tahmin.lower()=="yenile":
				self.__init__(self.isim_al())
			elif len(tahmin) != 1 and tahmin.lower()=="tahmin":
				self.kelime_tahmin_et()
			elif tahmin in self.haklar:
				print("Bu harfi girmiştiniz..")
			elif tahmin not in self.tüm_harfler:
				print("Lütfen bir karakter giriniz..")
			elif tahmin in self.sesli_harfler and not self.sesli_hakkı:
				print("Sesli harf hakkınız yoktur..")
			elif tahmin in self.sesli_harfler and self.sesli_hakkı:
				self.sesli_hakkı=False
				return self.tahmin
			else:
				return self.tahmin
			time.sleep(0.4)
			self.oyun_arayuz()
	def tekrar(self):
		while True:
			devam_soru=input("Tekrar oynamak ister misiniz?(e/h)\n")
			if devam_soru.lower().startswith("e") or devam_soru.lower().startswith("h"):
				self.devam_durumu=devam_soru.startswith("e")
				if self.devam_durumu:
					self.__init__(self.isim_al())
				break
	def kelime_tahmin_et(self):
		kelime_tahmini=input("Kelimeyi tahmin et:\n")
		if str(kelime_tahmini.upper()) == str(self.gizli_kelime):
			self.son_yazı()
			self.bitti=True
			if self.bitti:
				self.tekrar()
		else:
			self.tahminler.append(kelime_tahmini)
		try:
			self.tahmin_tablosu[len(self.tahminler)]
		except KeyError:
			time.sleep(0.4)
			self.ekranı_temizle()
			print("Kelime {} idi".format(self.gizli_kelime))
			print("Kaybettiniz")
			self.bitti=True
			self.tekrar()
	def oyun_arayuz(self):
		self.ekranı_temizle()
		print("Kategori:\t{}".format(self.gizli_anahtar.title()))
		print("Kalan hak:\t{}".format(len(pics)-len(self.haklar)))
		if len(self.haklar)==len(pics):
			time.sleep(0.4)
			self.ekranı_temizle()
			print("Kelime {} idi".format(self.gizli_kelime))
			print("Kaybettiniz")
			self.bitti=True
			self.tekrar()
		else:
			print(pics[len(self.haklar)],"\n")
			if self.haklar:
				print("Kullanılan harfler:"),
				print(*self.haklar)
			for i in range(len(self.gizli_kelime)):
				if self.gizli_kelime[i] in self.doğru_harfler:
					self.çizgili_kelime = self.çizgili_kelime[:i] + self.gizli_kelime[i] + self.çizgili_kelime[i + 1:]
			print(*self.çizgili_kelime,sep=" ")
	def oyun(self):
		while self.devam_durumu:
			self.ekranı_temizle()
			self.oyun_arayuz()
			oyun_tahmin=self.tahmin_yap()
			try:
				if oyun_tahmin in self.gizli_kelime:
					self.doğru_harfler.append(oyun_tahmin)
					self.kazandı=True
					for i in range(len(self.gizli_kelime)):
						if self.gizli_kelime[i] not in self.doğru_harfler:
							self.kazandı=False
							break
					if self.kazandı:
						self.son_yazı()
						self.bitti=True
				else:
					self.haklar.append(oyun_tahmin)
				if self.bitti:
					while True:
						self.tekrar()
				if not self.devam_durumu:
					break
			except TypeError:
				self.bitti=True
	@staticmethod
	def ekranı_temizle():
		try:
			if os.name=="nt":
				return os.system("cls")
			elif os.name=="posix":
				return os.system("clear")
			else:
				return os.name("clear")
		except AttributeError:
			sys.exit()
Oyuncu.ekranı_temizle()
oyuncu=Oyuncu(Oyuncu.isim_al())
Oyuncu.ekranı_temizle()
