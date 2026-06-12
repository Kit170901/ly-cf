import os

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("addToCartFromCollection(this, '')", "addToCartFromCollection(this)")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)
