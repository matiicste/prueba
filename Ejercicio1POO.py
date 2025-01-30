class Estudiante:
    def __init__ (self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando")

nombre = input("ingrese el nombre del estudiante: ")
edad = input("ingrese la edad del estudiante: ")
grado = input("ingrese el grado del estudiante: ")

estudiante = Estudiante(nombre,edad,grado)

print(f"""
    DATOS DEL ESTUDIANTE: \n\n
    nombre: {estudiante.nombre}\n
    edad: {estudiante.edad}\n
    grado: {estudiante.grado}\n
    
    """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante.estudiar()