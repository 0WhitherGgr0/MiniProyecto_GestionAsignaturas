# -*- coding: utf-8 -*-
"""Miniproyecto2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eCf1MIUOuxDyO5qakJkzGjYel5Rb9CXk
"""

# Mini proyecto: Gestión de Asignaturas y Estudiantes


from itertools import combinations

class Asignatura:
    def __init__(self, nombre, codigo, requisitos=None):
        self.nombre = nombre
        self.codigo = codigo
        self.requisitos = requisitos if requisitos is not None else set()

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}"

class Estudiante:
    def __init__(self, nombre, numero_estudiante):
        self.nombre = nombre
        self.numero_estudiante = numero_estudiante
        self.inscripciones = set()

    def inscribir_asignatura(self, asignatura):
        if asignatura not in self.inscripciones:
            self.inscripciones.add(asignatura)
            print(f"{self.nombre} se ha inscrito en {asignatura.nombre}")

    def verificar_requisitos(self):
        cumplidos = all(req in self.inscripciones for req in self.inscripciones)
        return cumplidos

    def __str__(self):
        return f"Número de estudiante: {self.numero_estudiante}, Nombre: {self.nombre}"

class SistemaGestionAcademica:
    def __init__(self):
        self.asignaturas = {}
        self.estudiantes = {}

    def agregar_asignatura(self, nombre, codigo, requisitos=None):
        if codigo not in self.asignaturas:
            asignatura = Asignatura(nombre, codigo, requisitos)
            self.asignaturas[codigo] = asignatura
            print(f"Se ha agregado la asignatura: {asignatura}")
        else:
            print(f"El código de asignatura {codigo} ya existe. No se agregó la asignatura.")

    def eliminar_asignatura(self, codigo):
        if codigo in self.asignaturas:
            del self.asignaturas[codigo]
            print(f"Se ha eliminado la asignatura con código: {codigo}")
        else:
            print(f"No se encontró la asignatura con código: {codigo}")

    def registrar_estudiante(self, nombre, numero_estudiante):
        if numero_estudiante not in self.estudiantes:
            estudiante = Estudiante(nombre, numero_estudiante)
            self.estudiantes[numero_estudiante] = estudiante
            print(f"Se ha registrado al estudiante: {estudiante}")
        else:
            print(f"El número de estudiante {numero_estudiante} ya existe. No se registró al estudiante.")

    def mostrar_asignaturas(self):
        print("\nLista de asignaturas disponibles:")
        for asignatura in self.asignaturas.values():
            print(asignatura)

    def inscribir_estudiante_en_asignatura(self, numero_estudiante, codigo_asignatura):
        estudiante = self.estudiantes.get(numero_estudiante)
        asignatura = self.asignaturas.get(codigo_asignatura)

        if estudiante is not None and asignatura is not None:
            if asignatura in estudiante.inscripciones:
                print(f"{estudiante.nombre} ya está inscrito en {asignatura.nombre}.")
            else:
                if all(req in estudiante.inscripciones for req in asignatura.requisitos):
                    estudiante.inscribir_asignatura(asignatura)
                else:
                    print(f"{estudiante.nombre} no cumple con los requisitos para {asignatura.nombre}.")
        else:
            print("Número de estudiante o código de asignatura no encontrado.")

    def listar_estudiantes_inscritos(self):
        print("\nLista de estudiantes y sus inscripciones:")
        for estudiante in self.estudiantes.values():
            print(estudiante)
            if estudiante.inscripciones:
                for asignatura in estudiante.inscripciones:
                    print(f"- {asignatura.nombre}")

    def calcular_combinaciones_posibles(self, numero_estudiante):
        estudiante = self.estudiantes.get(numero_estudiante)

        if estudiante is not None:
            asignaturas_disponibles = list(self.asignaturas.values())
            combinaciones = []

            # Genera todas las combinaciones posibles de asignaturas para el estudiante.
            for r in range(1, len(asignaturas_disponibles) + 1):
                for combo in combinations(asignaturas_disponibles, r):
                    combinaciones.append(combo)

            print(f"\nEl estudiante {estudiante.nombre} podría tomar un total de {len(combinaciones)} combinaciones de asignaturas:")
            for i, combo in enumerate(combinaciones, start=1):
                print(f"Combinación {i}: {[asig.nombre for asig in combo]}")
        else:
            print("Número de estudiante no encontrado.")

# Ejemplo de uso:
# Crear una instancia del sistema de gestión académica
sistema_academico = SistemaGestionAcademica()

# Agregar algunas asignaturas con requisitos
sistema_academico.agregar_asignatura("Matemáticas", "MAT101")
sistema_academico.agregar_asignatura("Física", "PHY201")
sistema_academico.agregar_asignatura("Química", "CHE301")
sistema_academico.agregar_asignatura("Biología", "BIO401", requisitos={"MAT101"})
sistema_academico.agregar_asignatura("Historia", "HIS501")

