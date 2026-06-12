$html = Get-Content -Raw index.html
$html = $html -replace "showToast\('Đã thêm (.*?) vào giỏ demo!'\)", "addToCartFromCollection(this, `'$1`')"
Set-Content -Path index.html -Value $html -Encoding UTF8
