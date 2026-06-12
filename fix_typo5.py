import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("ã thêm vào gi hàng demo!", "Đã thêm vào giỏ hàng demo!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed typo.")
