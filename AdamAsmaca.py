import random

alphabet1 = ["a","b","c","d","e","f","g","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
alphabet2 = ["a","b","c","d","e","f","g","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
alphabet3 = ["a","b","c","d","e","f","g","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
alphabet4 = ["a","b","c","d","e","f","g","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
alphabet5 = ["a","b","c","d","e","f","g","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
alphabet6 = ["a","b","c","d","e","f","g","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
alphabet7 = ["a","b","c","d","e","f","g","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
alphabet8 = ["a","b","c","d","e","f","g","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
alphabet9 = ["a","b","c","d","e","f","g","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
alphabet10 = ["a","b","c","d","e","f","g","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]

a = "_"
ab = 3
abc = 10

Name = input("İsminizi alayım efendim : ")
print("Merhaba sayın", Name, "hadi küçük bir oyun oynayalım!")
    

theword1 = ((random.choice(alphabet1)) + (random.choice(alphabet2)) + (random.choice(alphabet3)) + (random.choice(alphabet4)) + (random.choice(alphabet5)) + (random.choice(alphabet6)) + (random.choice(alphabet7)) + (random.choice(alphabet8)) + (random.choice(alphabet9)) + (random.choice(alphabet10)))
theword2 = ((random.choice(alphabet1)) + (random.choice(alphabet2)) + (random.choice(alphabet3)) + (random.choice(alphabet4)) + (random.choice(alphabet5)) + (random.choice(alphabet6)) + (random.choice(alphabet7)) + (random.choice(alphabet8)) + (random.choice(alphabet9)))
theword3 = ((random.choice(alphabet1)) + (random.choice(alphabet2)) + (random.choice(alphabet3)) + (random.choice(alphabet4)) + (random.choice(alphabet5)) + (random.choice(alphabet6)) + (random.choice(alphabet7)) + (random.choice(alphabet8)))
theword4 = ((random.choice(alphabet1)) + (random.choice(alphabet2)) + (random.choice(alphabet3)) + (random.choice(alphabet4)) + (random.choice(alphabet5)) + (random.choice(alphabet6)) + (random.choice(alphabet7)))
theword5 = ((random.choice(alphabet1)) + (random.choice(alphabet2)) + (random.choice(alphabet3)) + (random.choice(alphabet4)) + (random.choice(alphabet5)) + (random.choice(alphabet6)))
theword6 = ((random.choice(alphabet1)) + (random.choice(alphabet2)) + (random.choice(alphabet3)) + (random.choice(alphabet4)) + (random.choice(alphabet5)))


wordlist = [theword1,theword2,theword3,theword4,theword5,theword6]

ŞansArttır = input("Oyununuzun kolay olması için biraz şans ister miydiniz? (Y/N)")
if ŞansArttır == "Y":
    wordlist.append(theword6)

GameWord = random.choice(wordlist)
print(wordlist)
print(GameWord)

##----------------------------------------------------------------------------------------------------------------------

##if GameWord == theword1:
  ##  list1 = [a,a,a,a,a,a,a,a,a,a]
    ##print(list1)
    
##elif GameWord == theword2:
  ##  list2 = [a,a,a,a,a,a,a,a,a] 
    ##print(list2)
    
##elif GameWord == theword3:
  ##  list3 = [a,a,a,a,a,a,a,a]
    ##print(list3)  
    
##elif GameWord == theword4:
  ##  list4 = [a,a,a,a,a,a,a]
    ##print(list4)
    
##elif GameWord == theword5:
  ##  list5 = [a,a,a,a,a,a]
    ##print(list5)
    
##elif GameWord == theword6:
  ##  list6 = [a,a,a,a,a]
    ##print(list6)    
    
##else:
  ##  print("Ooops :/ Sanırım bir şeyler ters gitti. Bu durumu geliştiriciye raporlamaya ne dersin?")
    
RealGameWord = len(GameWord)    

Kelime = input("Kelime tahmininiz var mı: (Y/N)")

Başla = True
while Başla:
    if Kelime == "Y":
        print("Kelime girmek için" , ab , "kadar hakkınız kaldı!")
        KelimeGiriş = input("Kelimenizi alayım efendim: ")
        if KelimeGiriş != (GameWord):
            ab = (ab - 1)
            print("Yanlış giriş yaptınız!" , ab , "kadar hakkınız kaldı!")
            dene = input("Tekrar denemek istiyor musunuz (Y/N): ")
            if dene == "N":
                Başla = False
        if KelimeGiriş == (GameWord):
            print("TEBRİKLER OYUNU KAZANDINIZ!")
            Başla = False
            
        
Giriş = input("Harfinizi Alayım Efendim: ")
if RealGameWord == 5:
    if Giriş == RealGameWord[0]:
        print(Giriş, "_", "_", "_", "_")
        if Giriş == RealGameWord[1]:
            print(Giriş, Giriş, "_", "_", "_")
            if Giriş == RealGameWord[2]:
                print(Giriş, Giriş, Giriş, "_", "_")
                if Giriş == RealGameWord[3]:
                    print(Giriş, Giriş, Giriş, Giriş, "_")
                    if Giriş == RealGameWord[4]:
                        print("_", "_", "_", "_", Giriş)
        
    if Giriş == RealGameWord[1]:
        print("_", Giriş, "_", "_", "_")
        
    if Giriş == RealGameWord[2]:
        print("_", "_", Giriş, "_", "_")
        
    if Giriş == RealGameWord[3]:
        print("_", "_", "_", Giriş, "_") 
        
    if Giriş == RealGameWord[4]:
        print("_", "_", "_", "_", Giriş)        


        

    
    
    


Word = input("Çıkış için lütfen enter'e basınız!" )

print(RealGameWord)

