# OpenAI API with Python Bootcamp: ChatGPT API, GPT-4, DALL·E

OpenAI API with Python Bootcamp: ChatGPT API, GPT-4, DALL·E by Andrei Dumitrescu

## File Structure

# Details

<details open>
  <summary>Click to Contract/Expend</summary>

## Section 1: Getting Started

### 2. Setting Up the Environment: Jupyter Notebook and Google Colab

```sh
brew update && brew upgrade pyenv
pyenv install 3.11.3
pyenv global 3.11.3
# restart the terminal
poetry self update

python --version
# Python 3.11.3
poetry --version
# Poetry (version 1.4.2)

# using .env
poetry self add poetry-dotenv-plugin
```

```sh
poetry init
poetry add ipython jupyter
poetry shell
jupyter notebook
```

## Section 2: Deep Dive into OpenAI API: ChatGPT, GPT-4, GPT-3, DALL-E, Whisper

### 6. Installing the OpenAI API Library and Authenticating to OpenAI

```sh
poetry add openai
```

</details>
