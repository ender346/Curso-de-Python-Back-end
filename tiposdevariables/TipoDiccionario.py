# Información del estudiante
estudiante = {
    "nombre": "Ana",
    "edad": 20,
    "carrera": "Informática",
    "notas": {"matemáticas": 95, "historia": 88, "programación": 92}
}

# Mostrar información del estudiante
print(f"Nombre: {estudiante['nombre']}")
print(f"Edad: {estudiante['edad']} años")
print(f"Carrera: {estudiante['carrera']}")
print("Notas:")
for asignatura, nota in estudiante["notas"].items():
    print(f"- {asignatura}: {nota}")
