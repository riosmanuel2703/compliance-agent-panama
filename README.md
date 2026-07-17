# 🇵🇦 El "Fren" Legal de tu MVP - Copiloto de Compliance con IA 

[![Streamlit App](https://static.streamlit.io/badge-svg.svg)](https://compliance-agent-panama.streamlit.app/) <!-- REEMPLAZA ESTO CON EL ENLACE REAL DE TU APP -->

¿Qué xopá, friend? Este es un copiloto inteligente y automatizado hecho especialmente para los desarrolladores y diseñadores de Fintechs aquí en el patio (Panamá). 

Usando **Procesamiento de Lenguaje Natural (NLP)** del bueno, este agente te cruza en un dos por tres las dudas de tu código y tus pantallas con las leyes panameñas para que no te caiga la teja de la **Ley 81 de Protección de Datos**, las reglas de la **SBP** (Superintendencia de Bancos) o las multas de **ACODECO**.

---

## 📝 ¿De qué va esta ponchera? (Descripción)

Armar una Fintech en Panamá es buco trabajo y uno quiere tirar código rápido pa' lanzar el MVP "en bomba". Pero ¡ayala vida!, de repente te acuerdas de que hay que cumplir con un montón de leyes y te da dolor de cabeza de solo pensarlo. 

Este copiloto es como tener a un **Oficial de Cumplimiento metido en tu chat de WhatsApp**. Le preguntas cualquier duda sobre tus pantallas, registro (KYC) o límites de plata y de una vez te suelta:
1. El borrador legal masticadito para que lo copies y pegues en tus Términos y Condiciones.
2. Quién es el ente que te puede joder si lo haces mal (**ANTAI, SBP o ACODECO**).
3. El tip de diseño para que la pantalla de tu app móvil quede bien yeyo (interfaz limpia y transparente).

---

## 📐 ¿Cómo corre este invento? (Arquitectura)

Esta herramienta no gasta plata en APIs raras de afuera ni se queda pensando media hora. Es más rápida que un diablo rojo en hora pico (te responde en menos de 100ms) porque usa pura matemática local.

```text
 ┌───────────────────────┐
 │   Pregunta del Fren   │ ── (¿Qué xopá con esto?)
 └───────────────────────┘
             │
             ▼
 ┌───────────────────────┐
 │   Filtro de "Plena"   │ ── (Limpiamos el palabrerío con TF-IDF)
 └───────────────────────┘
             │
             ▼
 ┌───────────────────────┐      ┌───────────────────────────────┐
 │   Buscador de Rabo    │ ◄─── │  La Base de Datos del MVP     │
 │      de Ojo           │      │   (Las leyes panameñas)       │
 │  (Cosine Similarity)  │      └───────────────────────────────┘
 └───────────────────────┘
             │
             ▼
 ┌───────────────────────┐
 │  ¿Tiene sentido?      │ ── (Filtro de Confianza > 5%)
 └───────────────────────┘
             │
             ▼
 ┌──────────────────────────────────────────────────────────────┐
 │                    La Pantalla de Streamlit                  │
 │  - Pestaña 1: El copy legal masticadito y listo pa' pegar.   │
 │  - Pestaña 2: Quién te puede joder (ANTAI, SBP, ACODECO).    │
 │  - Pestaña 3: Cómo poner la pantalla bien 'yeyo' (UI/UX).    │
 └──────────────────────────────────────────────────────────────┘


 Los Juguetes que Usamos (Tecnologías)
Para armar esta belleza nos fuimos por lo seguro, usando herramientas Open Source profesionales que pesan poco y resuelven rápido:

1.Python 3.9+: El cerebro de la operación, el que manda en la casa y mueve toda la lógica del backend.

2.Streamlit: Para montar la página web interactiva en un dos por tres, sin tener que sufrir tirando HTML o CSS complicado. ¡Rápido, limpio y responsive!

3.Scikit-learn (TF-IDF Vectorizer): La biblioteca que le da el toque científico al asunto. Convierte las palabras de tu pregunta en números (vectores) ignorando las palabras "puente" como de, para, con para entender la esencia de lo que buscas.

4.Cosine Similarity (Similitud de Coseno): El algoritmo matemático que mide el ángulo entre lo que tú preguntas y lo que dicen los documentos legales. Si el ángulo es casi idéntico, ¡pum!, tenemos un match.

5.Pandas: Para ordenar los datos del MVP como si fuera una tabla de Excel bien pulida pero con superpoderes de búsqueda.

6.Streamlit Community Cloud: La nube donde dejamos corriendo el sistema las 24 horas del día para que las mentes brillantes de aluralatam lo pruebe gratis cuando quiera.

🎯 Qué locuras le puedes preguntar al Copiloto (Ejemplos)
El bot está activo para responder las preguntas sugeridas del menú o lo que le escribas en lenguaje natural:

¿Cómo nos chifiamos una multa con la Ley 81 si pedimos datos?

¿Hasta cuánta plata puede mover un usuario en la cuenta antes de que la SBP nos caiga encima?

¿Qué disclaimer hay que meter obligao para que la gente sepa que esto es un sandbox y no un banco real?

¿Podemos cobrar comisión en el piloto o ACODECO nos va a mandar a los inspectores?

¿Es obligatorio meter selfie o huella para que no nos metan goles con cuentas falsas?

Un ejemplo de cómo responde el Oficial de Cumplimiento
Cuando le pegas una buena pregunta, el bot se activa y te desglosa todo en tres pestañas bien organizadas:

1. El borrador legal (Pa' copiar y pegar de una)
Lo que debes poner en los términos y condiciones:
"Para validar su acceso al piloto, recopilaremos: a) Nombre completo, b) Número de Cédula o Pasaporte, e) Selfie biométrico."

2. La bajada de ley (El sustento legal sin rodeos)
⚠️ Ponte serio:
"Ojo: Si vas a pedir selfies (biometría), la ANTAI te exige que el usuario acepte con un botón bien grande y claro. No te pongas a inventar."

3. El truco de diseño (Para que la app quede bonita)
📱 Cómo ponerlo en el App:
"No seas bulto, no pidas la selfie al final del registro. Pon una pantalla limpia al inicio explicando por qué necesitas su foto antes de que la cámara se active de la nada."
