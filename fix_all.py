import os

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix Typos
replacements = {
    ">ánh giá<": ">Đánh giá<",
    "Ly Logo Thương Liệu": "Ly Logo Thương Hiệu",
    "In logo, tên quán cà phê trên sứ trắng bóng": "In logo, tên quán cà phê trên ly sứ trắng bóng",
    "nn trắng ngà": "nền trắng ngà",
    "phong cách retro sang trng": "phong cách retro sang trọng",
    "Thay đổi tuỳ chn": "Thay đổi tuỳ chọn",
    "Gói đang chn:": "Gói đang chọn:",
    "+ Chn": "+ Chọn",
    "Gi hàng đang trống.": "Giỏ hàng đang trống.",
    "Gi hàng trống!": "Giỏ hàng trống!",
    "Ly Trắng Basic Â· Minimal Â· Nâu": "Ly Trắng Basic · Minimal · Nâu",
}

for k, v in replacements.items():
    text = text.replace(k, v)

# Fix Cart JS
old_cart_js = """
  // CART STATE & LOGIC

  let cart = [];

  

  function addToCartFromCustomizer() {

    const text = document.getElementById('custom-text').value.trim() || 'Không có nội dung';

    const summary = document.getElementById('preview-summary').innerText;

    const price = 250000;

    const img = document.getElementById('preview-photo-img').src;

    

    addItemToCart({

      id: Date.now(),

      title: 'Ly gốm thiết kế theo yêu cầu',

      desc: summary + (text !== 'Không có nội dung' ? ` - In: "${text}"` : ''),

      price: price,

      qty: 1,

      img: img

    });

    

    const success = document.getElementById('cart-success');

    success.style.display = 'block';

    setTimeout(() => success.style.display = 'none', 3000);

    toggleCart(); // Open cart to show user

  }

  function addToCartFromCollection(btn) {

    const card = btn.closest('.product-card');

    const name = card.querySelector('.product-name').innerText;

    const imgPath = card.querySelector('img').src;

    const priceText = card.querySelector('.product-price').innerText;

    const price = parseInt(priceText.replace(/\D/g, ''));

    

    addItemToCart({

      id: Date.now(),

      title: name,

      desc: 'Mẫu thiết kế có sẵn',

      price: price,

      qty: 1,

      img: imgPath

    });

    toggleCart(); // Open cart to show user

  }

  function addItemToCart(item) {

    const existing = cart.find(i => i.title === item.title && i.desc === item.desc);

    if(existing) {

      existing.qty += 1;

    } else {

      cart.push(item);

    }

    renderCart();

  }

  function updateQuantity(id, delta) {

    const item = cart.find(i => i.id === id);

    if(item) {

      item.qty += delta;

      if(item.qty <= 0) {

        cart = cart.filter(i => i.id !== id);

      }

      renderCart();

    }

  }

  function renderCart() {

    const body = document.getElementById('cart-body');

    const totalEl = document.getElementById('cart-total-price');

    const badge = document.getElementById('nav-cart-badge');

    

    let totalQty = 0;

    let totalPrice = 0;

    

    if(cart.length === 0) {

      body.innerHTML = '<div class="cart-empty">Giỏ hàng đang trống.</div>';

    } else {

      body.innerHTML = cart.map(item => {

        totalQty += item.qty;

        totalPrice += item.price * item.qty;

        return `

          <div class="cart-item">

            <img src="${item.img}" alt="${item.title}">

            <div class="cart-item-details">

              <div class="cart-item-title">${item.title}</div>

              <div class="cart-item-desc">${item.desc}</div>

              <div class="cart-item-price">${(item.price).toLocaleString('vi-VN')}₫</div>

              <div class="cart-qty-ctrl">

                <button class="cart-qty-btn" onclick="updateQuantity(${item.id}, -1)">-</button>

                <span style="font-size:0.9rem;font-weight:600;">${item.qty}</span>

                <button class="cart-qty-btn" onclick="updateQuantity(${item.id}, 1)">+</button>

                <div class="cart-item-remove" onclick="updateQuantity(${item.id}, -${item.qty})">Xoá</div>

              </div>

            </div>

          </div>

        `;

      }).join('');

    }

    

    badge.innerText = totalQty;

    totalEl.innerText = totalPrice.toLocaleString('vi-VN') + '₫';

  }
"""

