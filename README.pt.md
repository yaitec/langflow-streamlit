# langflow-streamlit

O `langflow-streamlit` é uma API que facilita a comunicação entre [Langflow](https://github.com/logspace-ai/langflow) e aplicações [Streamlit](https://streamlit.io/). Esta biblioteca permite uma integração perfeita das capacidades avançadas de processamento de linguagem do Langflow com a interface amigável do Streamlit, permitindo que os desenvolvedores criem aplicações interativas que aproveitam modelos de linguagem poderosos.

## Características

- **Integração fácil:** Configure rapidamente a comunicação entre Langflow e Streamlit com configuração mínima.
- **Implantação simples:** Instale e execute a API facilmente com `pip` ou `poetry`.
- **Execução flexível:** Execute a pilha completa ou apenas o frontend Streamlit com o backend da API.

## Requisitos

- Python 3.10 ou superior

## Instalação

### Opção 1: Instalar via pip

```bash
pip install langflow-streamlit
```

### Opção 2: Clonar o repositório e usar Poetry

1. Clone o repositório:
   ```bash
   git clone https://github.com/yaitec/langflow-streamlit.git
   cd langflow-streamlit
   ```

2. Instale o Poetry se ainda não o tiver:
   ```bash
   pip install poetry
   ```

3. Instale as dependências do projeto:
   ```bash
   poetry install
   ```

## Uso

### Executando a Aplicação

1. Execute a pilha completa (Langflow, API e Streamlit):
   ```bash
   langflow-streamlit run
   ```

2. Execute apenas o frontend Streamlit e o backend da API:
   ```bash
   langflow-streamlit run --streamlit-only
   ```

### Usando Poetry (após clonar o repositório)

1. Execute a pilha completa:
   ```bash
   poetry run langflow-streamlit run
   ```

2. Execute apenas o frontend Streamlit e o backend da API:
   ```bash
   poetry run langflow-streamlit run --streamlit-only
   ```

### Usando comandos Make

1. Execute a pilha completa:
   ```bash
   make start
   ```

2. Execute apenas o frontend Streamlit e o backend da API:
   ```bash
   make start-streamlit-only
   ```

## Desenvolvimento

Para configurar o ambiente de desenvolvimento:

1. Clone o repositório (se ainda não o fez).
2. Instale as dependências de desenvolvimento:
   ```bash
   poetry install --with dev
   ```

3. Execute os testes:
   ```bash
   make test
   ```

4. Verifique o estilo do código:
   ```bash
   make lint
   ```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar um Pull Request ou abrir uma Issue no repositório do GitHub.

1. Faça um fork do repositório
2. Crie sua branch de feature (`git checkout -b feature/RecursoIncrivel`)
3. Faça commit de suas mudanças (`git commit -m 'Adiciona algum RecursoIncrivel'`)
4. Faça push para a branch (`git push origin feature/RecursoIncrivel`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](./LICENSE) para detalhes.

## Contato

YAITEC - contact@yaitec.org

Link do Projeto: [https://github.com/yaitec/langflow-streamlit](https://github.com/yaitec/langflow-streamlit)
