# --- ENTRADA E TRATAMENTO DE DADOS ---
nome = input('Digite o nome completo do aluno: ').strip().title()

# Lemos como texto (input), trocamos vírgula por ponto e só então convertemos para float
salario_input = input('Digite o salário do responsável: R$ ').replace(',', '.')
salario = float(salario_input)

# --- GERAÇÃO DE USUÁRIO (FATIAMENTO) ---
# Pega as 4 primeiras letras do nome em minúsculas
usuario = (nome[0:4]).strip().lower()

# --- LÓGICA DE NEGÓCIO (DESCONTO) ---
if salario < 2000:
    desconto = '50%'
else:
    desconto = '10%'

# --- COLETA DE NOTAS COM ESTRUTURA DE REPETIÇÃO ---
notas = []
cont = 1
while cont <= 3:
    # Usando f-string para numerar as notas dinamicamente
    nota = float(input(f'Digite a {cont}ª nota do aluno: ').replace(',', '.'))
    notas.append(nota)
    cont += 1

# --- CÁLCULO E ORGANIZAÇÃO DOS DADOS ---
media = sum(notas) / 3

# Armazenamento estruturado em Dicionário
cadastro = {
    'Usuário': usuario, 
    'Nome': nome, 
    'Desconto': desconto,
    'Média': round(media, 2), 
    'Situação': 'Aprovado' if media >= 7 else 'Reprovado' # Condicional simplificada
}

# --- RELATÓRIO FINAL ---
print("\n========== CADASTRO CONCLUÍDO ==========")
# Iteração sobre o dicionário para exibir o resultado
for chave, valor in cadastro.items():
    print(f'{chave.upper()}: {valor}')