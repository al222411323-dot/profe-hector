# ============================================================
# PRACTICA 2
# TUTOR INTELIGENTE CON LLM
# ============================================================
#
# Objetivo:
# Crear un asistente educativo especializado utilizando
# un modelo de lenguaje LLM ejecutado mediante Ollama.
#
# Modelo:
# llama3.2
#
# ============================================================


# ------------------------------------------------------------
# 1. IMPORTAR LA BIBLIOTECA
# ------------------------------------------------------------

import ollama


# ------------------------------------------------------------
# 2. CONFIGURACIÓN DEL MODELO
# ------------------------------------------------------------

MODELO = "llama3.2"


# ------------------------------------------------------------
# 3. CONFIGURACIÓN DEL SISTEMA
# ------------------------------------------------------------
#
# El mensaje "system" establece el comportamiento general
# que queremos que tenga nuestro asistente.
#
# ------------------------------------------------------------

mensaje_sistema = """
Eres un experto en Ciberseguridad.

Tu función es:

1. Explicar amenazas informáticas.
2. Enseñar conceptos de seguridad.
3. Ayudar a proteger equipos.
4. Explicar paso a paso.
5. Utilizar ejemplos sencillos.
6. Recomendar buenas prácticas.
7. No proporcionar actividades peligrosas.
"""


# ------------------------------------------------------------

# 4. CREAR HISTORIAL
# ------------------------------------------------------------
#
# El historial permitirá que posteriormente nuestro programa
# pueda mantener el contexto de la conversación.
#
# ------------------------------------------------------------

mensajes = [

    {
        "role": "system",
        "content": mensaje_sistema
    }

]


# ------------------------------------------------------------
# 5. ENCABEZADO DEL PROGRAMA
# ------------------------------------------------------------

print("=" * 50)
print("          TUTOR INTELIGENTE CON LLM")
print("=" * 50)

print("Modelo utilizado:", MODELO)
print()
print("Escribe 'salir' para terminar.")
print()


# ------------------------------------------------------------
# 6. BUCLE PRINCIPAL
# ------------------------------------------------------------

while True:

    # --------------------------------------------------------
    # Solicitar pregunta
    # --------------------------------------------------------

    pregunta = input("Estudiante: ")


    # --------------------------------------------------------
    # Comprobar si desea terminar
    # --------------------------------------------------------

    if pregunta.lower() == "salir":

        print()
        print("Sesión finalizada.")

        break


    # --------------------------------------------------------
    # Agregar pregunta al historial
    # --------------------------------------------------------

    mensajes.append(
        {
            "role": "user",
            "content": pregunta
        }
    )


    # --------------------------------------------------------
    # ENVIAR INFORMACIÓN AL LLM
    # --------------------------------------------------------

    try:

        respuesta = ollama.chat(

            model=MODELO,

            messages=mensajes

        )


    # --------------------------------------------------------
    # MANEJO DE ERRORES
    # --------------------------------------------------------

    except Exception as error:

        print()
        print("ERROR AL CONECTARSE CON EL LLM")
        print("--------------------------------")

        print(error)

        print()

        print("Verifica que Ollama esté ejecutándose.")

        # Eliminamos la pregunta del historial porque
        # no pudo ser procesada.

        mensajes.pop()

        continue


    # --------------------------------------------------------
    # EXTRAER RESPUESTA
    # --------------------------------------------------------

    contenido = respuesta["message"]["content"]


    # --------------------------------------------------------
    # GUARDAR RESPUESTA EN EL HISTORIAL
    # --------------------------------------------------------

    mensajes.append(
        {
            "role": "assistant",
            "content": contenido
        }
    )


    # --------------------------------------------------------
    # MOSTRAR RESPUESTA
    # --------------------------------------------------------

    print()
    print("TUTOR:")
    print()

    print(contenido)

    print()
    print("-" * 50)


# python -m py_compile unidad2_fia/p02primer_llm.py (comprueba que la sintaxis de python es correcta)

        #       SYSTEM
        #         │
        #         ▼
        #    Comportamiento
        #         │
        #         ▼
# USER ────────► LLM
        #         │
        #         ▼
        #      ASSISTANT