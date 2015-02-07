# coding=utf8

# Esqueleto de código Python para uso no Dojo-SE
# Escrito por Wagner Luís de Araújo Menezes Macêdo <wagnerluis1982@gmail.com>.
# 
# Para executar os testes, chame o interpretador Python com esse arquivo como
# parâmetro. Ex: python <caminho_do_arquivo>

import unittest

def gera_linha(inicial, qtd_colunas, incremento):
	vetor = []
	if incremento > 0:
		for i in range(inicial, qtd_colunas+1, incremento):
			vetor.append(i)
	else : 
		for i in range(inicial, 0, incremento):
			vetor.append(i)		
	return vetor

def inicia_matriz(linhas, colunas):
	matriz = [None]*linhas
	for i in range(0, len(matriz)):
		matriz[i] = [None]*colunas
	return matriz

def gera_espiral(linhas, colunas):
	matriz = [[]] #inicia_matriz(linhas, colunas)	 

	for i in range(0,colunas):
		matriz[0].append(i + 1)

	if linhas == 2:
		matriz.append([])
		for i in range(colunas*linhas, colunas, -1):
			matriz[1].append(i)	

	return matriz

class ProblemaParaResolverTest(unittest.TestCase):
	def test_simples(self):
		self.assertEqual([[1]], gera_espiral(1,1))
	def test_uma_linha(self):
		self.assertEqual([[1,2]], gera_espiral(1,2))		
	def test_uma_linha_n_colunas(self):
		self.assertEqual([[1,2,3,4,5]], gera_espiral(1,5))
	def test_uma_linha_n_colunas(self):
		self.assertEqual([[1,2,3,4,5],[10,9,8,7,6]], gera_espiral(2,5))
	def test_gera_uma_linha(self):
		self.assertEqual([1,2,3], gera_linha(1,3,1))
	def test_gera_uma_linha_contrario(self):
		self.assertEqual([3,2,1], gera_linha(3,3,-1))

if __name__ == '__main__':
	unittest.main()
