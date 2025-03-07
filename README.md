📡 Pipeline de Dados IoT com Docker e PostgreSQL

Este projeto processa leituras de temperatura de dispositivos IoT e exibe os dados em um dashboard interativo.

📌 Tecnologias Usadas
- Python  
- Docker  
- PostgreSQL  
- Streamlit  
- Pandas  
- Plotly  

📊 Como Rodar o Projeto

🔹 1. Clonar o Repositório
```bash
git clone https://github.com/Andest12213/pipeline-iot.git
cd pipeline-iot

🔹 2. Executar o Banco de Dados (Docker)
docker start postgres-iot

🔹 3. Rodar o Dashboard
streamlit run dashboard.py

🔹 4. Acessar no Navegador
http://localhost:8501

📈 Visão Geral
📥 Coleta de dados IoT a partir de arquivos CSV
🏗 Pipeline de processamento usando Python e Pandas
🗄 Armazenamento no PostgreSQL via Docker
📊 Visualização de dados com Streamlit e Plotly

📌 Desenvolvido por: Anderson Souza 🚀