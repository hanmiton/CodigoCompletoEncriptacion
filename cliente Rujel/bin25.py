import sys
import math
import random
LAMBDA = 16 #security parameter
N = LAMBDA	
P = LAMBDA ** 2
Q = LAMBDA ** 5

def principal(m1,m2):
	boln1 = bin(m1)
	boln2 = bin(m2)
	boln1Encrypt = []
	boln2Encrypt = []
	sumEncrypt = []
	mulEnctypt = []
	res = []
	aux = []

	if(len(boln1) > len(boln2)):
		print len(boln1) - len(boln2)
		for i in range(0, len(boln1) - len(boln2)):
			aux.append(0)
		boln2 = aux + boln2
	else:
		print len(boln2) - len(boln1)
		for i in range(0, len(boln2) - len(boln1)):
			aux.append(0)
		boln1 = aux + boln1
	key = map(keygen,boln1)

	boln1Encrypt = map(encrypt,key,boln1)
	boln2Encrypt = map(encrypt,key,boln2)

	sumEncrypt = map(add,boln1Encrypt,boln2Encrypt)
	mulEnctypt = map(mult,boln1Encrypt, boln2Encrypt)
	
	resSuma = map (decrypt, key, sumEncrypt)
	strSuma = ''.join(str(e) for e in resSuma)
	decSuma = int(strSuma, 2)

	resMult = map (decrypt, key, mulEnctypt)
	strMult = ''.join(str(e) for e in resMult)
	decMult = int(strMult, 2)
	
	return sumEncrypt
		
def quot(z, p):
        # http://stackoverflow.com/questions/3950372/round-with-integer-division
        return (z + p // 2) // p
        
def mod(z, p):
        return z - quot(z,p) * p

def keygen(n):
	key = random.getrandbits(P)
	while(key % 2 == 0):
		key = random.getrandbits(P)
	return key

def encrypt(key, aBit):
	q = random.getrandbits(Q)
	m_a = 2 * random.getrandbits(N - 1)
	c = key * q + m_a + aBit
	return c

def decrypt(key, cipherText):
	return mod(cipherText, key) % 2

def add(cipherText1, cipherText2):
	return cipherText1 + cipherText2

def mult(cipherText1, cipherText2):
	return cipherText1 * cipherText2

def bin(numero):
	binario = ""
	listaN = []
	listaRn = []
	if (numero >0):
		while (numero >0):
			if(numero%2 ==0):
				listaN.append(0)
				binario="0"+binario
			else:
				listaN.append(1)
				binario = "1"+ binario
			numero = int (math.floor(numero/2))
	else:
		if (numero ==0):
			listaN.append(0)
			return listaN
		else:
			return " no se pudo convertir el numero. ingrese solo numeros positivos"	
	for i in reversed(listaN):
		listaRn.append(i)
	return listaRn

if __name__ == '__main__':
	principal(m1,m2)