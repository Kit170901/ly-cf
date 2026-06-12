import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('.preview-text-on-photo {', '.preview-text-on-photo {\n      display: none !important;')
text = text.replace('.photo-blank-mask {', '.photo-blank-mask {\n      display: none !important;')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Hided preview text and blank mask.")
