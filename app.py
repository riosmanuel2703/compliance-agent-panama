import streamlit as st
import pandas as pd
import io
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Configuración de la Página
st.set_page_config(
    page_title="Fintech Compliance Copilot", 
    page_icon="🇵🇦", 
    layout="wide" # Cambiado a layout ancho para un look más "dashboard"
)

# 2. Palabras vacías en Español (Mejora la precisión de búsqueda de IA)
SPANISH_STOP_WORDS = [
    'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'y', 'o', 'pero', 'si', 'no',
    'de', 'del', 'al', 'a', 'en', 'con', 'por', 'para', 'como', 'su', 'sus', 'este', 'esta',
    'estos', 'estas', 'que', 'qué', 'cual', 'cuál', 'como', 'cómo', 'mi', 'mis', 'tu', 'tus'
]

# 3. Base de Datos Embebida (Resiliente)
datos_mvp = """Documento;Seccion_ID;Titulo_Seccion;Texto_Borrador_MVP;Guia_Regulatoria_Panama;Implementacion_UI_UX
1. Política de Privacidad;1.1;Responsable del Tratamiento;La plataforma digital [NOMBRE_FINTECH] es operada de forma experimental por el equipo de desarrollo. En cumplimiento con la Ley 81 de 2019 de la República de Panamá...;Requisito obligatorio de la Ley 81 de 2019. Se debe identificar claramente quién custodia la base de datos.;Enlace embebido en el modal de registro inicial.
1. Política de Privacidad;1.2;Datos Recopilados (Enfoque KYC);Para validar su acceso al piloto, recopilaremos: a) Nombre completo, b) Número de Cédula de Identidad Personal o Pasaporte, e) Datos biométricos faciales (Selfie).;El tratamiento de datos biométricos y de identificación personal en Panamá requiere consentimiento reforzado según ANTAI.;Pantalla de Onboarding durante la captura de la foto de la cédula y selfie.
1. Política de Privacidad;1.3;Derechos ARCO;Como usuario beta, usted tiene derecho a Acceder, Rectificar, Cancelar u Oponerse al uso de sus datos. Envíe una solicitud de inmediato.;Garantiza el cumplimiento de los Derechos ARCO fiscalizados por la ANTAI.;Sección 'Privacidad' dentro de la Configuración del Perfil en la App.
2. Términos y Condiciones;2.1;Declaración de Sandbox (Exención);IMPORTANTE: [NOMBRE_FINTECH] es un piloto tecnológico en fase MVP y no cuenta con una licencia bancaria de la SBP. Este entorno opera como un Sandbox simulado.;Protección crucial ante la SBP y ACODECO (Ley 45 de 2007) para evitar captación ilegal.;Pop-up de advertencia en pantalla completa ('Disclaimer') al primer inicio.
2. Términos y Condiciones;2.2;Límites Transaccionales del Piloto;Para mitigar riesgos operativos se imponen los siguientes límites inamovibles: Saldo máximo: $500 USD.;Mitiga la responsabilidad financiera y el perfil de riesgo AML/CFT ante reguladores.;Mensaje de validación interactivo en tiempo real al ingresar un monto.
4. Seguridad y Fraude;4.1;Autenticación Biométrica (2FA);Para proteger el acceso a tus fondos beta, exigimos el uso obligatorio de biometría móvil o en su defecto un código PIN de seguridad.;Alineado con el Acuerdo 007-2018 de la SBP de gestión de riesgos tecnológicos financieros.;Configuración rápida de seguridad habilitada por defecto en el primer ingreso.
5. Tarifas y Comisiones;5.1;Costo Cero MVP;Durante toda la duración del plan piloto y el challenge, el uso de la plataforma tiene un costo total de $0.00 USD.;Evita reclamos ante ACODECO sobre cobros sorpresa no contratados.;Etiqueta destacada de 'Beta - Gratis' en la sección de perfil.
"""

# Leer datos
df = pd.read_csv(io.StringIO(datos_mvp), sep=";")
df['indice_busqueda'] = (
    df['Documento'] + " " + 
    df['Titulo_Seccion'] + " " + 
    df['Texto_Borrador_MVP'] + " " + 
    df['Guia_Regulatoria_Panama']
)

# Configurar motor de IA con stopwords
vectorizer = TfidfVectorizer(stop_words=SPANISH_STOP_WORDS)
tfidf_matrix = vectorizer.fit_transform(df['indice_busqueda'])

# --- DISEÑO DE LA INTERFAZ ---

