# 🇵🇦 Copiloto Legal & Compliance IA - Panamá Fintech MVP

[![Streamlit App](https://static.streamlit.io/badge-svg.svg)](https://compliance-agent-panama.streamlit.app/) <!-- REEMPLAZA ESTA URL CON TU LINK DE STREAMLIT SI DESEAS -->

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
