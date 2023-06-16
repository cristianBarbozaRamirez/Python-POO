from cosas import Libro,Autor,Persona,Alumno

def main():

    l1 = Libro.libro_planeta("el perfume",Autor("Patrik","PS"),1980)
    print(l1)
    l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
    print(l1)
    print("-------Herencia---------------")
    al2 = Alumno("jose",19,"3232322334","ICO",9)
    al2.nombre = "pepe"
    print(vars(al2))
    print(al2.nombre)
main()