import tiktoken
import glob

encoding = tiktoken.encoding_for_model('gpt-3.5-turbo')

total_tokens = 0

files = glob.glob('*.txt')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    tokens = encoding.encode(text)
    print(f"{file}: {len(tokens)}")
    total_tokens += len(tokens)

print(f"Total tokens: {total_tokens}")