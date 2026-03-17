######LISTAS#######
print("########################")
print("TRABAJO LISTAS Y TUPLAS EN PYTHON")
print("########################")
print("########################")
print("LISTAS")
print("########################")
print("########################")
print("EJEMPLO CON LISTAS CON STRINGS")
print("########################")

lista_colores =['Rojo', 'Verde','Amarillo', 'Azul','Morado','Negro']
print(lista_colores) #imprime toda la lista 
print(type(lista_colores)) #tipo => 'list'

print(lista_colores[2]) #imprime el dato almacenado en la posicion 2 recordar que se inicia con cero normalmente

print("lista size: " , len(lista_colores)) # tamano de la lista => numero de posiciones disponibles

print(lista_colores[0:2]) #Imprime el barrido de un [inicio:fin] sin incluir el fin
print(lista_colores[:2])  #

lista_colores.append('Blanco')  #Agrega elemento al final de la lista
print(lista_colores)

lista_colores.insert(3,'Negro') #Agrega elemento en la posicion x 
print(lista_colores)

lista_colores.extend(['Marron','Gris']) #Itera los elementos de cualquier iterable agragandolos al final de la lista
print(lista_colores)

print(lista_colores.index('Azul')) #Imprime la posicion en la que se encuentra el elemento

lista_colores.remove('Marron') #Elimina el elemento de la lista
print(lista_colores)

lista_colores.insert(8,'Marron')
print(lista_colores)

print(lista_colores.pop())  #Funcion pop() elimina y retorna el elemento de la lista (en caso de llevar argumento se elimina el elemento de esa posicion)
size = len(lista_colores)
print("size = ", size)
#print(lista_colores.pop(size)) #Error pop index out of range. Esto sucede porque size es el numero de espacios disponibles y python indexa las posiciones desde el 0 por lo cual al ingresar el argumento size a la funcion pop siempre va a estar por fuera de la lista
print(lista_colores.pop(size-1)) #Solucion al error de la linea anterior

lista_colores_3 = lista_colores*3 #Esto triplica los elementos de la lista, es decir, concatena la lista tres veces en una lista nueva
print("lista_colores_3 = ", lista_colores_3)

print("Sort:")
print()
lista_coloresSort = lista_colores.sort() #Organiza los elementos de la lista, OJO tiene que ser todos del mismo tipo de dato
print(lista_coloresSort) #Retorna none porque esta funcion solo organiza la lista no retorna una nueva

print("########################")
print("EJEMPLO CON LISTAS NUMERICAS")
print("########################")

lista_numerica = [10,9,8,7,6,5,4,3,2,1]
print(lista_numerica)
print("Ordenando la lista numerica: ")
lista_numerica.sort()
print(lista_numerica)
#lista_numericaOrdenada = lista_numerica.sort()
#print(lista_numericaOrdenada) Estas dos ultimas lineas de codigo tienen el mismo comportamiento que en el ejemplo de listas con strings

print("Ordenando la lista de mayor a menor")
lista_numerica.sort(reverse=True)
print(lista_numerica)

print("########################")
print("########################")
print("TUPLAS")
print("########################")

#Conversion de Lista a tupla

tupla_colores = tuple(lista_colores)  #Tuplas estan definidas por parentesis <<()>>
print("Tupla numerica: ", tupla_colores) 

print(tupla_colores[0])
print(tupla_colores[2])
#Imprimen el elemento en la posicion deseada

print('Rojo' in tupla_colores) #Evalua si un elemento esta contenido en la tupla retorna true/false
print(tupla_colores.count('Rojo')) #Evalua cuantas veces aparece un mismo elemento en la tupla

tupla_unitaria = ('Blanco',) #Tupla de un solo elemento
print(tupla_unitaria)
print(type(tupla_unitaria))


tupla_2 = 'Gaspar', 5 , 8 , 1999 #En python lo que hace una tupla tupla son las comas. Asi que la coma es la que crea las tuplas
print(tupla_2)

# En el caso de la tupla unitaria, si no se pone la coma, python no lo considera una tupla si no una variable del tipo que se ingreso
#Por eso, en el caso de la linea 87 si no se coloca la coma el tipo de la variable va a ser un str no una tupla.

nombre , dia , mes , año = tupla_2 # Tuple unpacking lo que hace es asignarle una variable al elemento de la tupla en el orden que esta establecido en la tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre , " - Dia: ", dia, " - Mes: " , mes, " - Año: ", año) #Facilita ya que al asignar variable a los elementos de las tuplas, no se necesita
#acceder a la tupla para usar el elemento de ella, lo que facilita el trabajo y el acceso a la informacion de la tupla.











