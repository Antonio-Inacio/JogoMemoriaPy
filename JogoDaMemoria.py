import streamlit as st
import random
import time

# Lista de palavras aleatórias
palavras = ["banana", "livro", "carro", "gato", "caneta", "mesa", "lua", "nuvem", "ponte", "fogo"]

st.title("🧠 Desafie sua Mente!")

if "etapa" not in st.session_state:
    st.session_state.etapa = "inicio"
    st.session_state.palavras_exibidas = []
    st.session_state.resposta_usuario = []

# Início
if st.session_state.etapa == "inicio":
    if st.button("Começar desafio"):
        st.session_state.palavras_exibidas = random.sample(palavras, 5)
        st.session_state.etapa = "mostrando"
        st.rerun()

# Mostrar palavras por 5 segundos
elif st.session_state.etapa == "mostrando":
    st.write("Memorize essas palavras:")
    st.write(" | ".join(st.session_state.palavras_exibidas))
    time.sleep(5)
    st.session_state.etapa = "responder"
    st.rerun()

# Esconder e pedir resposta
elif st.session_state.etapa == "responder":
    st.write("Digite as palavras que você lembra:")
    resposta = st.text_input("Separe por vírgula (ex: gato, lua, mesa)")
    if st.button("Ver resultado"):
        digitadas = [p.strip().lower() for p in resposta.split(",")]
        corretas = set(digitadas) & set(st.session_state.palavras_exibidas)
        st.success(f"Você acertou {len(corretas)} de 5! ✅")
        st.write("Palavras corretas:", ", ".join(st.session_state.palavras_exibidas))
        st.session_state.etapa = "inicio"
