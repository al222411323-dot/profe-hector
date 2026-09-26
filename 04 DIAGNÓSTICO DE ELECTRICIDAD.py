# ============================================
# SISTEMA DE DIAGNÓSTICO DE ELECTRICIDAD
# ============================================

print("=" * 55)
print("          SISTEMA DE ELECTRICIDAD Y HARDWARE")
print("=" * 55)

# Captura de datos iniciales
electricidad_in = input("¿Tiene electricidad? (si/no): ").strip().lower()
enciende_in = input("¿Enciende el equipo? (si/no): ").strip().lower()
imagen_in = input("¿Muestra imagen la pantalla? (si/no): ").strip().lower()

# Conversión a booleanos
electricidad = electricidad_in == "si"
enciende = enciende_in == "si"
imagen = imagen_in == "si"

# 1. EVALUACIÓN DE ERRORES EN ENTRADAS USANDO 'OR' Y 'NOT'
# Si alguna respuesta NO es 'si' Y tampoco es 'no', hay un error de captura
entrada_invalida = (not (electricidad_in == "si" or electricidad_in == "no") or
                    not (enciende_in == "si" or enciende_in == "no") or
                    not (imagen_in == "si" or imagen_in == "no"))

if entrada_invalida:
    print("\n[!] ERROR DE ENTRADA: Solo se permite responder 'si' o 'no'.")

# 2. EVALUACIÓN DE DIAGNÓSTICO USANDO 'AND', 'OR' Y 'NOT'
else:
    # Caso 1: Falla total de energía o fallo en encendido
    if not electricidad or not enciende:
        print("\nDIAGNÓSTICO:")
        if not electricidad:
            print("Fallo en la alimentación eléctrica principal.")
            print("\nPROPUESTA:")
            print("- Revisar conexión eléctrica.")
            print("- Revisar interruptor o pastilla del centro de carga.")
            print("- Revisar cable de alimentación.")
        elif not enciende:
            print("El equipo recibe energía pero no completa el encendido (Fuente de poder).")
            print("\nPROPUESTA:")
            print("- Revisar fuente de alimentación.")
            print("- Revisar cable de corriente interno.")
            print("- Revisar fusible o protección de sobrevoltaje.")

    # Caso 2: El equipo enciende pero falla la imagen
    elif enciende and not imagen:
        print("\nDIAGNÓSTICO:")
        print("El sistema enciende correctamente pero no emite señal de video.")
        print("\nPROPUESTA:")
        print("- Revisar cable HDMI/VGA/DisplayPort o adaptadores.")
        print("- Revisar el monitor o probar en una pantalla externa.")
        print("- Revisar la tarjeta de video integrada/dedicada.")

    # Caso 3: Funcionamiento óptimo (Tiene electricidad AND enciende AND muestra imagen)
    elif electricidad and enciende and imagen:
        print("\nDIAGNÓSTICO:")
        print("El sistema enciende, recibe energía y proyecta imagen de forma correcta.")
        print("\nPROPUESTA:")
        print("- Revisar sistema de monitoreo de temperaturas.")
        print("- Revisar uso de memoria RAM.")
        print("- Realizar mantenimiento preventivo general.")

print("=" * 55)