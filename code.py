import streamlit as st

# --- 1. DATOS DEL CUESTIONARIO (Los ítems generados) ---
# En una aplicación real alojada en GitHub, podrías mover esta estructura
# a un archivo JSON o CSV y cargarlo usando 'pd.read_csv' o 'json.load'.
quiz_data = [
    {
        "question": "¿Qué lóbulo cerebral es el principal responsable de las funciones ejecutivas, como la planificación y la personalidad?",
        "options": ["Lóbulo Parietal", "Lóbulo Frontal", "Lóbulo Temporal", "Lóbulo Occipital"],
        "correct_index": 1,
        "rationale_correct": "¡Correcto! El Lóbulo Frontal es la región más grande, encargada de las habilidades cognitivas de orden superior y la modulación de la conducta.",
        "rationale_incorrect": "Incorrecto. Las funciones ejecutivas son exclusivas del Lóbulo Frontal. Los otros lóbulos se centran en el procesamiento sensorial, auditivo o visual."
    },
    {
        "question": "Una persona con dificultades en el equilibrio y la coordinación fina de movimientos probablemente tiene afectado el...",
        "options": ["Tálamo", "Hipocampo", "Cerebelo", "Bulbo Raquídeo"],
        "correct_index": 2,
        "rationale_correct": "¡Correcto! El Cerebelo es fundamental para coordinar el movimiento voluntario, el equilibrio y la precisión motora.",
        "rationale_incorrect": "Incorrecto. El Cerebelo controla la coordinación y el equilibrio. Las otras estructuras tienen funciones sensoriales (Tálamo), de memoria (Hipocampo) o vitales (Bulbo Raquídeo)."
    },
    {
        "question": "¿Cuál componente del tronco encefálico regula funciones vitales e involuntarias como la respiración y el ritmo cardíaco?",
        "options": ["Protuberancia anular", "Mesencéfalo", "Bulbo Raquídeo (Médula Oblongada)", "Hipotálamo"],
        "correct_index": 2,
        "rationale_correct": "¡Correcto! El Bulbo Raquídeo contiene centros de control autónomo esenciales para la supervivencia.",
        "rationale_incorrect": "Incorrecto. El Bulbo Raquídeo, en el tronco encefálico, es el centro de control para estas funciones vitales. El Hipotálamo controla la homeostasis general y hormonas."
    },
    {
        "question": "La corteza auditiva primaria y el área de Wernicke (comprensión del lenguaje) se localizan predominantemente en el...",
        "options": ["Lóbulo Frontal", "Lóbulo Temporal", "Lóbulo Parietal", "Lóbulo Occipital"],
        "correct_index": 1,
        "rationale_correct": "¡Correcto! El Lóbulo Temporal está asociado con el procesamiento de la información auditiva, el lenguaje comprensivo y la memoria.",
        "rationale_incorrect": "Incorrecto. El Lóbulo Temporal (cerca de los oídos) procesa la audición y la comprensión del lenguaje. Los otros lóbulos son para funciones ejecutivas, sensoriales o visuales."
    },
    {
        "question": "¿Qué estructura del sistema límbico es crucial para el procesamiento de las emociones, especialmente el miedo y el aprendizaje emocional?",
        "options": ["Tálamo", "Hipocampo", "Amígdala", "Cuerpo Calloso"],
        "correct_index": 2,
        "rationale_correct": "¡Correcto! La Amígdala es esencial para la detección de amenazas y la respuesta emocional intensa ('lucha o huida').",
        "rationale_incorrect": "Incorrecto. La Amígdala se encarga del procesamiento del miedo y las emociones. El Hipocampo es para la memoria; el Cuerpo Calloso, para la comunicación hemisférica."
    },
    {
        "question": "Si una persona pierde la capacidad de sentir el tacto o percibir la ubicación de sus extremidades (propiocepción), ¿qué lóbulo cerebral está afectado?",
        "options": ["Lóbulo Frontal", "Lóbulo Parietal", "Lóbulo Temporal", "Cerebelo"],
        "correct_index": 1,
        "rationale_correct": "¡Correcto! El Lóbulo Parietal contiene la corteza somatosensorial primaria, que procesa la información táctil, de temperatura, dolor y propiocepción.",
        "rationale_incorrect": "Incorrecto. El Lóbulo Parietal procesa la información somatosensorial (tacto, presión). El Lóbulo Frontal es motor, el Temporal es auditivo y el Cerebelo es de coordinación."
    },
    {
        "question": "¿Cuál es la principal función de la banda gruesa de fibras nerviosas conocida como Cuerpo Calloso?",
        "options": ["Controlar los movimientos automáticos.", "Almacenar recuerdos a largo plazo.", "Conectar los hemisferios cerebrales derecho e izquierdo.", "Filtrar la información sensorial."],
        "correct_index": 2,
        "rationale_correct": "¡Correcto! El Cuerpo Calloso es el puente más grande de sustancia blanca, permitiendo la comunicación entre los dos hemisferios cerebrales.",
        "rationale_incorrect": "Incorrecto. La función principal del Cuerpo Calloso es la comunicación inter-hemisférica. Controlar movimientos automáticos es de los ganglios basales; filtrar información, del Tálamo."
    },
    {
        "question": "El Hipotálamo es esencial para mantener la homeostasis (temperatura, sed, hambre) y la conexión con la glándula pituitaria. ¿A qué sistema(s) está funcionalmente ligado?",
        "options": ["Sistema Nervioso y Sistema Endocrino", "Sistema Límbico y Sistema Motor", "Sistema Respiratorio y Sistema Circulatorio", "Corteza Cerebral y Cerebelo"],
        "correct_index": 0,
        "rationale_correct": "¡Correcto! El Hipotálamo pertenece al Sistema Nervioso (Diencéfalo) y es el centro de control del Sistema Endocrino a través de la pituitaria.",
        "rationale_incorrect": "Incorrecto. Aunque tiene funciones límbicas, su papel como centro de control hormonal lo liga intrínsecamente al Sistema Endocrino, además del Nervioso."
    },
    {
        "question": "Una lesión en la parte posterior de la cabeza que afecta la corteza visual primaria resultaría en una alteración en la...",
        "options": ["Capacidad para formar nuevas memorias.", "Percepción e interpretación de la información visual.", "Coordinación y el equilibrio.", "Comprensión del lenguaje hablado."],
        "correct_index": 1,
        "rationale_correct": "¡Correcto! La corteza visual primaria se encuentra en el Lóbulo Occipital, lo que lo convierte en el centro principal para la interpretación de todo lo que vemos.",
        "rationale_incorrect": "Incorrecto. La corteza visual primaria en el Lóbulo Occipital está dedicada a la vista. Las otras opciones son para el Lóbulo Temporal o el Cerebelo."
    },
    {
        "question": "¿En qué región del Lóbulo Frontal se origina específicamente la señal para realizar los movimientos voluntarios del cuerpo?",
        "options": ["El Área de Broca", "La Corteza Prefrontal", "La Cisura de Silvio", "La Corteza Motora Primaria"],
        "correct_index": 3,
        "rationale_correct": "¡Correcto! La Corteza Motora Primaria, ubicada en la parte posterior del Lóbulo Frontal, es el origen del control y planificación de los movimientos corporales voluntarios.",
        "rationale_incorrect": "Incorrecto. La Corteza Motora Primaria controla el movimiento. El Área de Broca es para el habla; la Corteza Prefrontal, para la planificación."
    }
]

