import string
import random
import serial
import time
import _thread
import winsound
import os

temp = ""
port = "COM4"
speed = 9600
cent = 100
connect = serial.Serial(port, speed)

def arduino():
	beep_var = 600
	time.sleep(1)
	global secs
	
	count = 1
	while True:
		time_init = ""
		if secs >= 10:
			temp = []
			for item in str(secs):
				temp.append(item)
			temp = temp[0],".", temp[1]
		elif secs >2:
			temp = secs
			temp = "0.",temp
		else:
			temp = "1"

		for item in temp:
			time_init += str(item)
		time_init = float(time_init)
		beep_var = 600

		if secs > 6 and secs < 10:
			time_init -= 0.15
			beep_var = 200
		elif secs > 4:
			time_init -=0.2
			beep_var = 150
		elif secs > 1:
			time_init -=0.25
			beep_var = 100

		count += 1
		

		if temp == "1":
			while secs >= 1:
				time.sleep(0.05)
				opt = "1"
				connect.write(opt.encode())
				winsound.Beep(1500, beep_var)
				time.sleep(0.05)
				opt = "0"
				connect.write(opt.encode())
				winsound.Beep(1500, beep_var)
			opt = "1"
			connect.write(opt.encode())
			winsound.Beep(1500, 2000)
			time.sleep(3)

			quit()
		else:
			opt = "1"
			connect.write(opt.encode())
			winsound.Beep(1500, beep_var)
			if time_init < 5:
				time.sleep(0.05)
			else:
				time.sleep(0.2)
			opt = "0"
			connect.write(opt.encode())
		time.sleep(time_init)

def seconds():
	global secs
	global cent
	secs = 10
	cent_um = secs / 100

	while secs > 0:
		time.sleep(1)
		secs -= 1
		cent -= cent_um
		
	print ("BOOOOOM")
	print("Game over")

def quit():
	connect.close()
	os._exit(0)

def senha_gen(tam, type):
	temp = ""
	count = tam
	letras = string.ascii_uppercase
	temp_2 = ""
	if type == "num":
		temp_2 = random.sample(range(0,10),tam)
	elif type == None:
		temp = random.sample(letras, len(letras))
		temp += random.sample(range(0,10), 10)
		temp_2 = random.sample(temp, len(temp))
	else:
		temp_2 = random.sample(letras, len(letras))

	global senha
	senha = temp_2
	iniciar()

def iniciar_config():
	print('''
	Defina o modo de jogo:
	1. 4 Numeros (Baby)
	2. 6 Numeros (Toddler)
	3. 9 Numeros (Gradeschooler)
	4. 5 letters (Teen)
	5. 10 letters (Adult)
	6. 15 letters (Badass)
	7. 26 letters (no way.)
	8. 36 All letters and numbers (Are you fucking crazy!)''')
	game_mode = input()
	if int(game_mode) > 0 and int(game_mode) < 4:
		if game_mode == "1":
			senha_gen(4, "num")
		if game_mode == "2":
			senha_gen(6, "num")	
		if game_mode == "3":
			senha_gen(9, "num")		

	elif int(game_mode) > 3 and int(game_mode) < 9:
		if game_mode == "4":
			senha_gen(5, "letters")
		if game_mode == "5":
			senha_gen(10, "letters")
		if game_mode == "6":
			senha_gen(15, "letters")
		if game_mode == "7":
			senha_gen(26, "letters")
		if game_mode == "8":
			senha_gen(36, None)

def iniciar():
	_thread.start_new_thread(seconds,())
	_thread.start_new_thread(arduino,())
	temp = ""
	global senha
	for item in senha:
		temp += str(item)
	senha = temp
	temp = ""

	senha_solut = []
	print("\n \n \n \n \n")
	print("Digite a senha correta para desarmar a bomba")
	print ("A senha possui",len(senha),"digitos")
	print("")
	for item in senha:
		senha_solut += "_"

	while True:
		count = 0
		temp = ""
		for item in senha_solut:
			temp += item
		print(senha_solut)
		print("Digite a senha:")
		senha_correta = str(input())
		if senha_correta == "/quit":
			quit()

		if senha_correta == senha:
			print("Bomba desarmada")
			quit()
		for item in senha_correta:
			if item == senha[count]:
				senha_solut[count] = item

			elif item in senha:
				senha_solut[count] = "? "

			else: 
				senha_solut[count] = "_ "
			count +=1
		

def ajuda():
	print('''
Instruções:

	Uma senha sera gerada com o numero X de caracteres.
	Voce deve digitar uma senha que você acredita ser a correta.
	Os numeros não se repetem.
	A senha que você digitar deve possuir o mesmo numero de caracteres
que a senha gerada.
	
Simbolos:

	_ = Numero não decifrado
	? = Numero correro, porem no local errado

		''')
while True:
	print ('Digite "/iniciar" para começar')
	print('Digite "/ajuda" para aprender a jogar')
	print('Digite "/quit" para sair')

	start = input()
	if start == "/iniciar":
		iniciar_config()
	elif start == "/ajuda":
		ajuda()
	elif start == "/quit":
		quit()




