# 🤖 Chatbot com Streamlit + Gemini

![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![OpenAI SDK](https://img.shields.io/badge/OpenAI%20SDK-compatível-412991?logo=openai&logoColor=white)
![Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?logo=google&logoColor=white)

## 📌 Sobre o projeto

Chatbot simples construído com **Streamlit**, consumindo o modelo **Gemini Flash Lite** (com camada gratuita, sujeita a limites de uso) através da **SDK da OpenAI** (compatibilidade de API). O projeto foi desenvolvido como prática da **Aula 03 da Jornada Python Programação (Hashtag Treinamentos)**, focando em APIs de IA generativa e construção de interfaces interativas.

## 🎯 Objetivo

- Praticar integração com APIs de LLM usando a interface da OpenAI SDK
- Implementar um chat com **histórico de mensagens**
- Personalizar a experiência com **tela de identificação** e **saudação por horário**
- Construir uma interface web funcional com Streamlit, sem necessidade de HTML/CSS

## 🛠️ Tecnologias utilizadas

- **Python 3.12**
- **Streamlit** — interface web e gerenciamento de estado (`session_state`)
- **OpenAI SDK** — cliente usado para consumir o endpoint compatível do Gemini
- **Google Gemini API** (`gemini-flash-lite-latest`) — modelo de linguagem

## 📂 Estrutura do projeto

```
Projetos/
└── ChatbotIA/
    ├── chatbot.py          # Código principal da aplicação
    ├── requirements.txt    # Dependências do projeto
    └── README.md
```

## ⚙️ Como executar

```bash
# Clone o repositório
git clone https://github.com/brunotanchela/Projetos.git
cd Projetos

# Instale as dependências
pip install -r ChatbotIA/requirements.txt
```

### 🔑 Configurando a API Key

Para que o código rode, você precisa de uma chave de API (única para cada pessoa). Gere a sua em [Google AI Studio](https://aistudio.google.com/apikey) e defina-a como variável de ambiente **no mesmo terminal em que vai rodar a aplicação**:

```bash
# Linux/macOS
export GEMINI_API_KEY="sua_chave_aqui"

# Windows (PowerShell)
$env:GEMINI_API_KEY="sua_chave_aqui"

# Windows (CMD, sem aspas)
set GEMINI_API_KEY=sua_chave_aqui
```

> ⚠️ A variável vale apenas para o terminal atual: ao fechá-lo, é preciso defini-la novamente. Nunca escreva a chave diretamente no código nem a envie ao GitHub.

### ▶️ Rodando a aplicação

```bash
streamlit run ChatbotIA/chatbot.py
```

> 💡 O programa foi feito com Gemini Flash Lite. Para usar outro modelo ou provedor, altere o `base_url` e o `model` no código.

## 🧠 Como funciona

1. **Identificação** — ao abrir o app, o usuário informa seu nome em um formulário (`st.form`). O nome fica guardado em `st.session_state`, e o app recarrega (`st.rerun()`) para exibir o chat.
2. **Saudação** — o título exibe "Bom dia", "Boa tarde" ou "Boa noite" de acordo com o horário da máquina que executa o app.
3. **Validação da chave** — se `GEMINI_API_KEY` não estiver definida, o app mostra uma mensagem de erro e interrompe a execução (`st.stop()`).
4. **Histórico** — as mensagens ficam em `st.session_state["lista_mensagens"]`, para que a conversa não se perca a cada interação do Streamlit (que recarrega o script inteiro a cada evento).
5. **Contexto** — a cada mensagem enviada, ela é adicionada ao histórico e reenviada **junto com todo o contexto anterior** ao modelo, permitindo respostas coerentes com a conversa. A resposta da IA também é salva no histórico.

## Melhorias futuras

- [ ] Adicionar tratamento de erros (ex: falha na chamada à API, key inválida)
- [ ] Botão para limpar o histórico de conversa

## 👤 Autor

**Bruno Tanchela** — [GitHub](https://github.com/brunotanchela)

## 📄 Licença

Uso livre para fins educacionais — projeto de prática de curso (Jornada Python, Hashtag), sem restrições de uso.