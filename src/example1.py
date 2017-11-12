#!/usr/bin/env python3
# Testando modulos ppm matrixImage
# Nota de desenvolvimento
# Corrigir modulo matrixImage. Funcionamento
# diferente do uso de map e funcao lambda
# para criacao de matrix em
# matrixImage -> MatrixImRGB e MatrixImage.Matrix
#  Verificar doc Python3 sobre interadores e geradores
# e funcoes map.
# My code from github in Gist
m, n = 3 , 3
# Create matrix
# B = [ [ 0 for i in range(m)] for j in range(n) ]
A = [  [  1 if i==j else 0  for i in range(m)] for j in range(n)]
# Output: >>> [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print('\n',A[0],'\n',A[1],'\n',A[2],'\n')
# 
import matrixImage
matrix = lambda m,n: [ [ 0 for j in range(n)] for i in range(m) ]

img = matrix(10,5)
print(img)

