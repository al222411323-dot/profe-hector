# ============================================
# SISTEMA EXPERTO DE DIAGNÓSTICO Y CITAS
# ============================================

print("SISTEMA DE DIAGNÓSTICO Y AGENDAMIENTO\n")

# --- Recolección de datos del paciente ---
nombre = input("Nombre completo del paciente: ")
edad = input("Edad (años): ")
peso = input("Peso (kg): ")
tipo_sangre = input("Tipo de sangre (ej. O+, A-): ")

# --- Evaluación de síntomas ---
fiebre = input("¿Tiene fiebre? (s/n): ")
tos = input("¿Tiene tos? (s/n): ")
dolor = input("¿Tiene dolor de garganta? (s/n): ")
dificultad_respirar = input("¿Tiene dificultad para respirar? (s/n): ")


if dificultad_respirar == "s":

    diagnostico = "ALERTA: respiratoria aguda"
    cita = "Urgencia inmediata (Acudir al hospital o llamar a emergencias hoy mismo)"

elif fiebre == "s" and tos == "s" and dolor == "s":

    diagnostico = "Posible cuadro infeccioso respiratorio severo"
    cita = "Cita médica prioritaria (Aprox. en las próximas 12 a 24 horas)"

elif fiebre == "s" and tos == "s":

    diagnostico = "Posible infección respiratoria"
    cita = "Cita médica general (Aprox. en las próximas 24 a 48 horas)"

elif tos == "s" and dolor == "s":

    diagnostico = "Posible irritación respiratoria"
    cita = "Cita médica programada (Aprox. en 2 a 3 días si no mejora)"

elif fiebre == "s":

    diagnostico = "Síndrome febril aislado"
    cita = "Valoración profesional recomendada (Aprox. en 24 a 48 horas)"

else:

    diagnostico = "No se identificó un patrón de infección activo"
    cita = "No requiere cita de urgencia (Monitoreo en casa)"

# --- Resultados ---
print("\n============================================")
print("RESUMEN DEL PACIENTE")
print("============================================")
print("Paciente: " + nombre)
print("Edad: " + edad + " años | Peso: " + peso + " kg | Tipo de sangre: " + tipo_sangre)

print("\nRESULTADO DEL DIAGNÓSTICO:")
print(diagnostico)

print("\nRECOMENDACIÓN DE CITA MÉDICA:")
print(cita)