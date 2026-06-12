import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix typo and add active class to Trang chủ
text = text.replace('<li><a href="#hero">Trang chủủ</a></li>', '<li><a href="#hero" class="active">Trang chủ</a></li>')
text = text.replace('<li><a href="#hero" class="mobile-nav-link">Trang chủủ</a></li>', '<li><a href="#hero" class="mobile-nav-link active">Trang chủ</a></li>')

# Also fix the correct ones if it was somehow "Trang chủ"
text = text.replace('<li><a href="#hero">Trang chủ</a></li>', '<li><a href="#hero" class="active">Trang chủ</a></li>')
text = text.replace('<li><a href="#hero" class="mobile-nav-link">Trang chủ</a></li>', '<li><a href="#hero" class="mobile-nav-link active">Trang chủ</a></li>')

# 2. Update CSS for nav-links a
css_old = """    .nav-links a {

      padding: 7px 13px; border-radius: 8px;

      font-size: 0.875rem; font-weight: 500;

      color: var(--brown-text);

      transition: var(--transition);

    }

    .nav-links a:hover { background: rgba(107,63,30,0.09); color: var(--coffee); }"""

css_new = """    .nav-links a {
      background: transparent !important;
      padding: 8px 12px;
      border-radius: 0;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.875rem; font-weight: 500;
      color: var(--brown-text);
      transition: var(--transition);
    }
    
    .nav-links a:hover {
      color: var(--coffee);
    }

    .nav-links a.active {
      background: transparent !important;
      color: #7A421F;
      font-weight: 700;
      position: relative;
    }

    .nav-links a.active::after {
      content: "";
      position: absolute;
      left: 12px;
      right: 12px;
      bottom: -8px;
      height: 2px;
      background: #7A421F;
      border-radius: 999px;
    }"""

# Try a regex replace because of line endings
css_old_pattern = r"\.nav-links a\s*\{.*?\}.*?\.nav-links a:hover\s*\{.*?\}"
text = re.sub(css_old_pattern, css_new, text, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Nav CSS updated.")
