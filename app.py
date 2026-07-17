import streamlit as st
import pandas as pd
import io
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Configuración de la Página
st.set_page_config(
    page_title="Oficial de Cumplimiento IA - Panamá", 
    page_icon="🇵🇦", 
    layout="wide"
)

# 2. Palabras vacías en Español (Mejora la precisión del motor de IA)
SPANISH_STOP_WORDS = [
    'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'y', 'o', 'pero', 'si', 'no',
    'de', 'del', 'al', 'a', 'en', 'con', 'por', 'para', 'como', 'su', 'sus', 'este', 'esta',
    'estos', 'estas', 'que', 'qué', 'cual', 'cuál', 'como', 'cómo', 'mi', 'mis', 'tu', 'tus'
]

# 3. Base de Datos del MVP
datos_mvp = """Documento;Seccion_ID;Titulo_Seccion;Texto_Borrador_MVP;Guia_Regulatoria_Panama;Implementacion_UI_UX
1. Política de Privacidad;1.1;Responsable del Tratamiento;La plataforma digital [NOMBRE_FINTECH] es operada de forma experimental por el equipo de desarrollo. En cumplimiento con la Ley 81 de 2019 de la República de Panamá...;Requisito obligatorio de la Ley 81 de 2019. Se debe identificar claramente quién custodia la base de datos.;Enlace embebido en el modal de registro inicial.
1. Política de Privacidad;1.2;Datos Recopilados (Enfoque KYC);Para validar su acceso al piloto, recopilaremos: a) Nombre completo, b) Número de Cédula de Identidad Personal o Pasaporte, e) Datos biométricos faciales (Selfie).;El tratamiento de datos biométricos y de identificación personal en Panamá requiere consentimiento reforzado según ANTAI.;Pantalla de Onboarding durante la captura de la foto de la cédula y selfie.
1. Política de Privacidad;1.3;Derechos ARCO;Como usuario beta, usted tiene derecho a Acceder, Rectificar, Cancelar u Oponerse al uso de sus datos. Envíe una solicitud de inmediato.;Garantiza el cumplimiento de los Derechos ARCO fiscalizados por la ANTAI.;Sección 'Privacidad' dentro de la Configuración del Perfil en la App.
2. Términos y Condiciones;2.1;Declaración de Sandbox (Exención);IMPORTANTE: [NOMBRE_FINTECH] es un piloto tecnológico en fase MVP y no cuenta con una licencia bancaria de la SBP. Este entorno opera como un Sandbox simulado.;Protección crucial ante la SBP y ACODECO (Ley 45 de 2007) para evitar captación ilegal.;Pop-up de advertencia en pantalla completa ('Disclaimer') al primer inicio.
2. Términos y Condiciones;2.2;Límites Transaccionales del Piloto;Para mitigar riesgos operativos se imponen los siguientes límites inamovibles: Saldo máximo: $500 USD.;Mitiga la responsabilidad financiera y el perfil de riesgo AML/CFT ante reguladores.;Mensaje de validación interactivo en tiempo real al ingresar un monto.
4. Seguridad y Fraude;4.1;Autenticación Biométrica (2FA);Para proteger el acceso a tus fondos beta, exigimos el uso obligatorio de biometría móvil o en su defecto un código PIN de seguridad.;Alineado con el Acuerdo 007-2018 de la SBP de gestión de riesgos tecnológicos financieros.;Configuración rápida de seguridad habilitada por defecto en el primer ingreso.
5. Tarifas y Comisiones;5.1;Costo Cero MVP;Durante toda la duración del plan piloto y el challenge, el uso de la plataforma tiene un costo total de $0.00 USD.;Evita reclamos ante ACODECO sobre cobros sorpresa no contratados.;Etiqueta destacada de 'Beta - Gratis' en la sección de perfil.
"""

# Cargar base de datos
df = pd.read_csv(io.StringIO(datos_mvp), sep=";")
df['indice_busqueda'] = (
    df['Documento'] + " " + 
    df['Titulo_Seccion'] + " " + 
    df['Texto_Borrador_MVP'] + " " + 
    df['Guia_Regulatoria_Panama']
)

# Inicializar IA
vectorizer = TfidfVectorizer(stop_words=SPANISH_STOP_WORDS)
tfidf_matrix = vectorizer.fit_transform(df['indice_busqueda'])

# --- INTERFAZ GRÁFICA ---