# Registrar algunos estudiantes
sistema_academico.registrar_estudiante("Juan Pérez", "2023001")
sistema_academico.registrar_estudiante("Ana García", "2023002")
sistema_academico.registrar_estudiante("Luis Rodríguez", "2023003")

# Inscribir estudiantes en asignaturas
sistema_academico.inscribir_estudiante_en_asignatura("2023001", "MAT101")
sistema_academico.inscribir_estudiante_en_asignatura("2023001", "PHY201")
sistema_academico.inscribir_estudiante_en_asignatura("2023002", "MAT101")
sistema_academico.inscribir_estudiante_en_asignatura("2023002", "BIO401")
sistema_academico.inscribir_estudiante_en_asignatura("2023003", "HIS501")

# Mostrar la lista de asignaturas disponibles
sistema_academico.mostrar_asignaturas()

# Listar estudiantes y sus inscripciones
sistema_academico.listar_estudiantes_inscritos()

# Calcular combinaciones posibles para un estudiante
sistema_academico.calcular_combinaciones_posibles("2023001")

# Verificar requisitos de un estudiante
juan = sistema_academico.estudiantes["2023001"]
biologia = sistema_academico.asignaturas["BIO401"]
print(f"{juan.nombre} cumple con los requisitos de Biología: {juan.verificar_requisitos()}")

# Eliminar una asignatura
sistema_academico.eliminar_asignatura("PHY201")
sistema_academico.mostrar_asignaturas()

# Crear una instancia del sistema de gestión académica
sistema_academico = SistemaGestionAcademica()

# Agregar algunas asignaturas
sistema_academico.agregar_asignatura("Matemáticas", "MAT101")
sistema_academico.agregar_asignatura("Física", "PHY201")
sistema_academico.agregar_asignatura("Química", "CHE301")

# Eliminar la asignatura "Química"
sistema_academico.eliminar_asignatura("CHE301")

# Mostrar la lista de asignaturas disponibles después de la eliminación
sistema_academico.mostrar_asignaturas()

# Ejemplo de uso:

# Crear una instancia del sistema de gestión académica
sistema_academico = SistemaGestionAcademica()

# Agregar algunas asignaturas con requisitos
sistema_academico.agregar_asignatura("Matemáticas", "MAT101")
sistema_academico.agregar_asignatura("Física", "PHY201")
sistema_academico.agregar_asignatura("Química", "CHE301")
sistema_academico.agregar_asignatura("Biología", "BIO401", requisitos={"MAT101"})
sistema_academico.agregar_asignatura("Historia", "HIS501")

# Registrar algunos estudiantes
sistema_academico.registrar_estudiante("Juan Pérez", "2023001")
sistema_academico.registrar_estudiante("Ana García", "2023002")
sistema_academico.registrar_estudiante("Luis Rodríguez", "2023003")

# Inscribir estudiantes en asignaturas
sistema_academico.inscribir_estudiante_en_asignatura("2023001", "MAT101")
sistema_academico.inscribir_estudiante_en_asignatura("2023001", "PHY201")
sistema_academico.inscribir_estudiante_en_asignatura("2023002", "MAT101")
sistema_academico.inscribir_estudiante_en_asignatura("2023002", "BIO401")
sistema_academico.inscribir_estudiante_en_asignatura("2023003", "HIS501")

# Mostrar la lista de asignaturas disponibles
sistema_academico.mostrar_asignaturas()

# Listar estudiantes y sus inscripciones
sistema_academico.listar_estudiantes_inscritos()

# Calcular combinaciones posibles para un estudiante
sistema_academico.calcular_combinaciones_posibles("2023001")

# Verificar requisitos de un estudiante
juan = sistema_academico.estudiantes["2023001"]
biologia = sistema_academico.asignaturas["BIO401"]
print(f"{juan.nombre} cumple con los requisitos de Biología: {juan.verificar_requisitos()}")

# Eliminar una asignatura
sistema_academico.eliminar_asignatura("PHY201")

# Mostrar la lista de asignaturas disponibles después de la eliminación
sistema_academico.mostrar_asignaturas()

# Ejemplo de uso:

sistema_academico = SistemaGestionAcademica()

sistema_academico.agregar_asignatura("Matemáticas", "MAT101")
sistema_academico.agregar_asignatura("Física", "PHY201")
sistema_academico.agregar_asignatura("Química", "CHE301")

sistema_academico.registrar_estudiante("Juan Pérez", "2023001")
sistema_academico.registrar_estudiante("Ana García", "2023002")

sistema_academico.inscribir_estudiante_en_asignatura("2023001", "MAT101")
sistema_academico.inscribir_estudiante_en_asignatura("2023001", "PHY201")
sistema_academico.inscribir_estudiante_en_asignatura("2023002", "MAT101")

sistema_academico.mostrar_asignaturas()
sistema_academico.listar_estudiantes_inscritos()
sistema_academico.calcular_combinaciones_posibles("2023001")