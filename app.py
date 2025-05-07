import streamlit as st

template = "A {character} in a {setting}, {style}, trending on ArtStation, ultra-detailed, 8K"
characters = ["cyberpunk samurai", "steampunk robot", "wizard", "alien cat", "futuristic knight"]
settings = ["futuristic city", "enchanted forest", "space station", "ancient temple", "digital desert"]
styles = ["cinematic", "oil painting", "anime", "photorealistic", "pixel art"]

st.title("🎨 Prompt Generator")

character = st.selectbox("Choose a character", characters)
setting = st.selectbox("Choose a setting", settings)
style = st.selectbox("Choose a style", styles)

if st.button("Generate Prompt"):
    result = template.format(character=character, setting=setting, style=style)
    st.success(result)