# 4. Barra Lateral (Sidebar)
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/000000/artificial-intelligence.png", width=120)
    st.header("⚙️ Panel de Control")
    st.markdown("### Piloto Fintech Panamá")
    st.info("Este copiloto utiliza **Procesamiento de Lenguaje Natural (NLP)** para cruzar tus dudas con el marco legal panameño en tiempo real.")
    
    st.subheader("📊 Datos del Piloto")
    st.metric(label="Cláusulas Mapeadas", value=len(df))
    st.metric(label="Leyes Reguladas", value="Ley 81 / SBP / ACODECO")
    
    st.markdown("---")
    st.caption("Creado para el Tech Challenge 2026. Sandbox Regulatorio Experimental.")

# 5. Cuerpo Principal (Main Layout)
st.title("🇵🇦 Copiloto Legal & Compliance IA")
st.markdown("##### Validador inteligente de términos, políticas y regulaciones para tu MVP Financiero")
st.markdown("---")

# 6. Preguntas Rápidas (Un salvavidas para que el jurado interactúe rápido)
st.write("💡 **¿No sabes qué preguntar? Prueba un clic en estas sugerencias:**")
col_sug1, col_sug2, col_sug3 = st.columns(3)

# Inicializamos el estado de la pregunta si no existe
if 'pregunta_input' not in st.session_state:
    st.session_state.pregunta_input = ""

# Acciones de los botones
if col_sug1.button("🔒 ¿Cómo se maneja la Ley 81 de datos?"):
    st.session_state.pregunta_input = "Ley 81 datos personales privacidad"
if col_sug2.button("💰 ¿Cuáles son los límites de dinero?"):
    st.session_state.pregunta_input = "límites transaccionales saldo máximo"
if col_sug3.button("⚖️ ¿Qué pasa si no tengo licencia bancaria?"):
    st.session_state.pregunta_input = "declaración de sandbox exención licencia sbp"

# 7. Cuadro de búsqueda principal
pregunta_usuario = st.text_input(
    "💬 Hazle una pregunta legal o de diseño a tu Oficial de Cumplimiento:", 
    value=st.session_state.pregunta_input,
    placeholder="Ej: ¿Necesito huella digital para entrar a la app?"
)

# 8. Procesamiento de la Consulta
if pregunta_usuario:
    pregunta_vector = vectorizer.transform([pregunta_usuario])
    similitudes = cosine_similarity(pregunta_vector, tfidf_matrix).flatten()
    idx_mas_cercano = similitudes.argsort()[-1]
    score_confianza = similitudes[idx_mas_cercano]
    
    if score_confianza < 0.1:
        st.error("🤖 **Agente:** Lo siento, no logré asociar tu pregunta con ninguna cláusula legal establecida para este piloto. Intenta reformularla.")
    else:
        row = df.iloc[idx_mas_cercano]
        
        # Formatear el indicador de confianza según el porcentaje
        if score_confianza > 0.35:
            st.success(f"🎯 **Coincidencia Alta Detectada** (Confianza: {score_confianza:.1%})")
        else:
            st.warning(f"⚠️ **Coincidencia Moderada Detectada** (Confianza: {score_confianza:.1%})")
            
        # Layout de dos columnas para presentar los datos ordenados
        col_doc, col_reg = st.columns(2)
        with col_doc:
            st.subheader("📝 Cláusula Propuesta para el MVP")
            st.info(f"**Documento:** {row['Documento']} (Sección {row['Seccion_ID']})\n\n**{row['Titulo_Seccion']}**")
            st.code(row['Texto_Borrador_MVP'], language="text")
            
        with col_reg:
            st.subheader("🇵🇦 Sustento Regulatorio en Panamá")
            st.warning(row['Guia_Regulatoria_Panama'])
            
            # Un expander interactivo para los tips de diseño UI/UX
            with st.expander("👁️ Ver sugerencia de diseño UI/UX para el App móvil", expanded=True):
                st.write(f"**Recomendación de pantalla:** \n{row['Implementacion_UI_UX']}")import streamlit as st
import pandas as pd
import io
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Configuración visual de la página
st.set_page_config(
    page_title="Oficial de Cumplimiento IA - Panamá", 
    page_icon="🇵🇦", 
    layout="centered"
)

# Encabezado principal de la app
st.title("🤖 Oficial de Cumplimiento Virtual")
st.subheader("Piloto Fintech - República de Panamá")
st.markdown("---")
st.write("Escribe tu consulta legal sobre el MVP de forma natural. El agente analizará los términos de uso y las políticas del piloto bajo el marco de la **Ley 81 de 2019 de Panamá**.")

