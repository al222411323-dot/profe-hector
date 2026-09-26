import datetime
import random

#reporte 
numero = random.randint(10000, 99999)

#identificador 
numero_reporte = "R" + str(numero)

#fecha y hora 
fecha_hora = datetime.now()

#formato 
fecha = fecha_hora.strftime("%Y-%m-%d %H:%M:%S")

#hora 
hora = fecha_hora.strftime("%H:%M:%S")

# Bienvenida al sistema 

print("=" * 55)
print("       SISTEMA DE DIAGNÓSTICO TÉCNICO - BIENVENIDA")
print("=" * 55)

nombre = input("Ingrese su nombre completo: ")
apellido = input("Ingrese su apellido: ")
direccion = input("Ingrese su dirección: ")

print("\nSeleccione el tipo de dispositivo:")
print("1. PC")
print("2. Laptop")
print("3. Servidor")
print("4. Tablet")

opcion = input("seleccione un opcion(1-4): ")

if opcion == "1":
    tipo_dispositivo = "PC"
elif opcion == "2":
    tipo_dispositivo = "Laptop"
elif opcion == "3":
    tipo_dispositivo = "Servidor"
elif opcion == "4":
    tipo_dispositivo = "Tablet"

else:
    tipo_dispositivo = "Dispositivo Desconocido"


numero_reporte = f"REP-{random.randint(10000, 99999)}"

# DIAGNÓSTICO 

print("\n--- CUESTIONARIO DE DIAGNÓSTICO ---")
electricidad = input("¿Tiene electricidad? (s/n): ").strip().lower() == "s"
enciende = input("¿Enciende? (s/n): ").strip().lower() == "s"
sistema = input("¿Carga el sistema operativo? (s/n): ").strip().lower() == "s"
sonido = input("¿Tiene sonido? (s/n): ").strip().lower() == "s"
internet = input("¿Tiene internet? (s/n): ").strip().lower() == "s"


# IMPRESIÓN DEL REPORTE FINAL

print("\n" + "=" * 55)
print("             REPORTE DE DIAGNÓSTICO DEL EQUIPO")
print("=" * 55)
print(f"Bienvenido(a), {nombre}!")
print(f"Apellido          : {apellido}")
print(f"Número de Reporte : {numero_reporte}")
print(f"Dirección         : {direccion}")
print(f"Tipo de Equipo    : {tipo_dispositivo}")
print("-" * 55)

if not electricidad:
    print("Diagnóstico: revisar alimentación.")
elif not enciende:
    print("Diagnóstico: revisar fuente de poder.")
elif not sistema:
    print("Diagnóstico: revisar disco duro.")
elif not internet:
    print("Diagnóstico: revisar conexión red.")
else:
    print("Diagnóstico: funcionamiento básico correcto.")

print("=" * 55)