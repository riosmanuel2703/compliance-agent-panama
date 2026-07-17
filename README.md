# 🇵🇦 Copiloto Legal & Compliance IA - Panamá Fintech MVP

[![Streamlit App](https://static.streamlit.io/badge-svg.svg)](https://compliance-agent-panama-8ccdrmvzebff9ln6hgxrhm.streamlit.app/)

Un copiloto inteligente y automatizado diseñado para equipos de desarrollo Fintech en la República de Panamá. Utilizando **Procesamiento de Lenguaje Natural (NLP)**, este agente cruza de manera instantánea las dudas de desarrollo y diseño de un MVP financiero con el marco regulatorio panameño (**Ley 81 de 2019 de Protección de Datos, regulaciones de la SBP y lineamientos de ACODECO**).

---

## 📝 Descripción General

El desarrollo de soluciones Fintech ágiles suele colisionar con la complejidad de la regulación financiera y de datos en Panamá. Este Copiloto actúa como un **Oficial de Cumplimiento Virtual** embebido en el ciclo de vida del MVP. 

Permite a los desarrolladores y diseñadores de producto consultar de forma conversacional si sus políticas, límites transaccionales, métodos de registro (KYC) y flujos de pantallas cumplen con las normativas panameñas vigentes, ofreciendo simultáneamente:
1. El borrador legal preciso para los Términos y Condiciones.
2. El sustento regulatorio en Panamá.
3. La recomendación interactiva de diseño UI/UX para la interfaz de usuario.

---

## 📐 Arquitectura de la Solución

El agente utiliza un enfoque ágil y altamente eficiente de **Recuperación de Información Basada en Semántica** sin depender de APIs externas costosas o pesadas, asegurando tiempos de respuesta menores a 100ms.

```text
 ┌───────────────────────┐
 │   Consulta Usuario    │ ── (Pregunta Frecuente o Texto Libre)
 └───────────────────────┘
             │
             ▼
 ┌───────────────────────┐
 │   TF-IDF Vectorizer   │ ── (Filtrado de Stop Words en Español)
 └───────────────────────┘
             │
             ▼
 ┌───────────────────────┐      ┌───────────────────────────────┐
 │  Cosine Similarity    │ ◄─── │ Base de Datos del MVP (CSV)   │
 └───────────────────────┘      └───────────────────────────────┘
             │
             ▼
 ┌───────────────────────┐
 │   Selección de Nodo   │ ── (Filtro por Umbral de Confianza > 5%)
 └───────────────────────┘
             │
             ▼
 ┌──────────────────────────────────────────────────────────────┐
 │                    Interfaz Streamlit UI                     │
 │  - Pestaña 1: Cláusula sugerida en formato Markdown.         │
 │  - Pestaña 2: Base legal panameña asociada (ANTAI, SBP, etc.)│
 │  - Pestaña 3: Recomendaciones funcionales de UI/UX.          │
 └──────────────────────────────────────────────────────────────┘

---

🛠️ Tecnologías y Herramientas Utilizadas
Lenguaje de Programación: Python 3.9+

Interfaz Gráfica: Streamlit (Para un Dashboard interactivo, responsivo y ágil).

Procesamiento de Lenguaje Natural (NLP): Scikit-learn (Modelado y vectorización de texto con TF-IDF).

Cálculo Matemático: Cosine Similarity (Para medir la cercanía semántica entre la duda del usuario y la base regulatoria).

Manipulación de Datos: Pandas (Estructuración de datos en DataFrame).

Despliegue: Streamlit Community Cloud.

---
❓ Ejemplos de Preguntas que el Agente Puede Responder
El copiloto está configurado para responder tanto a preguntas sugeridas como a preguntas abiertas formuladas en lenguaje natural:

¿Cómo protegemos la privacidad de los usuarios bajo la Ley 81 de Panamá?

¿Cuáles son los límites de transacciones y saldo de dinero en las cuentas beta?

¿Qué exención de responsabilidad debemos mostrar al usuario por no tener una licencia bancaria de la SBP?

¿Cómo se maneja el cobro de comisiones y tarifas en la fase del MVP financiero?

¿Qué medidas de seguridad y biometría se aplican para prevenir fraudes en los accesos?

🎯 Ejemplos de Respuestas Generadas por el Agente
Cuando se realiza una consulta exitosa, el agente estructura la respuesta de forma interactiva en tres secciones clave:

1. Borrador de la Cláusula Legal
Cláusula sugerida para colocar en el modal de registro de usuario:
"Para validar su acceso al piloto, recopilaremos: a) Nombre completo, b) Número de Cédula de Identidad Personal o Pasaporte, e) Datos biométricos faciales (Selfie)."

2. Sustento de Cumplimiento (Regulación de Panamá)
⚠️ Sustento Legal:
"El tratamiento de datos biométricos y de identificación personal en Panamá requiere un consentimiento explícito y reforzado por parte del usuario, fiscalizado bajo la autoridad de la ANTAI."

3. Experiencia de Usuario (Diseño UI/UX Recomendado)
📱 Implementación en la App:
"Se debe habilitar una pantalla de Onboarding específica y dedicada durante el flujo de registro, justo en el momento exacto en el que el usuario va a capturar la foto de su cédula y selfie, informando el propósito de la captura."

