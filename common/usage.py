def print_token_usage(response):
    # "·Token usage: 36 = 33 + 3 (prompt + completion)"
    print(f"·Token usage: {response['usage']['total_tokens']} = {response['usage']['prompt_tokens']} + {response['usage']['completion_tokens']} (prompt + completion)")