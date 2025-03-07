import pandas as pd
from sqlalchemy import create_engine

# Conectar ao PostgreSQL
engine = create_engine('postgresql://postgres:Sbnova-01@localhost:5432/postgres')

# Ler o arquivo CSV (lembre-se de baixar o arquivo do Kaggle)
df = pd.read_csv('temperature_readings.csv')

# Enviar os dados para o banco PostgreSQL
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

print("✅ Dados inseridos no banco com sucesso!")

