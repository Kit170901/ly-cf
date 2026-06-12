import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

fixes = {
    r'\bánh giá\b': 'Đánh giá',
    r'>ánh giá<': '>Đánh giá<',
    r'Ha tiết': 'Họa tiết',
    r'ha tiết': 'họa tiết',
    r'gio demo': 'giỏ demo',
    r'gi demo': 'giỏ demo', # Just in case it was "gi demo"
    r'ặt lại': 'Đặt lại',
    r'Chn': 'Chọn',
    r'chn': 'chọn',
    r'Trang ch': 'Trang chủ', # if "ủ" was dropped
}

for k, v in fixes.items():
    text = re.sub(k, v, text)

# Let's also do exact string replacements
exact_fixes = {
    "ánh giá": "Đánh giá",
    "Ha tiết trang trí": "Họa tiết trang trí",
    "gio demo": "giỏ demo",
    "ặt lại": "Đặt lại"
}

for k, v in exact_fixes.items():
    text = text.replace(k, v)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed more typos.")
