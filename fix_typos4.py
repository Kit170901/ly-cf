import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

fixes = {
    "ĐĐánh giá": "Đánh giá",
    "DĐánh giá": "Đánh giá",
    "ĐĐặt lại": "Đặt lại",
    "DĐặt lại": "Đặt lại",
    "ĐĐ": "Đ",
}

for k, v in fixes.items():
    text = text.replace(k, v)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed over-corrected typos.")
