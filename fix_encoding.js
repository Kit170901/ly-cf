const fs = require('fs');
let content = fs.readFileSync('index.html');
// The file was originally UTF-8.
// Powershell read it as Windows-1252, and then saved it as UTF-8.
// So the current bytes represent the UTF-8 encoding of the Windows-1252 decoding of the original UTF-8.
// We can reverse it: read the file as UTF-8 string. Convert string to buffer using latin1 (Windows-1252 approx). Then decode buffer as UTF-8.

let str = fs.readFileSync('index.html', 'utf8');
let buf = Buffer.from(str, 'latin1');
let restored = buf.toString('utf8');

// Apply the regex properly
restored = restored.replace(/showToast\('Đã thêm (.*?) vào giỏ demo!'\)/g, "addToCartFromCollection(this, '$1')");

// Also replace the mangled version just in case:
restored = restored.replace(/showToast\('Đã thêm (.*?) vào giỏ demo!'\)/g, "addToCartFromCollection(this, '$1')");
// Wait, the string was mangled too. The powershell script already replaced it but mangled the rest of the file.
// If the powershell script already replaced it, the string `showToast...` is gone.
// So we just need to fix the encoding.

fs.writeFileSync('index.html', restored, 'utf8');
