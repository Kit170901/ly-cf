import os
import re

with open('index.html', 'rb') as f:
    raw = f.read()

s = raw.decode('utf-8').lstrip('\ufeff')

try:
    original_bytes = s.encode('cp1252')
    restored_str = original_bytes.decode('utf-8')
    print("Success with cp1252")
except Exception as e:
    print("Failed cp1252:", e)
    try:
        # Fallback dictionary for common powershell encoding corruptions if encode fails
        # Actually let's try replacing chars that can't be encoded
        original_bytes = s.encode('cp1252', errors='ignore')
        restored_str = original_bytes.decode('utf-8', errors='ignore')
        print("Success with cp1252 ignore")
    except Exception as e2:
        print("Failed cp1258:", e2)

# Re-apply the regex correctly
restored_str = re.sub(r"showToast\('Đã thêm (.*?) vào giỏ demo!'\)", r"addToCartFromCollection(this, '\1')", restored_str)
# also try to replace the mangled version
restored_str = re.sub(r"showToast\('Ä áº£ thÃªm (.*?) vÃ o giá» demo!'\)", r"addToCartFromCollection(this, '\1')", restored_str)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(restored_str)

print("Fixed encoding.")
