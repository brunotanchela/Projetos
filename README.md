# 🐍 Projetos em Python

![Status](https://img.shields.io/badge/status-em%20constru%C3%A7%C3%A3o-orange)
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-DataFrame-150458?logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Visualização-3F4F75?logo=plotly&logoColor=white)

## 📌 Sobre este repositório

Coleção dos meus projetos de estudo em **Python**, com foco em **análise de dados**, **automação**, **aplicações web com Streamlit**, **machine learning** e **integração com IA generativa**. Parte dos projetos foi desenvolvida como prática de cursos e evoluída com melhorias próprias, além de projetos individuais independentes.

O repositório é um **monorepo**: cada projeto vive em sua própria pasta, com seus dados e dependências, e com um README próprio explicando objetivo, tecnologias e como executar.

## 🗂️ Organização

```
Projetos/
├── AnaliseDados/       # Análise exploratória de dados (Jupyter)
├── ChatbotIA/          # Chatbot com Streamlit + Gemini
├── MachineLearning/    # Modelos de machine learning
├── PythonPowerup/      # Automação de tarefas com Python
├── SistemaProfessor/   # Aplicação de gestão para professores
├── SistemaVendas/      # Sistema de gestão vendas com dashboard
└── README.md
```

Agrupar tudo em um único repositório facilita a **navegação** e a **organização**: um só lugar para acompanhar a evolução dos estudos, com cada pasta independente.

## 📚 Projetos

| Projeto | Descrição | Tecnologias | Status |
|---|---|---|---|
| [🤖 ChatbotIA](./ChatbotIA) | Chatbot com histórico de conversa, tela de identificação e saudação por horário, consumindo o modelo Gemini | Streamlit, OpenAI SDK, Gemini API | ✅ Publicado |
| 📉 AnaliseDados | Análise de cancelamento de clientes para identificar as causas mais relevantes | Pandas, Plotly, Jupyter | 🔜 Em breve |
| 🧠 MachineLearning | Projeto de machine learning com bases de clientes e novos clientes | Python, Jupyter | 🔜 Em breve |
| ⚙️ PythonPowerup | Automação do cadastro de produtos em um sistema web a partir de uma planilha | PyAutoGUI, Pandas | 🔜 Em breve |
| 🎓 SistemaProfessor | Aplicação para gerenciar alunos, turmas, notas e mensagens | Python, Streamlit e + | 🔜 Em breve |
| 🛒 SistemaVendas | Cadastro de vendas com dashboard de faturamento por vendedor e produto | Streamlit, Pandas, Plotly | 🔜 Em breve |

## 🛠️ Tecnologias em comum

- **Python** — linguagem principal de todos os projetos
- **Pandas** — leitura, limpeza e persistência de dados em CSV
- **Plotly** — gráficos interativos
- **Streamlit** — interfaces web sem necessidade de HTML/CSS
- **Jupyter Notebook** — análises exploratórias e experimentos
_Poderá haver implementações ao longo do desenvolvimento conforme a evolução dos projetos_

## ⚙️ Como executar um projeto

Cada projeto tem suas próprias dependências. O fluxo geral é o mesmo para todos:

```bash
# Clone o repositório
git clone https://github.com/brunotanchela/Projetos.git
cd Projetos

# (Opcional) Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# Instale as dependências do projeto escolhido
pip install -r NomeDoProjeto/requirements.txt

# Rode (apps Streamlit)
streamlit run NomeDoProjeto/arquivo.py
```

> 💡 Os comandos exatos de cada projeto, incluindo configurações extras (como a chave de API do **ChatbotIA**), estão no README da respectiva pasta.

## 🎯 Objetivos

- Consolidar os fundamentos de Python em projetos práticos para mim
- Treinar o ciclo completo: dados, lógica, interface e documentação
- Construir um portfólio organizado e reproduzível

## 👤 Autor

**Bruno Tanchela** — [GitHub](https://github.com/brunotanchela)

## 📄 Licença

Uso livre para fins educacionais — repositório de prática e estudos, sem restrições de uso.