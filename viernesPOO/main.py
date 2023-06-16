from cosas import *

def main():
    per1 = Persona("jose",19)
    print(per1)
    print(Persona.descripcion)

    print("----herencia alumno----")
    al1 = Alumno("jose",19,"233232323232","ICO")
    print(al1)
    print(Alumno.descripcion)

    al2 = Alumno.constructor_defecto()

    print(al2)

    al2.nombre = "juan"
    print(al2)
    al2.dormir()


    print("----herencia profesor---")

    profe1 = Profesor("jesus",30+16,344343,"ingenieria de software")
    print(profe1)
    profe1.dormir()

    print("-----Ayudante profesor------")
    ayudante  = AyudanteProfesor("Adrian",20,"23323","ICO",232323,"ing. de software",4)
    print(ayudante)
    ayudante.dormir()
    ayudante.nombre = "Abraham"
    ayudante.dar_clase("POO")

main()