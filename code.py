import streamlit as st

# --- 1. DATOS DEL CUESTIONARIO (Los ítems generados) ---
quiz_data = [
    {
        "question": "¿Qué lóbulo cerebral es el principal responsable de las funciones ejecutivas, como la planificación y la personalidad?",
        "options": ["Lóbulo Parietal", "Lóbulo Frontal", "Lóbulo Temporal", "Lóbulo Occipital"],
        "correct_index": 1,
        "rationale_correct": "¡Correcto! El Lóbulo Frontal es la región más grande, encargada de las habilidades cognitivas de orden superior y la modulación de la conducta.",
        "rationale_incorrect": "Incorrecto. Las funciones ejecutivas son exclusivas del Lóbulo Frontal. Los otros lóbulos se centran en el procesamiento sensorial, auditivo o visual. ¡Inténtalo de nuevo!"
    },
    {
        "question": "Una persona con dificultades en el equilibrio y la coordinación fina de movimientos probablemente tiene afectado el...",
        "options": ["Tálamo", "Hipocampo", "Cerebelo", "Bulbo Raquídeo"],
        "correct_index": 2,
        "rationale_correct": "¡Correcto! El Cerebelo es fundamental para coordinar el movimiento voluntario, el equilibrio y la precisión motora.",
        "rationale_incorrect": "Incorrecto. El Cerebelo controla la coordinación y el equilibrio. Las otras estructuras tienen funciones sensoriales, de memoria o vitales. ¡Debes acertar para avanzar!"
    },
    {
        "question": "¿Cuál componente del tronco encefálico regula funciones vitales e involuntarias como la respiración y el ritmo cardíaco?",
        "options": ["Protuberancia anular", "Mesencéfalo", "Bulbo Raquídeo (Médula Oblongada)", "Hipotálamo"],
        "correct_index": 2,
        "rationale_correct": "¡Correcto! El Bulbo Raquídeo contiene centros de control autónomo esenciales para la supervivencia.",
        "rationale_incorrect": "Incorrecto. El Bulbo Raquídeo, en el tronco encefálico, es el centro de control para estas funciones vitales. ¡Sigue intentando!"
    },
    {
        "question": "La corteza auditiva primaria y el área de Wernicke (comprensión del lenguaje) se localizan predominantemente en el...",
        "options": ["Lóbulo Frontal", "Lóbulo Temporal", "Lóbulo Parietal", "Lóbulo Occipital"],
        "correct_index": 1,
        "rationale_correct": "¡Correcto! El Lóbulo Temporal está asociado con el procesamiento de la información auditiva, el lenguaje comprensivo y la memoria.",
        "rationale_incorrect": "Incorrecto. El Lóbulo Temporal (cerca de los oídos) procesa la audición y la comprensión del lenguaje. ¡Vuelve a pensarlo!"
    },
    {
        "question": "¿Qué estructura del sistema límbico es crucial para el procesamiento de las emociones, especialmente el miedo y el aprendizaje emocional?",
        "options": ["Tálamo", "Hipocampo", "Amígdala", "Cuerpo Calloso"],
        "correct_index": 2,
        "rationale_correct": "¡Correcto! La Amígdala es esencial para la detección de amenazas y la respuesta emocional intensa ('lucha o huida').",
        "rationale_incorrect": "Incorrecto. La Amígdala se encarga del procesamiento del miedo y las emociones. ¡No te rindas!"
    },
    {
        "question": "Si una persona pierde la capacidad de sentir el tacto o percibir la ubicación de sus extremidades (propiocepción), ¿qué lóbulo cerebral está afectado?",
        "options": ["Lóbulo Frontal", "Lóbulo Parietal", "Lóbulo Temporal", "Cerebelo"],
        "correct_index": 1,
        "rationale_correct": "¡Correcto! El Lóbulo Parietal contiene la corteza somatosensorial primaria, que procesa la información táctil, de temperatura, dolor y propiocepción.",
        "rationale_incorrect": "Incorrecto. El Lóbulo Parietal procesa la información somatosensorial (tacto, presión). ¡Asegúrate de elegir el lóbulo correcto!"
    },
    {
        "question": "¿Cuál es la principal función de la banda gruesa de fibras nerviosas conocida como Cuerpo Calloso?",
        "options": ["Controlar los movimientos automáticos.", "Almacenar recuerdos a largo plazo.", "Conectar los hemisferios cerebrales derecho e izquierdo.", "Filtrar la información sensorial."],
        "correct_index": 2,
        "rationale_correct": "¡Correcto! El Cuerpo Calloso es el puente más grande de sustancia blanca, permitiendo la comunicación entre los dos hemisferios cerebrales.",
        "rationale_incorrect": "Incorrecto. La función principal del Cuerpo Calloso es la comunicación inter-hemisférica. ¡Vuelve a revisar tus conocimientos!"
    },
    {
        "question": "El Hipotálamo es esencial para mantener la homeostasis (temperatura, sed, hambre) y la conexión con la glándula pituitaria. ¿A qué sistema(s) está funcionalmente ligado?",
        "options": ["Sistema Nervioso y Sistema Endocrino", "Sistema Límbico y Sistema Motor", "Sistema Respiratorio y Sistema Circulatorio", "Corteza Cerebral y Cerebelo"],
        "correct_index": 0,
        "rationale_correct": "¡Correcto! El Hipotálamo pertenece al Sistema Nervioso (Diencéfalo) y es el centro de control del Sistema Endocrino a través de la pituitaria.",
        "rationale_incorrect": "Incorrecto. Su papel como centro de control hormonal lo liga intrínsecamente al Sistema Endocrino, además del Nervioso. ¡Busca la conexión clave!"
    },
    {
        "question": "Una lesión en la parte posterior de la cabeza que afecta la corteza visual primaria resultaría en una alteración en la...",
        "options": ["Capacidad para formar nuevas memorias.", "Percepción e interpretación de la información visual.", "Coordinación y el equilibrio.", "Comprensión del lenguaje hablado."],
        "correct_index": 1,
        "rationale_correct": "¡Correcto! La corteza visual primaria se encuentra en el Lóbulo Occipital, lo que lo convierte en el centro principal para la interpretación de todo lo que vemos.",
        "rationale_incorrect": "Incorrecto. La corteza visual primaria en el Lóbulo Occipital está dedicada a la vista. ¡Piensa en la ubicación del lóbulo!"
    },
    {
        "question": "¿En qué región del Lóbulo Frontal se origina específicamente la señal para realizar los movimientos voluntarios del cuerpo?",
        "options": ["El Área de Broca", "La Corteza Prefrontal", "La Cisura de Silvio", "La Corteza Motora Primaria"],
        "correct_index": 3,
        "rationale_correct": "¡Correcto! La Corteza Motora Primaria, ubicada en la parte posterior del Lóbulo Frontal, es el origen del control y planificación de los movimientos corporales voluntarios.",
        "rationale_incorrect": "Incorrecto. La Corteza Motora Primaria controla el movimiento. El Área de Broca es para el habla; la Corteza Prefrontal, para la planificación. ¡Una vez más!"
    }
]

# --- 2. INICIALIZAR EL ESTADO DE LA SESIÓN ---
# 'current_q': Índice de la pregunta actual.
# 'score': Puntuación (número de aciertos).
# 'attempt_count': Número de intentos en la pregunta actual.
# 'feedback': Mensaje de retroalimentación.
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.feedback = ""
    st.session_state.attempt_count = 0 

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
        label="Puntuación Final (Total de Aciertos)",
        value=f"{st.session_state.score} / {len(quiz_data)}"
    )

    if st.session_state.score == len(quiz_data):
        st.balloons()
        st.success("¡Felicidades! Tienes un conocimiento experto del cerebro.")
    else:
st.info("¡Buen trabajo! Has completado el cuestionario. Puedes reiniciar para mejorar tu puntuación.")
