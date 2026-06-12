import os
import re

with open('index.html', 'rb') as f:
    raw = f.read()

s = raw.decode('utf-8')

try:
    original_bytes = s.encode('cp1252')
    restored_str = original_bytes.decode('utf-8')
    print("Success with cp1252")
except Exception as e:
    print("Failed cp1252:", e)
    try:
        original_bytes = s.encode('cp1258')
        restored_str = original_bytes.decode('utf-8')
        print("Success with cp1258")
    except Exception as e2:
        print("Failed cp1258:", e2)
