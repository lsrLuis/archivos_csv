import csv

print "--------------------------------"
print "\t \t \t Agenda"
a = 1
while a == 1:
    print "--------------------------------"
    print "1) Leer"
    print "2) Insertar"
    print "3) Salir"
    print "--------------------------------"
    opcion = input("Elija una opcion por favor: ")
    print "--------------------------------"
    if opcion == 1:
        with open("data.csv","r") as file:
            data = csv.reader(file, delimiter='|')
            for x in data:
                print x
    elif opcion == 2:
        nombre = raw_input("Ingrese el nombre: ")
        email = raw_input("Ingrese el e-mail: ")
        with open("data.csv","a") as file:
            data = csv.writer(file, delimiter='|')
            data.writerow([nombre,email])
    elif opcion == 3:
        print "--------------------------------"
        print "Gracias por su preferencia"
        print "Realizado por Luis Sanchez Rosas"
        print "--------------------------------"
        break
