# ==========================================================
# DIAGNÓSTICO BÁSICO DEL EQUIPO
# ==========================================================

electricidad = input("¿Tiene electricidad? (s/n): ") == "s"
enciende = input("¿Enciende? (s/n): ") == "s"
imagen = input("¿Muestra imagen? (s/n): ") == "s"
sistema = input("¿Carga el sistema operativo? (s/n): ") == "s"
sonido = input("¿Tiene sonido? (s/n): ") == "s"
internet = input("¿Tiene internet? (s/n): ") == "s"

print("\n" + "=" * 55)
print("             DIAGNÓSTICO DEL EQUIPO")
print("=" * 55)

if not electricidad:
    print("Diagnóstico: revisar alimentación.")

elif not enciende:
    print("Diagnóstico: revisar fuente de poder.")

elif not imagen:
    print("Diagnóstico: revisar monitor.")

elif not sistema:
    print("Diagnóstico: revisar disco duro.")

elif not sonido:
    print("Diagnóstico: revisar altavoces / audio.")

elif not internet:
    print("Diagnóstico: revisar conexión Wi-Fi / red.")

else:
    print("Diagnóstico: funcionamiento básico correcto.")