
from cosas import Alumno
from cosas import Perro
def main():
    al1 = Alumno("jose",19,"ICO")
    print(vars(al1))
    al1.__nombre = "diego"
    print(vars(al1))
    al1.set_nombre("pablo")
    print(vars(al1))

    print("--------to string ---------")
    print(al1)

    perro1 = Perro("poddle",2,0.35)
    print(vars(perro1))
    perro1.raza = "De la calle"
    print(vars(perro1))

    perro1.__raza ="otra"
    print(vars(perro1))
    perro1.edad = 12
    perro1.estatura = 0.43

    print(perro1)
    cachorro = perro1.es_cachorro(perro1.edad)
    print(cachorro)
    Perro.dormir()
    danes = Perro.perro_grande((0.8))
    print(danes)

main()