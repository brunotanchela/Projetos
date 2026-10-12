import streamlit as st
from openai import OpenAI
import os
from datetime import datetime, time

if "nome_usuario" not in st.session_state:
    st.session_state.nome_usuario = None

if st.session_state.nome_usuario is None:
    st.title("É um prazer!")

    with st.form(key="login_form"):
        nome_digitado = st.text_input("Como podemos te chamar?")
        entrar = st.form_submit_button("Abrir chat")

        if entrar:
            if nome_digitado.strip():
                st.session_state.nome_usuario = nome_digitado.strip()
                st.rerun()
            else:
                st.error("O campo não pode ficar vazio.")

else:
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        st.error("GEMINI_API_KEY não encontrada. Verifique a env")
        st.stop()

    modelo_ia = OpenAI(api_key=api_key, base_url = "https://generativelanguage.googleapis.com/v1beta/openai")

    momento_execucao = datetime.now()
    chamada_horario = momento_execucao.time()

    if chamada_horario >= time(6, 0) and chamada_horario < time(12, 0):
        st.write(f"# Bom dia, {st.session_state.nome_usuario}.")
    elif chamada_horario >= time(12, 0) and chamada_horario < time(18, 0):
        st.write(f"# Boa tarde, {st.session_state.nome_usuario}.")
    else:
        st.write(f"# Boa noite, {st.session_state.nome_usuario}.")


    if "lista_mensagens" not in st.session_state:       # vê se não tem uma lista de mensagens já preenchida. Se já houver, ele não cria outra, gerando uma 'memória' 
        st.session_state["lista_mensagens"] = []

    mensagem_usuario = st.chat_input("O que temos para hoje?")

    for mensagem in st.session_state["lista_mensagens"]:
        quem_enviou = mensagem["role"]
        texto_mensagem = mensagem["content"]
        st.chat_message(quem_enviou).write(texto_mensagem)      # percorre a lista inteira e exibe-a por completo

    if mensagem_usuario:
        st.chat_message("user").write(mensagem_usuario)
        mensagem1 = {"role": "user", "content": mensagem_usuario}
        st.session_state["lista_mensagens"].append(mensagem1)

        resposta_modelo = modelo_ia.chat.completions.create (
            messages = st.session_state["lista_mensagens"],
            model = "gemini-flash-lite-latest"
        )
        
        resposta_ia = resposta_modelo.choices[0].message.content

        mensagem2 = {"role": "assistant", "content": resposta_ia}
        st.session_state["lista_mensagens"].append(mensagem2)
        st.chat_message("assistant").write(resposta_ia)
