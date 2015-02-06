# coding=utf8

# Esqueleto de código Python para uso no Dojo-SE
# Escrito por Wagner Luís de Araújo Menezes Macêdo <wagnerluis1982@gmail.com>.
# 
# Para executar os testes, chame o interpretador Python com esse arquivo como
# parâmetro. Ex: python <caminho_do_arquivo>

import unittest

def gera_espiral(linhas, colunas):
	matriz = [[]]	

	for i in xrange(0,colunas):
		matriz[0].append(i + 1)

	return matriz

class ProblemaParaResolverTest(unittest.TestCase):
	def test_simples(self):
		self.assertEqual([[1]], gera_espiral(1,1))
	def test_uma_linha(self):
		self.assertEqual([[1,2]], gera_espiral(1,2))		
	def test_uma_linha_n_colunas(self):
		self.assertEqual([[1,2,3,4,5]], gera_espiral(1,5))

if __name__ == '__main__':
	unittest.main()
