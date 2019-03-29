"""
#Dictionary
pins = {"Afandi":1234,"Gita":1111,"Rifky":2222}

#Menampilkan Key
pins.keys()

#menampilkan values
pins.values()

#menghapus dictionary
pins.pop()

#untuk inputan luar [variable] = [type](input())
masukkan = input("masukkan nama anda : ")
bilangan = int(input("masukkan bilangan : "))

#untuk mengecek ada atau tidaknya values
kode = 1234
kode in pins.values()

#persyaratan
if 1<5:
	print("Benar")
else:
	print("Salah")
"""

user_input = float(input("masukkan angka : "))
if user_input>100:
	print("Greater")
elif user_input==100:
	print("Equals")
else:
	print("Smaller")