# Panel Lateral
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/000000/artificial-intelligence.png", width=120)
    st.header("⚙️ Panel de Control")
    st.markdown("### Piloto Fintech Panamá")
    st.info("Este copiloto utiliza Procesamiento de Lenguaje Natural (NLP) para cruzar tus dudas con el marco legal panameño.")
    st.subheader("📊 Datos del Piloto")
    st.metric(label="Cláusulas Mapeadas", value=len(df))
    st.metric(label="Leyes Reguladas", value="Ley 81 / SBP / ACODECO")
    st.markdown("---")
    st.caption("Creado para el Tech Challenge 2026.")

# Cuerpo Principal
st.title("🇵🇦 Copiloto Legal & Compliance IA")
st.markdown("##### Validador inteligente de términos, políticas y regulaciones para tu MVP Financiero")
st.markdown("---")

# Selección de modalidad de pregunta (¡Mucho más estable y profesional!)
metodo_consulta = st.radio(
    "Selecciona cómo deseas consultar al Oficial de Cumplimiento:",
    ["💡 Elegir una pregunta frecuente (Recomendado para el Jurado)", "✍️ Escribir mi propia pregunta libre"]
)

pregunta_final = ""

if metodo_consulta == "💡 Elegir una pregunta frecuente (Recomendado para el Jurado)":
    opcion_seleccionada = st.selectbox(
        "Haz clic abajo y elige una duda regulatoria común para ver cómo responde la IA:",
        [
            "¿Cómo protegemos la privacidad de los usuarios bajo la Ley 81 de Panamá?",
            "¿Cuáles son los límites de transacciones y saldo de dinero en las cuentas?",
            "¿Qué exención de responsabilidad mostramos por no tener licencia de la SBP?",
            "¿Cómo se maneja el cobro de comisiones y tarifas en el plan piloto?",
            "¿Qué medidas de seguridad y biometría se aplican para evitar fraudes?"
        ]
    )
    # Mapeo simple para la búsqueda semántica
    mapeo_preguntas = {
        "¿Cómo protegemos la privacidad de los usuarios bajo la Ley 81 de Panamá?": "Ley 81 datos personales privacidad ARCO",
        "¿Cuáles son los límites de transacciones y saldo de dinero en las cuentas?": "límites transaccionales saldo máximo fondos",
        "¿Qué exención de responsabilidad mostramos por no tener licencia de la SBP?": "sandbox exención de responsabilidad licencia bancaria sbp",
        "¿Cómo se maneja el cobro de comisiones y tarifas en el plan piloto?": "tarifas comisiones costo cero gratis acodeco",
        "¿Qué medidas de seguridad y biometría se aplican para evitar fraudes?": "seguridad fraude biometría código pin doble factor"
    }
    pregunta_final = mapeo_preguntas[opcion_seleccionada]
else:
    pregunta_final = st.text_input(
        "Escribe tu pregunta legal aquí:", 
        placeholder="Ej: ¿Necesito selfie o cédula para crear la cuenta?"
    )

# Procesar la búsqueda si hay una pregunta activa
if pregunta_final:
    pregunta_vector = vectorizer.transform([pregunta_final])
    similitudes = cosine_similarity(pregunta_vector, tfidf_matrix).flatten()
    idx_mas_cercano = similitudes.argsort()[-1]
    score_confianza = similitudes[idx_mas_cercano]
    
    if score_confianza < 0.05:
        st.error("🤖 **Agente:** Lo siento, no encontré cláusulas relacionadas con tu pregunta en el borrador del MVP.")
    else:
        row = df.iloc[idx_mas_cercano]
        
        if score_confianza > 0.25:
            st.success(f"🎯 **Cláusula Localizada con Éxito** (Precisión del motor de búsqueda: {score_confianza:.1%})")
        else:
            st.warning(f"⚠️ **Coincidencia Parcial Detectada** (Precisión: {score_confianza:.1%})")
            
        col_doc, col_reg = st.columns(2)
        with col_doc:
            st.subheader("📝 Cláusula Propuesta para el MVP")
            st.info(f"**Documento:** {row['Documento']} (Sección {row['Seccion_ID']})\n\n**{row['Titulo_Seccion']}**")
            st.code(row['Texto_Borrador_MVP'], language="text")
            
        with col_reg:
            st.subheader("🇵🇦 Sustento Regulatorio en Panamá")
            st.warning(row['Guia_Regulatoria_Panama'])
            
            with st.expander("👁️ Ver sugerencia de diseño UI/UX para el App móvil", expanded=True):
                st.write(f"👉 {row['Implementacion_UI_UX']}")
