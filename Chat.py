import streamlit as st
import os
import openai

# Substitua YOUR_API_KEY_HERE pela sua chave de API real
openai.api_key = os.environ.get('api')


# Função para enviar mensagens à API GPT e obter respostas utilizando o endpoint de chat
def ask_gpt(message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0125",  # Modelo específico de chat
            messages=[
                {"role": "system", "content": "Você está conversando com um assistente inteligente."},
                {"role": "user", "content": message},
            ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"Ocorreu um erro ao processar sua solicitação: {e}"

# Verifica se o histórico já foi inicializado
if 'history' not in st.session_state:
    st.session_state['history'] = []

# CSS customizado para ajustar o tamanho das letras do cabeçalho e o tamanho dos emojis
def custom_css():
    st.markdown("""
        <style>
        h1 {
            font-size:24px !important;
        }
        .emoji {
            font-size: 1.5em;
        }
        </style>
        """, unsafe_allow_html=True)

# Aplicando o CSS customizado
custom_css()

# Interface Streamlit
st.title('🤖 IA Gedison Stein')

user_input = st.text_input("🤯 Eu:", "")

if st.button('Enviar'):
    # Obtendo a resposta do GPT
    gpt_response = ask_gpt(user_input)

    # Atualizando o histórico com a pergunta do usuário e a resposta do GPT
    st.session_state['history'].append(f"🤯 Eu: {user_input}")
    st.session_state['history'].append(f"🤖 Gedison: {gpt_response}")

# Exibindo o histórico de conversa com emojis maiores
for message in st.session_state['history']:
    # Usando st.markdown para permitir HTML customizado
    st.markdown(f'<p class="emoji">{message}</p>', unsafe_allow_html=True)


