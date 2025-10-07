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
        "options": ["Lóbulo Frontal", "Lóbulo Parietal", "Lóbulo Temporal", "Cerebelo