# --- 2. INICIALIZAR EL ESTADO DE LA SESIÓN ---
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.feedback = ""
    st.session_state.answered = False

# --- 3. CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(
    page_title="Quiz sobre las Partes del Cerebro",
    layout="centered"
)
st.title("🧠 Quiz Interactivo: Las Partes del Cerebro")

# --- 4. LÓGICA DEL CUESTIONARIO ---

# 4.1. Mostrar resultado final
if st.session_state.current_q >= len(quiz_data):
    st.header("¡Cuestionario Terminado! 🎉")
    st.metric(
        label="Puntuación Final",
        value=f"{st.session_state.score} / {len(quiz_data)} Respuestas Correctas"
    )

    if st.session_state.score == len(quiz_data):
        st.balloons()
        st.success("¡Felicidades! Tienes un conocimiento experto del cerebro.")
    elif st.session_state.score >= len(quiz_data) * 0.7:
        st.info("¡Buen trabajo! Tienes un sólido conocimiento.")
    else:
        st.warning("Puedes repasar algunas áreas. ¡Inténtalo de nuevo!")

    if st.button("Reiniciar Cuestionario"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()

# 4.2. Mostrar pregunta actual
else:
    current_index = st.session_state.current_q
    q = quiz_data[current_index]

    st.subheader(f"Pregunta {current_index + 1} de {len(quiz_data)}")
    st.write(q["question"])

    # Usar un formulario para agrupar la pregunta y el botón de envío
    with st.form(key=f'q_form_{current_index}'):
        user_choice = st.radio(
            "Selecciona tu respuesta:",
            options=q["options"],
            index=None,
            key=f'radio_{current_index}'
        )
        
        # Botón de envío
        submitted = st.form_submit_button("Responder")

    # 4.3. Lógica de retroalimentación y avance
    if submitted:
        if user_choice is None:
            st.warning("Por favor, selecciona una opción antes de responder.")
            st.stop()

        # Determinar el índice seleccionado por el usuario
        user_index = q["options"].index(user_choice)
        
        # Verificar la respuesta
        if user_index == q["correct_index"]:
            st.session_state.score += 1
            st.session_state.feedback = q["rationale_correct"]
            st.success(st.session_state.feedback)
            
            # **REQUISITO: Si se responde correctamente, pasar al siguiente item**
            st.session_state.current_q += 1
            st.session_state.answered = True # Marcar como respondido para el rerunn
        else:
            st.session_state.feedback = q["rationale_incorrect"]
            st.error(st.session_state.feedback)
            
            # Permitir al usuario avanzar a la siguiente pregunta después de un intento
            st.session_state.current_q += 1
            st.session_state.answered = True

        # Rerun para actualizar la pantalla y mostrar la siguiente pregunta o el resultado
        st.rerun()
