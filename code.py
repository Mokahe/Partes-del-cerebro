import streamlit as st

# --- 1. DATOS DEL CUESTIONARIO ---
quiz_data = [
    {
        "question": "¿Qué lóbulo cerebral es el principal responsable de las funciones ejecutivas, como la planificación y la personalidad?",
        "options": ["Lóbulo Parietal", "Lóbulo Frontal", "Lóbulo Temporal", "Lóbulo Occipital"],
        "correct_index": 1,
        "rationale_correct": "¡Correcto! El Lóbulo Frontal es la región más grande, encargada de las habilidades cognitivas de orden superior y la modulación de la conducta.",
        "rationale_incorrect": "Incorrecto. Las funciones ejecutivas son exclusivas del Lóbulo Frontal. Los otros lóbulos se centran en el procesamiento sensorial, auditivo o visual. La respuesta correcta es el Lóbulo Frontal."
    },
    {
        "question": "Una persona con dificultades en el equilibrio y la coordinación fina de movimientos probablemente tiene afectado el...",
        "options": ["Tálamo", "Hipocampo", "Cerebelo", "Bulbo Raquídeo"],
        "correct_index": 2,
        "rationale_correct": "¡Correcto! El Cerebelo es fundamental para coordinar el movimiento voluntario, el equilibrio y la precisión motora.",
        "rationale_incorrect": "Incorrecto. El Cerebelo controla la coordinación y el equilibrio. Las otras estructuras tienen funciones sensoriales, de memoria o vitales. La respuesta correcta es el Cerebelo."
    },
    {
        "question": "¿Cuál componente del tronco encefálico regula funciones vitales e involuntarias como la respiración y el ritmo cardíaco?",
        "options": ["Protuberancia anular", "Mesencéfalo", "Bulbo Raquídeo (Médula Oblongada)", "Hipotálamo"],
        "correct_index": 2,
        "rationale_correct": "¡Correcto! El Bulbo Raquídeo contiene centros de control autónomo esenciales para la supervivencia.",
        "rationale_incorrect": "Incorrecto. El Bulbo Raquídeo, en el tronco encefálico, es el centro de control para estas funciones vitales. La respuesta correcta es Bulbo Raquídeo (Médula Oblongada)."
    },
    {
        "question": "La corteza auditiva primaria y el área de Wernicke (comprensión del lenguaje) se localizan predominantemente en el...",
        "options": ["Lóbulo Frontal", "Lóbulo Temporal", "Lóbulo Parietal", "Lóbulo Occipital"],
        "correct_index": 1,
        "rationale_correct": "¡Correcto! El Lóbulo Temporal está asociado con el procesamiento de la información auditiva, el lenguaje comprensivo y la memoria.",
        "rationale_incorrect": "Incorrecto. El Lóbulo Temporal (cerca de los oídos) procesa la audición y la comprensión del lenguaje. La respuesta correcta es Lóbulo Temporal."
    },
    {
        "question": "¿Qué estructura del sistema límbico es crucial para el procesamiento de las emociones, especialmente el miedo y el aprendizaje emocional?",
        "options": ["Tálamo", "Hipocampo", "Amígdala", "Cuerpo Calloso"],
        "correct_index": 2,
        "rationale_correct": "¡Correcto! La Amígdala es esencial para la detección de amenazas y la respuesta emocional intensa ('lucha o huida').",
        "rationale_incorrect": "Incorrecto. La Amígdala se encarga del procesamiento del miedo y las emociones. La respuesta correcta es Amígdala."
    },
    {
        "question": "Si una persona pierde la capacidad de sentir el tacto o percibir la ubicación de sus extremidades (propiocepción), ¿qué lóbulo cerebral está afectado?",
        "options": ["Lóbulo Frontal", "Lóbulo Parietal", "Lóbulo Temporal", "Cerebelo"],
        "correct_index": 1,
        "rationale_correct": "¡Correcto! El Lóbulo Parietal contiene la corteza somatosensorial primaria, que procesa la información táctil, de temperatura, dolor y propiocepción.",
        "rationale_incorrect": "Incorrecto. El Lóbulo Parietal procesa la información somatosensorial (tacto, presión). La respuesta correcta es Lóbulo Parietal."
    },
    {
        "question": "¿Cuál es la principal función de la banda gruesa de fibras nerviosas conocida como Cuerpo Calloso?",
        "options": ["Controlar los movimientos automáticos.", "Almacenar recuerdos a largo plazo.", "Conectar los hemisferios cerebrales derecho e izquierdo.", "Filtrar la información sensorial."],
        "correct_index": 2,
        "rationale_correct": "¡Correcto! El Cuerpo Calloso es el puente más grande de sustancia blanca, permitiendo la comunicación entre los dos hemisferios cerebrales.",
        "rationale_incorrect": "Incorrecto. La función principal del Cuerpo Calloso es la comunicación inter-hemisférica. La respuesta correcta es Conectar los hemisferios cerebrales derecho e izquierdo."
    },
    {
        "question": "El Hipotálamo es esencial para mantener la homeostasis (temperatura, sed, hambre) y la conexión con la glándula pituitaria. ¿A qué sistema(s) está funcionalmente ligado?",
        "options": ["Sistema Nervioso y Sistema Endocrino", "Sistema Límbico y Sistema Motor", "Sistema Respiratorio y Sistema Circulatorio", "Corteza Cerebral y Cerebelo"],
        "correct_index": 0,
        "rationale_correct": "¡Correcto! El Hipotálamo pertenece al Sistema Nervioso (Diencéfalo) y es el centro de control del Sistema Endocrino a través de la pituitaria.",
        "rationale_incorrect": "Incorrecto. Su papel como centro de control hormonal lo liga intrínsecamente al Sistema Endocrino, además del Nervioso. La respuesta correcta es Sistema Nervioso y Sistema Endocrino."
    },
    {
        "question": "Una lesión en la parte posterior de la cabeza que afecta la corteza visual primaria resultaría en una alteración en la...",
        "options": ["Capacidad para formar nuevas memorias.", "Percepción e interpretación de la información visual.", "Coordinación y el equilibrio.", "Comprensión del lenguaje hablado."],
        "correct_index": 1,
        "rationale_correct": "¡Correcto! La corteza visual primaria se encuentra en el Lóbulo Occipital, lo que lo convierte en el centro principal para la interpretación de todo lo que vemos.",
        "rationale_incorrect": "Incorrecto. La corteza visual primaria en el Lóbulo Occipital está dedicada a la vista. La respuesta correcta es Percepción e interpretación de la información visual."
    },
    {
        "question": "¿En qué región del Lóbulo Frontal se origina específicamente la señal para realizar los movimientos voluntarios del cuerpo?",
        "options": ["El Área de Broca", "La Corteza Prefrontal", "La Cisura de Silvio", "La Corteza Motora Primaria"],
        "correct_index": 3,
        "rationale_correct": "¡Correcto! La Corteza Motora Primaria, ubicada en la parte posterior del Lóbulo Frontal, es el origen del control y planificación de los movimientos corporales voluntarios.",
        "rationale_incorrect": "Incorrecto. La Corteza Motora Primaria controla el movimiento. El Área de Broca es para el habla; la Corteza Prefrontal, para la planificación. La respuesta correcta es La Corteza Motora Primaria."
    }
]

