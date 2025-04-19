$(document).ready(function() {
    // Функция для обновления отображения корзины
    function updateCartDisplay() {
        let cart;
        try {
            cart = JSON.parse(localStorage.getItem('cart')) || [];
        } catch (e) {
            cart = [];
        }

        if (!Array.isArray(cart)) {
            cart = [];
        }

        let cartHtml = '';

        cart.forEach(function(item, index) {
            cartHtml += `
                <li>
                    <a href="${item.url}" class="image"><img src="${item.image}" alt="Cart product Image"></a>
                    <div class="content">
                        <a href="${item.url}" class="title">${item.name}</a>
                        <span class="quantity-price">${item.quantity} x <span class="amount">${item.price}</span></span>
                        <a href="#" class="remove" data-index="${index}">×</a>
                    </div>
                </li>
            `;
        });

        $('.minicart-product-list').html(cartHtml);
        updateCartCount();
    }

    // Функция для обновления количества товаров в корзине
    function updateCartCount() {
        let cart;
        try {
            cart = JSON.parse(localStorage.getItem('cart')) || [];
        } catch (e) {
            cart = [];
        }

        if (!Array.isArray(cart)) {
            cart = [];
        }

        let totalCount = cart.reduce((sum, item) => sum + item.quantity, 0);
        let cartCountElement = $('.header-action-num');
        if (totalCount > 0) {
            cartCountElement.text(String(totalCount).padStart(2, '0')).show();
        } else {
            cartCountElement.hide();
        }
    }

    // Добавление товара в корзину
    $('.add-prod-to-cart').on('click', function() {
        let productElement = $(this).closest('.product-details-content');
        
        // Получаем количество из input.cart-plus-minus-box
        let quantity = parseInt(productElement.find('.cart-plus-minus-box').val(), 10) || 1; // Если значение невалидно, используем 1

        let product = {
            id: productElement.data('id'),
            name: productElement.data('name'),
            price: productElement.data('price'),
            image: productElement.data('image'),
            quantity: quantity, // Используем значение из input
            url: productElement.data('url')
        };

        let cart;
        try {
            cart = JSON.parse(localStorage.getItem('cart')) || [];
        } catch (e) {
            cart = [];
        }

        if (!Array.isArray(cart)) {
            cart = [];
        }

        let existingProduct = cart.find(item => item.id === product.id);

        if (existingProduct) {
            existingProduct.quantity += quantity; // Увеличиваем количество на значение из input
        } else {
            cart.push(product); // Добавляем новый товар в корзину
        }

        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartDisplay();
    });

    // Удаление товара из корзины
    $(document).on('click', '.remove', function(e) {
        e.preventDefault();
        let index = $(this).data('index');

        let cart;
        try {
            cart = JSON.parse(localStorage.getItem('cart')) || [];
        } catch (e) {
            cart = [];
        }

        if (!Array.isArray(cart)) {
            cart = [];
        }

        cart.splice(index, 1);
        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartDisplay();
    });

    $('#clear-cart').on('click', function() {
        localStorage.removeItem('cart');
        updateCartDisplay();
    });

    // Инициализация корзины при загрузке страницы
    updateCartDisplay();
});