## Set the system role

```py
system_role_content = 'You are a helpful assistant.'
# Note: the "{you input text here}" is a placeholder for actual text/context.
```

## Recommnedations:

1. Use the latest model.

2. Put the instructions at the beginning of the prompt, on their own line, and separate the instructions from the context .

```py
# GOOD
user_prompt = '''Translate the text below from English to Korean.

{Prompt engineering is a new discipline for developing and optimizing prompts \
to efficiently use language models (LMs) for a wide variety of applications and research topics.}
'''
```

3. Be specific and descriptive

```py
# GOOD
user_prompt = 'Configure BGP on two routers.'

# BETTER
user_prompt = '''Configure BGP on two routers and then explain in detail each command.
{1. The routers run in the same AS.
2. The AS number is 45653
3. Configure authentication using MD5 and password fddk&73}'''
```

4. Start with zero-shot, if the results are not optimal,

**fine-tune by providing a couple of examples.**

```py
# BETTER
user_prompt = '''Extract keywords from the below text.

Text 1: OpenAI has trained cutting-edge language models that are very good at understanding and generating text.\
Our API provides access to these models and can be used to solve virtually any task\
that involves processing language.
Keywords 1: OpenAI, models, text processing, API.

Text 2: {Python is an interpreted, object-oriented, high-level programming language with \
dynamic semantics. Its high-level built in data structures, combined with dynamic \
typing and dynamic binding, make it very attractive for Rapid Application Development, \
as well as for use as a scripting or glue language to connect existing components together. \
Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost \
of program maintenance.}
Keywords 2:'''
```

5. Reduse "fluffy" and imprecise descriptions

```py
# NOT SO GOOD
user_prompt = '''The description for the product below should be fairly short, a few sentences
only and not too much more.

Product:{Rubik's Cube}'''

# #BETTER
user_prompt = '''Write a description of 3 to 5 sentences for the product below.

Product:{Rubik's Cube}'''
```

6. Don't say what not to do, say what to do instead

```py
# GOOD
user_prompt = '''The following is a conversation between an Agent and a Customer\
DO NOT ASK FOR USERNAME OR PASSWORD. DO NOT REPEAT.

Customer: I can't log into my account.
Agent:'''

# BETTER
user_prompt = '''The following is a conversation between an Agent and a Customer\
The agent will attempt to diagnose the problem and suggest a solution, without asking\
any questions related to the username and password.
Instead of asking for credentials, refer the user to the help article at www.company/help

Customer: I can't log into my account.
Agent:'''
```

7. Give hints

```py
# NOT SO GOOD
user_prompt = '''Write a simple function that:
1. Asks the user for the temperature in F
2. Converts the temperature to C'''


# BETTER
user_prompt = '''Write a simple function that:
1. Asks the user for the temperature in F
2. Converts the temperature to C

import ...'''
```
