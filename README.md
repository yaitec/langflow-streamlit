# Langflow Streamlit Integration

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [How to run](#how-to-run)
4. [Starter Projects](#starter-projects)
   1. [How to get Streamlit's Flows from the store](#how-to-get-streamlits-flows-from-the-store)
   2. [Using Streamlit Components in Langflow](#using-streamlit-components-in-langflow)
   3. [Streamlit Components](#streamlit-components)
5. [Contributing](#contributing)
6. [License](#license)
7. [Contact](#contact)

## Introduction
`langflow-streamlit` is a powerful API that bridges the gap between [Langflow](https://github.com/logspace-ai/langflow) and [Streamlit](https://streamlit.io/) applications. This library seamlessly integrates Langflow's advanced language processing capabilities with Streamlit's user-friendly interface, enabling developers to create interactive applications that harness the power of sophisticated language models.

**Important:** To use this library effectively, you need to set up a Langflow Store Key. This key allows you to access and use flows and components from the Langflow Store. For more information on setting up your Langflow Store Key, please refer to the [Langflow documentation](https://docs.langflow.org/configuration-api-keys).

## Features

- **Seamless Integration:** Effortlessly establish communication between Langflow and Streamlit with minimal configuration.
- **Streamlined Deployment:** Quickly install and run the API using either `pip` or `poetry`.
- **Flexible Execution Options:** Choose to run the full stack (Langflow + Streamlit API) or just the Streamlit backend with API.
- **Langflow Store Integration:** Access and utilize pre-built flows and Streamlit components from the Langflow Store to enhance your applications.

## Requirements

- Python 3.10 or higher
## Installation

### Option 1: Install via pip

```bash
python3 -m venv env
source env/bin/activate
pip install langflow-streamlit==0.1.8a1
```

### Option 2: Clone the repository and use Poetry

1. Clone the repository:
   ```bash
   git clone https://github.com/yaitec/langflow-streamlit.git
   cd langflow-streamlit
   ```

2. Install Poetry if you haven't already:
   ```bash
   pip install poetry
   ```

3. Install the project dependencies:
   ```bash
   poetry install
   ```

### How to run

<details>
<summary>If choose <a href="#option-1-install-via-pip">pip installation</a> option</summary>

1. Run the full stack (Langflow, API, and Streamlit):
   ```bash
   python -m langflow-streamlit run
   ```

2. Run only the Streamlit backend and API:
   ```bash
   python -m langflow-streamlit run --streamlit-only
   ```
</details>

<details>
<summary>If choose <a href="#option-2-clone-the-repository-and-use-poetry">clone the repository</a> option</summary>

1. Run the full stack (Langflow, API, and Streamlit):
   ```bash
   make start
   ```

2. Run only the Streamlit backend and API:
   ```bash
   make start-streamlit-only
   ```
</details>
<br/>

**Note:** Running only the Streamlit backend is useful when you want to use Langflow-created flows in your Streamlit application without running the full Langflow instance.

#### How to open each aplication(after running the project)

- `Streamlit chat` should be running on default port 5001 and click [here](http://localhost:5001) to access in your browser.
- `Streamlit API` should be running on default port 7881 and click [here](http://localhost:7881/docs) to access it's docs in your browser.
- `Langflow` should be running on default port 7860 and click [here](http://localhost:7860) to access in your browser.

---

## Starter Projects

###  How to get Streamlit's Flows from the store

The gif below shows how to search, download, and run Streamlit's flow:

<p align="center">
  <img src="./docs/static/streamlit_how_to_get_flows.gif" alt="Your GIF" style="border: 3px solid #211C43;">
</p>


### Using Streamlit Components in Langflow

The gif below shows how to use `Listen` and `Send` components:

<p align="center">
  <img src="./docs/static/streamlit_how_to_connect_components.gif" alt="Your GIF" style="border: 3px solid #211C43;">
</p>


### Streamlit Components

Langflow provides pre-built Streamlit components that can be accessed through the Langflow store. These components enhance your Streamlit applications with powerful functionality:

- **[Send](./send.md)**: Send messages to a Streamlit chat session.
- **[Listen](./listen.md)**: Listen for incoming messages in a Streamlit chat, dynamically altering the layout of the Streamlit application.

To use these components:
1. Access the Langflow store within your Langflow instance.
2. Search for and download the desired Streamlit component.
3. Integrate the component into your Langflow workflow.
4. Connect the component to your Streamlit application using the `langflow-streamlit` API.

For detailed instructions on using Streamlit components, refer to the [Usage](#usage) section below.

---

## Environment Variables

| Variable       | Description                                                   | Default |
|----------------|---------------------------------------------------------------|---------|
| STREAMLIT_ONLY | If True, runs only Streamlit and Streamlit API; else, runs Langflow too | False   |
| LOG_LEVEL | Defines log level of library | "info" |
| LOG_FILE_GENERATION | If True, creates a langflow-streamlit.log file for debug purpose and override LOG_LEVEL to 'debug' | False |

### Setting Environment Variables
You can learn how to set environment variables for each alternative bellow, click in the arrow that correlated to installation option that you choosed and check how to setup it properly.

<details>
<summary>If choose <a href="#option-1-install-via-pip">pip installation</a> option</summary>
these are the options that you can set:

   ```bash
   langflow-streamlit --streamlit-only --log-level error --log-file-generation
   ```
</details>
<details>
<summary>If choose <a href="#option-2-clone-the-repository-and-use-poetry">clone the repository</a> option</summary>

- Setting it in zsh or bash

   ```bash
   export STREAMLIT_ONLY=True LOG_LEVEL=debug LOG_FILE_GENERATION=True
   ```

- Setting it in PowerShell

   ```powershell
   $env:STREAMLIT_ONLY = "True"
   $env:LOG_LEVEL = "debug"
   $env:LOG_FILE_GENERATION = "True"
   ```

</details> 

### Using Poetry (after cloning the repository)

1. Run the full stack:
   ```bash
   poetry run langflow-streamlit run
   ```

2. Run only the Streamlit frontend and API backend:
   ```bash
   poetry run langflow-streamlit run --streamlit-only
   ```

### Using Make Commands

1. Run the full stack:
   ```bash
   make start
   ```

2. Run only the Streamlit frontend and API backend:
   ```bash
   make start-streamlit-only
   ```
3. Check the other available commands:
   ```bash
   make help
   ```

## Development

To set up the development environment:

1. Clone the repository (if you haven't already).
2. Enter inside the cloned repository directory.
   ```bash
   cd <repository_path>
   ```
2. Install development dependencies:
   ```bash
   poetry install --with dev
   ```

3. Run tests:
   ```bash
   make test
   ```

4. Check code style:
   ```bash
   make lint
   ```

## Contributing

We welcome contributions! Please feel free to submit a Pull Request or open an Issue on the GitHub repository.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Contact

YAITEC - contact@yaitec.org

Project Link: [https://github.com/yaitec/langflow-streamlit](https://github.com/yaitec/langflow-streamlit)

