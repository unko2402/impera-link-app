import streamlit as st
import pandas as pd

# Datos actualizados con juegos adicionales
data = {
    "Juego": [
        "Sizzling Hot Deluxe",
        "Dolphin's Pearl Deluxe",
        "Lucky Lady's Charm Deluxe",
        "Golden Sevens",
        "Book of Ra Deluxe",
        "Lord of the Ocean",
        "Amazon Diamonds",
        "Burning Sky",
        "Explorer Book",
        "Royal Lady",
        "Golden Horus",
        "Book of Ra",
        "Little Pharaoh",
        "Cash Crown",
        "Juego del mago con conejo (nombre pendiente)"
    ],
    "RTP (%)": [
        95.66, 95.13, 95.13, 95.12, 95.10, 95.10,
        95.10, 95.00, 95.00, 95.05, 95.00, 95.10, 95.00, 95.00, 95.00
    ],
    "Volatilidad": [
        "Media", "Alta", "Alta", "Media", "Alta", "Alta",
        "Alta", "Media", "Alta", "Media", "Media", "Alta", "Media", "Alta", "Media"
    ],
    "Estrategia recomendada": [
        "Pagos frecuentes, útil para jugadores conservadores.",
        "Bonos frecuentes pero irregulares, buena para variar.",
        "Buena para apuestas medias-altas buscando bonos grandes.",
        "Frecuentes pagos pequeños, útil para sesiones largas.",
        "Ideal para apuestas altas, espera bonos ocasionales.",
        "Buena para jugadores pacientes, busca grandes premios.",
        "Volatilidad alta, útil para buscar bonos grandes esporádicos.",
        "Pagos regulares, buena para mantener saldo en sesiones medias.",
        "Similar a Book of Ra, buena para buscar rondas de bonificación.",
        "Juego balanceado, útil para sesiones moderadas.",
        "Juego clásico de estilo egipcio, adecuado para mantener el ritmo.",
        "Alta volatilidad con gran potencial de bono.",
        "Sesiones largas con premios medianos frecuentes.",
        "Potencial alto de ganancia, pero requiere paciencia.",
        "Ideal para entretenimiento con posibilidad de bono visual."
    ]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Interfaz Streamlit
st.set_page_config(page_title="Guía Impera Link", layout="centered")
st.title("🎰 Guía de Juegos - Impera Link")
st.subheader("🎯 Estrategia: Subir desde 3000 DKK al día, minimizando pérdidas")

st.markdown("""
Esta herramienta te ayuda a elegir los juegos más inteligentes dentro del sistema **Impera Link** de Novomatic.
Ideal para jugadores que quieren mantener control del bankroll y maximizar oportunidades de bono o ganancia.
""")

st.markdown("## ✅ Juegos recomendados según tu estrategia")
st.dataframe(df, use_container_width=True)

st.markdown("💡 *Consejo:* Empieza con juegos de volatilidad media, luego alterna a alta volatilidad si estás ganando para intentar un bono fuerte.")
