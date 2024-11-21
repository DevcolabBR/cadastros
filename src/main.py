import os
import sqlite3

# Define the path for the database file
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, 'data')
db_path = os.path.join(data_dir, 'clientes.db')

# Create the data directory if it doesn't exist
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create the clientes table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    nascimento TEXT,
    genero TEXT,
    estado_civil TEXT,
    profissao TEXT,
    telefone TEXT,
    cidade TEXT,
    CEP TEXT,
    estado TEXT,
    rua TEXT,
    bairro TEXT,
    pontos_fidelidade INTEGER DEFAULT 0
)
''')

# Function to add a new client
def add_cliente(nome, nascimento, genero, estado_civil, profissao, telefone, cidade, cep, estado, rua, bairro):
    cursor.execute('''
    INSERT INTO clientes (nome, nascimento, genero, estado_civil, profissao, telefone, cidade, cep, estado, rua, bairro) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nome, nascimento, genero, estado_civil, profissao, telefone, cidade, cep, estado, rua, bairro))
    conn.commit()

# Example usage
if __name__ == "__main__":
    nome = input("Digite o nome do cliente: ")
    nascimento = input("Digite a data de nascimento do cliente: ")
    genero = input("Digite o gênero do cliente: ")
    estado_civil = input("Digite o estado civil do cliente: ")
    profissao = input("Digite a profissão do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    cep = input("Digite o CEP do cliente: ")
    estado = input("Digite o estado do cliente: ")
    cidade = input("Digite a cidade do cliente: ")
    rua = input("Digite o endereço do cliente: ")
    bairro = input("Digite o bairro do cliente: ")
    numero_endereco = input("Digite o número do endereço do cliente: ")
   
    add_cliente(nome, nascimento, genero, estado_civil, profissao, telefone, cidade, cep, estado, rua, bairro)
    print("Cliente cadastrado com sucesso!")

# Close the connection
conn.close()