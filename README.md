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

[Pytube](https://pytube.io/en/latest/index.html)

```sh
poetry add pytube
```

### 33. The YouTube Download Function

[Debate for the location of import statements](https://stackoverflow.com/questions/128478/should-import-statements-always-be-at-the-top-of-a-module)

## Section 8: Text Embeddings

### 41. Generating Simple Embeddings

```sh
poetry add numpy
poetry add matplotlib scikit-learn plotly pandas
poetry add scipy  # have to fix python version to ">=3.11,<3.12" in pyproject.toml
```

### 42. Finding Similarities Using Embeddings

```sh
poetry add tiktoken
```

### 48. Visualizing Embeddings

- [Nomic AI - Atlas: Visualising tool](https://docs.nomic.ai/index.html)
- [Nomic AI - Atlas: Collection of maps](https://docs.nomic.ai/collection_of_maps.html)

## Section 10: Project #7: Boost Your Linux Sysadmin Capabilities with ChatGPT (ShellGPT)

### 51. Installing and Configuring ShellGPT

[Shell-GPT](https://github.com/TheR1D/shell_gpt)

#### basic setup for pip

```sh
python3 --version
sudo apt install python3-pip
pip3 --version
sudo apt install python3-venv

mkdir ~/.shellgpt
cd shellgpt
python3 -m venv gpt_cli
source gpt_cli/bin/activate

pip3 install shell-gpt
```

#### basic setup for poetry

```sh
poetry add shell-gpt
poetry shell
```

#### use shell-gpt

```
export OPENAI_API_KEY=<MY_OPENAI_API_KEY>
env | grep OPENAI_API_KEY
# add it to ~/.zshrc or ~/bash_aliases for persistency

cat ~/.config/shell_gpt/.sgptrc

sgpt "Distance to Mars"
```

### 52. Using ShellGPT like a PRO

#### Simple Query

```sh
sgpt --help

sgpt "default location for sshd configuration file"
sgpt "default location for the key-pair used by SSH for authentication"
sgpt "command to show docker images. Answer with the command only"
```

#### Shell Query

```sh
# --execute -e is deprecated
sgpt --shell "update my system"
sgpt --shell "list all files in /var/log sorted by size"
sgpt --shell "list all files in /var/log sorted by size"
sgpt -s "create a new user called dan and add it to the sudo group"
# sudo adduser dan && sudo usermod -aG sudo dan
sgpt -s "show all open ports"
# sudo lsof -i -P -n | grep LISTEN
```

```sh
sgpt -s "create a firewall to drop all incoming ssh traffic"
# sudo ufw deny ssh
sgpt -s "create iptables rules to drop all incoming ssh traffic"
# sudo iptables -A INPUT -p tcp --dport ssh -j DROP
sgpt -s "create iptables rules to drop all incoming ssh traffic except coming from 12.45.3.5"
# sudo iptables -A INPUT -p tcp --dport ssh -s 12.45.3.5 ACCPET
# sudo iptables -A INPUT -p tcp --dport ssh -j DROP
```

#### Bash Script

```sh
sgpt --code "Bash script that prompts the user for a directory and then creates an archive of that directory. Also check that the directory exists" > backup_dir.sh
mkdir dir1
ls > dir1/a.txt
chmod +x backup_dir.sh
./backup_dir.sh
# Enter directory path: dir1
ls
# archive.tar.gz
```

### 53. The Chat Feature of ShellGPT

It remembers the context

```sh
sgpt --chat ssh --code "Python script that runs commands on a remote host using ssh" > remote_ssh.py
sgpt --chat ssh --code "remote ip=200.0.0.1 and for authentication use: user=admin, password=asdfasdfsecret, port=99" > remote_ssh_2.py
```

```sh
sgpt --chat files --shell "What are the files in /var/log?"
# ls /var/log
sgpt --chat files --shell "What are the files in /var/log?"
# ls -ilS /var/log
```

```sh
sgpt --list-chats
sgpt --show-chat ssh
```

#### Temperature

```sh
cd dir
ls > b.txt
touch c.txt
ls
# a.txt b.txt c.txt

sgpt --temperature 0 --code "bash script that renames all files in the current directory to \"current date\" + \"old name\"" > rename_files.sh
chmod +x rename_files.sh
./rename_files.sh
ls
# 2023-05-03-a.txt  2023-05-03-b.txt  2023-05-03-c.txt  2023-05-03-rename_files.sh
```

</details>
