import os

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("nn trong", "nền trong")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed nn trong")