new_cart_js = """
  // CART STATE & LOGIC
  let cart = [];

  function generateId(str) {
    return btoa(encodeURIComponent(str)).substring(0, 10);
  }

  function addToCartFromCustomizer() {
    const text = document.getElementById('custom-text').value.trim() || 'Không có nội dung';
    const summary = document.getElementById('preview-summary').textContent;
    const price = 250000;
    const image = document.getElementById('preview-photo-img').src;
    const name = 'Ly gốm thiết kế theo yêu cầu';
    const desc = summary + (text !== 'Không có nội dung' ? ` - In: "${text}"` : '');
    const id = generateId(name + desc);
    
    addToCart({ id, name, price, image, desc });
    
    const success = document.getElementById('cart-success');
    success.style.display = 'block';
    setTimeout(() => success.style.display = 'none', 3000);
    toggleCart();
  }

  function addToCartFromCollection(btn) {
    const card = btn.closest('.product-card');
    const name = card.querySelector('.product-name').textContent.trim() || 'Sản phẩm gốm sứ';
    const image = card.querySelector('img').src;
    const priceText = card.querySelector('.product-price').textContent;
    const price = parseInt(priceText.replace(/\D/g, '')) || 0;
    const desc = 'Mẫu thiết kế có sẵn';
    const id = generateId(name + desc);
    
    addToCart({ id, name, price, image, desc });
    toggleCart();
  }

  function addToCart(product) {
    const existing = cart.find(item => item.id === product.id);
    if (existing) {
      existing.quantity += 1;
    } else {
      cart.push({
        id: product.id,
        name: product.name,
        desc: product.desc,
        price: product.price,
        image: product.image,
        quantity: 1
      });
    }
    renderCart();
  }

  function updateQuantity(id, delta) {
    const item = cart.find(i => i.id === id);
    if(item) {
      item.quantity += delta;
      if(item.quantity <= 0) {
        cart = cart.filter(i => i.id !== id);
      }
      renderCart();
    }
  }

  function removeItem(id) {
    cart = cart.filter(i => i.id !== id);
    renderCart();
  }

  function renderCart() {
    const body = document.getElementById('cart-body');
    const totalEl = document.getElementById('cart-total-price');
    const badge = document.getElementById('nav-cart-badge');
    
    if(cart.length === 0) {
      body.innerHTML = '<div class="cart-empty">Giỏ hàng đang trống.</div>';
      badge.textContent = 0;
      totalEl.textContent = '0₫';
      return;
    } 

    body.innerHTML = cart.map(item => `
      <div class="cart-item">
        <img src="${item.image}" alt="${item.name}">
        <div class="cart-item-details">
          <div class="cart-item-title">${item.name}</div>
          <div class="cart-item-desc">${item.desc}</div>
          <div class="cart-item-price">${(item.price).toLocaleString('vi-VN')}₫</div>
          <div class="cart-qty-ctrl">
            <button class="cart-qty-btn" onclick="updateQuantity('${item.id}', -1)">-</button>
            <span style="font-size:0.9rem;font-weight:600;">${item.quantity}</span>
            <button class="cart-qty-btn" onclick="updateQuantity('${item.id}', 1)">+</button>
            <div class="cart-item-remove" onclick="removeItem('${item.id}')">Xoá</div>
          </div>
        </div>
      </div>
    `).join('');
    
    const totalQty = cart.reduce((sum, item) => sum + item.quantity, 0);
    const totalPrice = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
    
    badge.textContent = totalQty;
    totalEl.textContent = totalPrice.toLocaleString('vi-VN') + '₫';
  }
"""

# We need to replace the old cart js cleanly. Since line endings vary, let's use regex.
import re
start_marker = "// CART STATE & LOGIC"
end_marker = "function toggleCart()"
match = re.search(re.escape(start_marker) + r".*?(?=" + re.escape(end_marker) + ")", text, re.DOTALL)
if match:
    text = text[:match.start()] + new_cart_js + "\n  " + text[match.end():]
else:
    print("Could not find cart JS block!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied fixes.")
