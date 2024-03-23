#solicitar al usuario que ingrese 10 números 
numbers  = [] 
for i in range (10):
   num = float (input("ingresar el numero{}:".format(i+1))) 
   numbers.append(num)
   
   #Calcular el promedio de la lista
   average = sum(numbers)/len(numbers)
   
   #Mostrar el resultado del promedio al usuario 
   print("El promedio de los numeros ingresados es",average)
   
   
   