# Base de datos embebida en el MVP
datos_mvp = """Documento;Seccion_ID;Titulo_Seccion;Texto_Borrador_MVP;Guia_Regulatoria_Panama;Implementacion_UI_UX
1. Política de Privacidad;1.1;Responsable del Tratamiento y Base Legal;La plataforma digital [NOMBRE_FINTECH] es operada de forma experimental por [RAZON_SOCIAL/EQUIPO]. En cumplimiento con la Ley 81 de 2019 de la República de Panamá...;Requisito obligatorio de la Ley 81 de 2019. Se debe identificar claramente quién custodia la base de datos.;Enlace embebido en el modal de registro inicial.
1. Política de Privacidad;1.2;Datos Recopilados (Enfoque KYC);Para validar su acceso al piloto, recopilaremos: a) Nombre completo, b) Número de Cédula de Identidad Personal o Pasaporte, c) Correo electrónico, d) Datos biométricos faciales (Selfie).;El tratamiento de datos biométricos y de identificación personal en Panamá requiere consentimiento reforzado según ANTAI.;Pantalla de Onboarding durante la captura de la foto de la cédula y selfie.
1. Política de Privacidad;1.3;Derechos ARCO y Eliminación de Datos;Como usuario beta, usted tiene derecho a Acceder, Rectificar, Cancelar u Oponerse al uso de sus datos. Envíe una solicitud a [CORREO_SOPORTE].;Garantiza el cumplimiento de los Derechos ARCO fiscalizados por la ANTAI.;Sección 'Privacidad' dentro de la Configuración del Perfil en la App.
2. Términos y Condiciones de Uso;2.1;Declaración de Sandbox / Exención de Responsabilidad;IMPORTANTE: [NOMBRE_FINTECH] es un piloto tecnológico en fase MVP y no cuenta con una licencia bancaria de la SBP. Este entorno opera como un Sandbox simulado.;Protección crucial ante la SBP y ACODECO (Ley 45 de 2007) para evitar captación ilegal.;Pop-up de advertencia en pantalla completa ('Disclaimer') al primer inicio.
2. Términos y Condiciones de Uso;2.2;Límites Transaccionales del Piloto;Para mitigar riesgos operativos se imponen los siguientes límites inamovibles: Saldo máximo: $500 USD.;Mitiga la responsabilidad financiera y el perfil de riesgo AML/CFT ante reguladores.;Mensaje de validación interactivo en tiempo real al ingresar un monto.
4. Política de Seguridad y Fraude;4.1;Autenticación Biométrica y Doble Factor (2FA);Para proteger el acceso a tus fondos beta, exigimos el uso obligatorio de biometría móvil o en su defecto un código PIN.;Alineado con el Acuerdo 007-2018 de la SBP de gestión de riesgos tecnológicos financieros.;Configuración rápida de seguridad habilitada por defecto en el primer ingreso.
5. Tarifas y Comisiones;5.1;Transparencia de Costos (Costo Cero MVP);Durante toda la duración del plan piloto y el challenge, el uso de [NOMBRE_FINTECH] tiene un costo total de $0.00 USD.;Evita reclamos ante ACODECO sobre cobros sorpresa no contratados.;Etiqueta destacada de 'Beta - Gratis' en la sección de perfil.
"""

# Inicialización y lectura del CSV virtual
df = pd.read_csv(io.StringIO(datos_mvp), sep=";")
df['indice_busqueda'] = (
    df['Documento'] + " " + 
    df['Titulo_Seccion'] + " " + 
    df['Texto_Borrador_MVP'] + " " + 
    df['Guia_Regulatoria_Panama']
)

# Ajuste del motor de búsqueda (TF-IDF)
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['indice_busqueda'])

# Input interactivo para el usuario
pregunta = st.text_input(
    "💬 Escribe tu pregunta para el Oficial de Cumplimiento:", 
    placeholder="Ej: ¿Cuáles son los límites de transacciones en la app?"
)

if pregunta:
    pregunta_vector = vectorizer.transform([pregunta])
    similitudes = cosine_similarity(pregunta_vector, tfidf_matrix).flatten()
    idx_mas_cercano = similitudes.argsort()[-1]
    score_confianza = similitudes[idx_mas_cercano]
    
    if score_confianza < 0.1:
        st.warning("🤖 **Agente:** Lo siento, no encontré cláusulas que respondan exactamente a esa pregunta en la documentación actual del piloto.")
    else:
        row = df.iloc[idx_mas_cercano]
        
        # Tarjeta de respuesta interactiva
        st.success(f"🎯 **Sección Encontrada:** {row['Titulo_Seccion']} (Confianza: {score_confianza:.1%})")
        
        # Grid para ordenar la información de forma elegante
        col1, col2 = st.columns(2)
        with col1:
            st.info(f"📁 **Documento:** {row['Documento']}")
        with col2:
            st.warning(f"⚖️ **Ley / Enfoque Panamá:** {row['Guia_Regulatoria_Panama']}")
            
        st.markdown("### 📝 Cláusula para el Usuario:")
        st.code(row['Texto_Borrador_MVP'], language="text")
        
        st.markdown("### 📱 Recomendación de Implementación UI/UX:")
        st.info(f"👉 {row['Implementacion_UI_UX']}")