# --- FUNCIÓN PARA REINICIAR EL ESTADO ---
def reset_quiz():
    """Limpia el estado de la sesión para reiniciar el quiz."""
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()

# --- 2. INICIALIZAR EL ESTADO DE LA SESIÓN ---
if 'current_q' not in st.session_state:
    st.session_state['current_q'] = 0
    st.session_state['score'] = 0
    st.session_state['feedback'] = ""
    # Esta bandera ahora indica si la pregunta ha sido respondida (correcta o incorrecta)
    st.session_state['answered'] = False 

# --- 3. CONFIGURACIÓN DE LA PÁGINA Y BARRA LATERAL ---
st.set_page_config(
    page_title="Quiz sobre las Partes del Cerebro",
    layout="centered"
)
st.title("🧠 Quiz Interactivo: Las Partes del Cerebro")

# Botón de Reinicio en la barra lateral
st.sidebar.header("Opciones del Quiz")
if st.sidebar.button("Reiniciar Quiz (Borrar Progreso)"):
    reset_quiz()

# Mostrar progreso en la barra lateral
total_questions = len(quiz_data)
st.sidebar.header("Progreso")
st.sidebar.info(f"Pregunta: {st.session_state.current_q} / {total_questions}")
st.sidebar.metric("Aciertos totales", st.session_state.score)

# --- 4. LÓGICA DEL CUESTIONARIO ---

# 4.1. Mostrar resultado final
if st.session_state.current_q >= total_questions:
    st.header("¡Cuestionario Terminado! 🎉")
    
    if st.session_state.score == total_questions:
        st.balloons()
        st.success("¡Felicidades! Tienes un conocimiento experto del cerebro.")
    else:
        st.info("¡Buen trabajo! Has completado el cuestionario.")

    st.metric(
        label="Puntuación Final (Total de Aciertos)",
        value=f"{st.session_state.score} / {total_questions}"
    )
    
    # Se añade un botón de reinicio al final también
    if st.button("Reiniciar Cuestionario"):
        reset_quiz()

# 4.2. Mostrar pregunta actual
else:
    current_index = st.session_state.current_q
    q = quiz_data[current_index]

    st.subheader(f"Pregunta {current_index + 1} de {total_questions}")
    st.write(q["question"])

    # 4.2.1 Mostrar Retroalimentación y Botón de Avance
    if st.session_state.answered:
        # Muestra el feedback
        if st.session_state.feedback.startswith("¡Correcto"):
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)
        
        # Botón para avanzar a la siguiente pregunta
        if st.button("Siguiente Pregunta"):
            # Lógica de avance
            st.session_state.current_q += 1
            st.session_state.answered = False
            st.session_state.feedback = ""
            # Eliminamos el estado del radio button para que no arrastre la selección
            del st.session_state[f'radio_{current_index}'] 
            st.rerun()

    # 4.2.2 Formulario de respuesta (oculto si ya fue respondida)
    if not st.session_state.answered:
        with st.form(key=f'q_form_{current_index}'):
            radio_key = f'radio_{current_index}'
            
            user_choice = st.radio(
                "Selecciona tu respuesta:",
                options=q["options"],
                index=None,
                key=radio_key
            )
            
            submitted = st.form_submit_button("Responder")

        # 4.3. Lógica de evaluación (solo se ejecuta si se envía el formulario)
        if submitted:
            if user_choice is None:
                st.warning("Por favor, selecciona una opción antes de responder.")
            
            elif user_choice in q["options"]:
                user_index = q["options"].index(user_choice)
                
                # Evaluación
                if user_index == q["correct_index"]:
                    st.session_state.score += 1
                    st.session_state.feedback = q["rationale_correct"]
                # Caso Incorrecto
                else:
                    st.session_state.feedback = q["rationale_incorrect"]
                
                # Marcamos como respondida para mostrar el feedback y el botón "Siguiente Pregunta"
                st.session_state.answered = True 
                st.rerun()
