
import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

# Criação da tabela "alunos"
cursor.execute('''CREATE TABLE alunos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    idade INTEGER,
                    curso TEXT
                 )''')

# Inserção de registros na tabela "alunos"
cursor.execute('''INSERT INTO alunos (nome, idade, curso) VALUES
                    ('João', 22, 'Engenharia'),
                    ('Maria', 25, 'Medicina'),
                    ('Pedro', 20, 'Direito'),
                    ('Ana', 21, 'Engenharia'),
                    ('Carlos', 19, 'Ciência da Computação')
                 ''')

# Selecionar todos os registros da tabela "alunos"
cursor.execute('SELECT * FROM alunos;')
print(cursor.fetchall())

# Selecionar o nome e a idade dos alunos com mais de 20 anos
cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20;')
print(cursor.fetchall())

# Selecionar os alunos do curso de "Engenharia" em ordem alfabética
cursor.execute('''SELECT * FROM alunos WHERE curso = 'Engenharia' ORDER BY nome;''')
print(cursor.fetchall())

# Contar o número total de alunos na tabela
cursor.execute('SELECT COUNT(*) AS total_alunos FROM alunos;')
print(cursor.fetchone()[0])

# Atualize a idade de um aluno específico na tabela
cursor.execute("UPDATE alunos SET idade = 23 WHERE nome = 'João';")

# Remova um aluno pelo seu ID
cursor.execute('DELETE FROM alunos WHERE id = 3;')

# Commit changes
conexao.commit()

# Fechar a conexão com o banco de dados
conexao.close()
