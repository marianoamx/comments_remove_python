#!/usr/bin/env python2
#! -*- coding: utf8 -*-

"""
borrar comentarios multilinea de html
"""

#from __future__ import unicode_literals
import re
import sys

def cargar_texto_from_archivo_print(ar1):
	arch1 = open(ar1, 'r')
	list1 = []
	accion = 'no procesar'
	for linea in arch1 :
		#linea = unicode( linea , 'utf-8' )
		list1.append(linea)
	arch1.close()
	todo_junto1 = ''.join(list1)
	#result = re.sub('<!--.*?-->', '', todo_junto1 , flags=re.DOTALL)
	#result = re.sub('<!--.*?-->', '', todo_junto1 , flags=re.S)
	# http://stackoverflow.com/questions/9235232/period-stops-multiline-regex-substitute-in-python
	# Note that re.sub() only accepts the flags argument in Python 2.7 or Python 3.1+, before that you will either need to compile the regex with the flag set or use something like [\s\S]*? instead of .*?
	result1 = re.sub('<!--[\s|\S]*?-->', '', todo_junto1)
	print result1
	
	ar2 = ar1
	
	arch2 = open(ar2, 'w')
	arch2.write(result1)
	arch2.close()

#if len(sys.argv) == 1 : print "error, se aborta programa" ; exit()
if len(sys.argv) == 1 : sys.exit('abortando programa, ingrese archivo a eliminar comentarios html\nuso: python %s archivo1.txt' % sys.argv[0] )
#elif len(sys.argv) > 2 : sys.exit('abortando programa, solo ingrese archivo a eliminar comentarios html\nuso: python %s archivo1.txt' % sys.argv[0] )

cargar_texto_from_archivo_print(sys.argv[1])
