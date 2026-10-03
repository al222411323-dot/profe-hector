import tkinter as tk
from tkinter import messagebox
import ollama

# =========================
# CONFIGURACIÓN DEL LLM
# =========================

MODELO = "llama3.2:1b"

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

mensajes = [
    {
        "role": "system",
        "content": mensaje_sistema
    }
]

# =========================
# FUNCIÓN ENVIAR
# =========================

def enviar():

    pregunta = entrada.get()

    if pregunta.strip() == "":
        return

    chat.insert(
        tk.END,
        f"\nUsuario: {pregunta}\n"
    )

    mensajes.append(
        {
            "role": "user",
            "content": pregunta
        }
    )

    try:

        respuesta = ollama.chat(
            model=MODELO,
            messages=mensajes
        )

        contenido = respuesta["message"]["content"]

        mensajes.append(
            {
                "role": "assistant",
                "content": contenido
            }
        )

        chat.insert(
            tk.END,
            f"\nTutor:\n{contenido}\n"
        )

        chat.see(tk.END)

    except Exception as error:

        messagebox.showerror(
            "Error",
            f"No fue posible conectar con Ollama:\n\n{error}"
        )

    entrada.delete(0, tk.END)

# =========================
# FUNCIÓN RESUMEN
# =========================

def generar_resumen():

    historial = ""

    for m in mensajes:

        if m["role"] != "system":

            historial += f"{m['role']}: {m['content']}\n"

    try:

        respuesta = ollama.chat(
            model=MODELO,
            messages=[
                {
                    "role": "user",
                    "content":
                    f"""
Resume la conversación.

Incluye:

1. Temas tratados.
2. Conceptos aprendidos.
3. Conclusiones.

{historial}
"""
                }
            ]
        )

        resumen = respuesta["message"]["content"]

        chat.insert(
            tk.END,
            "\n\n===== RESUMEN DE LA CONVERSACIÓN =====\n"
        )

        chat.insert(
            tk.END,
            resumen + "\n"
        )

    except Exception as error:

        messagebox.showerror(
            "Error",
            str(error)
        )

# =========================
# LIMPIAR CHAT
# =========================

def limpiar():

    chat.delete(
        1.0,
        tk.END
    )

# =========================
# INTERFAZ GRÁFICA
# =========================

ventana = tk.Tk()

ventana.title(
    "Tutor Inteligente de Ciberseguridad"
)

ventana.geometry(
    "900x700"
)

titulo = tk.Label(
    ventana,
    text="Tutor Inteligente de Ciberseguridad",
    font=("Arial", 16, "bold")
)

titulo.pack(pady=10)

chat = tk.Text(
    ventana,
    width=100,
    height=25
)

chat.pack(pady=10)

entrada = tk.Entry(
    ventana,
    width=80
)

entrada.pack(pady=5)

btn_enviar = tk.Button(
    ventana,
    text="Enviar",
    command=enviar
)

btn_enviar.pack(pady=5)

btn_resumen = tk.Button(
    ventana,
    text="Generar Resumen",
    command=generar_resumen
)

btn_resumen.pack(pady=5)

btn_limpiar = tk.Button(
    ventana,
    text="Limpiar Chat",
    command=limpiar
)

btn_limpiar.pack(pady=5)

ventana.mainloop()