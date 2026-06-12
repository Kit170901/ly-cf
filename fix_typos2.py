import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

fixes = {
    r'\bChn\b': 'Chọn',
    r'\bchn\b': 'chọn',
    r'sang trng': 'sang trọng',
    r'nn trắng': 'nền trắng',
    r'nn kem': 'nền kem',
    r'ha tiết': 'họa tiết',
    r'b mặt': 'bề mặt',
    r'nhu c u': 'nhu cầu',  # "nhu c u" was "nhu cầu"
    r'b T': 'bộ', # "bT sưu tập" -> "bộ sưu tập" ? Wait, "b T"
    r't y chn': 'tùy chọn', # "t A 1 y chn" ?
    r't I i u': 'tối ưu', # "t A' i u"
    r'c n th n': 'cẩn thận', # "c c n th n"
    r'ý ng a': 'ý nghĩa',
    r'qu  t ng': 'quà tặng',
    r' t  y': ' từ ',
    r' s n ': ' sẵn ',
}

for k, v in fixes.items():
    text = re.sub(k, v, text)

# Just manual fixes based on the PS output
text = text.replace('Chn kiểu ly', 'Chọn kiểu ly')
text = text.replace('chn kiểu ly', 'chọn kiểu ly')
text = text.replace('Chn phong cách', 'Chọn phong cách')
text = text.replace('Chn mẫu ly', 'Chọn mẫu ly')
text = text.replace('chn kiểu dáng', 'chọn kiểu dáng')
text = text.replace('Chn nhu cầu', 'Chọn nhu cầu')
text = text.replace('tùy chn', 'tùy chọn')
text = text.replace('tuỳ chn', 'tuỳ chọn')
text = text.replace('ha tiết', 'họa tiết')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed specific typos caused by encode drop.")
