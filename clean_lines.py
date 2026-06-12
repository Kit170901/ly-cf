import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Normalize line endings
text = text.replace('\r\n', '\n').replace('\r', '\n')

# Collapse multiple blank lines into a single blank line
text = re.sub(r'\n\n+', '\n\n', text)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Cleaned up blank lines.")
