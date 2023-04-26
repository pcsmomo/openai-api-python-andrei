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

### 13. Tokens

- [OpenAI API - Tokenizer](https://platform.openai.com/tokenizer)

### 16. Prompt Engineering

````md
3. Be specific and descriptive

```py
# GOOD
user_prompt = 'Configure BGP on two routers.'

# BETTER
user_prompt = '''Configure BGP on two routers and then explain in detail each command.
1. The routers run in the same AS.
2. The AS number is 45653
3. Configure authentication using MD5 and password fddk&73}'''
```

for more example below
````

[📁 Prompt Engineering.md](./02-dive-into-openai-api/16-prompts.md)

### 17. Image Generation Using the DALL-E Model

[Image generation - OpenAI API Doc](https://platform.openai.com/docs/guides/images)

### 20. Speech Recognition With Whisper

[Speech to text - OpenAI API Doc](https://platform.openai.com/docs/guides/speech-to-text)

- [Ronald Reagan - Tear Down this Wall](http://www.historyplace.com/speeches/reagan-tear-down.htm)
  - [Ronald Reagan - Original script](./02-dive-into-openai-api/19-rr-original.txt)
  - [Ronald Reagan - Transcript](./02-dive-into-openai-api/19-rr-original.txt)
    - 100% correct

## Section 6: Project #4: YouTube Videos Summary Generator

### 32. Building a YouTube Downloader With Python

```sh
poetry add pytube
```

</details>
