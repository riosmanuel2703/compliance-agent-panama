import streamlit as st
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
