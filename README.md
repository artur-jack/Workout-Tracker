# Sistema de Gerenciamento de Treinos

Este é um aplicativo de linha de comando para gerenciar seus treinos e exercícios.

## Funcionalidades

- Cadastro de treinos por dia da semana
- Registro de exercícios com:
  - Nome do exercício
  - Número de séries
  - Número de repetições
  - Peso atual
  - PR (Personal Record - maior peso já utilizado)
- Visualização organizada dos treinos e exercícios

## Requisitos

- Python 3.6+
- SQLAlchemy
- tabulate
- Venv

## Passos para rodar

Aqui estão os passos para rodar o projeto:

### 1. Criar e ativar ambiente virtual (venv):

```bash
python -m venv venv
source venv/bin/activate  # No Linux/Mac
```

### 2. Instalar dependências:

```bash
pip install -r requirements.txt
```

### 3. Rodar aplicação

```bash
python app.py
```

### Menu Principal

1. **Adicionar novo treino**: Permite cadastrar um novo treino e seus exercícios
2. **Visualizar treinos**: Mostra todos os treinos cadastrados e seus detalhes
3. **Sair**: Encerra o programa

## Estrutura do Banco de Dados

- O aplicativo usa SQLite como banco de dados
- Os dados são armazenados no arquivo `workouts.db`
- Duas tabelas principais:
  - `workouts`: Armazena informações dos treinos
  - `exercises`: Armazena os exercícios relacionados a cada treino
Workout Tracker
