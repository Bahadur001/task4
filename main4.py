
class Sahmat():
    def __init__(self):
        print("oyunda 64 dama mövcuddur")
    def oyun(self):
        print("ilk ağlar baslayir")


class Sah(Sahmat):
    def __init__(self):
        print("Şah 'mat' olunsa oyun uduzulur")
    def oyun(self):
        print("Şah bir dama üfuqi və şaquli hərəkət edə bilir")

class Vezir(Sahmat):
    def __init__(self):
        print("Vezir en guclu daşdir oyunda")
    def oyun(self):
        print("Vezir ufuqi saquli dioqanal veziyyetde hereket ede bilir")

class Top(Sahmat):
    def __init__(self):
        print("Top-vezirden sonra oyundaki guclu das")
    def oyun(self):
        print("Top saquli ve ufuqi sekilde hereket ede bilir")
    def say(self):
        print("top iki dene olur  ")    

class Fil(Sahmat):
    def __init__(self):
        print("Fil-topdan sonra en guclu das")
    def oyun(self):
        print("Filler dioqanal veziyyetde hereket edir")
    def say(self):
        print("fil iki dene olur")    


class At(Sahmat):
    def __init__(self):
        print("At-Filden sonra en guclu das")
    def oyun(self):
        print("At 2 sekilde hereket edir")
    def say(self):
        print("at iki dene olur")    
    

class Piyada(Sahmat):
    def __init__(self):
        print("Piyadalar-oyundaki en zeif daslar")
    def oyun(self):
        print("piyadalar bir dama qabaga gedirler")
    def gerigetme(self):        
        print("piyadalar geri gede bilmir")


sahmat = Sahmat()
sah = Sah()
vezir = Vezir()
at = At()
fil = Fil()
top = Top()
piyada = Piyada()

def test_olunan(test_sahmat):
    test_sahmat.oyun()
test_olunan(sah)
test_olunan(vezir)
test_olunan(at)
test_olunan(top)
test_olunan(piyada)

def das_saylari(daslarin_saylari):
    daslarin_saylari.say()
das_saylari(top)
das_saylari(fil)
das_saylari(at)


def geriye_gede_bilmeme(geriye_no):
    geriye_no.gerigetme()

geriye_gede_bilmeme(piyada)




