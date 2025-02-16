$(document).ready(function() {
    // Функция для обновления отображения корзины
    function updateCartDisplay() {
        let cart = getCart();

        // Обновляем мини-корзину
        updateMiniCart(cart);

        // Обновляем таблицу на странице корзины
        updateCartTable(cart);

        // Обновляем количество товаров в корзине
        updateCartCount(cart);

        // Обновляем итоговую стоимость
        updateGrandTotal(cart);
    }

    // Функция для получения корзины из localStorage
    function getCart() {
        let cart;
        try {
            cart = JSON.parse(localStorage.getItem('cart')) || [];
        } catch (e) {
            cart = [];
        }

        if (!Array.isArray(cart)) {
            cart = [];
        }

        return cart;
    }

    // Функция для обновления мини-корзины
    function updateMiniCart(cart) {
        let cartHtml = '';

        cart.forEach(function(item, index) {
            cartHtml += `
                <li>
                    <a href="${item.url}" class="image"><img src="${item.image}" alt="Cart product Image"></a>
                    <div class="content">
                        <a href="${item.url}" class="title">${item.name}</a>
                        <span class="quantity-price">${item.quantity} x <span class="amount">${item.price} ₽</span></span>
                        <a href="#" class="remove" data-index="${index}">×</a>
                    </div>
                </li>
            `;
        });

        $('.minicart-product-list').html(cartHtml);
    }

    // Функция для обновления таблицы на странице корзины
    function updateCartTable(cart) {
        let tableHtml = '';

        cart.forEach(function(item, index) {
            tableHtml += `
                <tr>
                    <td class="product-thumbnail">
                        <a href="${item.url}"><img class="img-responsive ml-15px" src="${item.image}" alt="" /></a>
                    </td>
                    <td class="product-name"><a href="${item.url}">${item.name}</a></td>
                    <td class="product-price-cart"><span class="amount">${item.price} ₽</span></td>
                    <td class="product-quantity">
                        <div class="cart-plus-minus">
                            <div class="dec qtybutton" data-index="${index}">-</div>
                            <input class="cart-plus-minus-box" type="text" name="qtybutton" value="${item.quantity}" />
                            <div class="inc qtybutton" data-index="${index}">+</div>
                        </div>
                    </td>
                    <td class="product-subtotal">${item.quantity * parseFloat(item.price.replace('₽', ''))} ₽</td>
                    <td class="product-remove">
                        <a href="#" class="remove-from-cart" data-index="${index}"><i class="fa fa-times"></i></a>
                    </td>
                </tr>
            `;
        });

        $('.cart-table-content tbody').html(tableHtml);
    }

    // Функция для обновления количества товаров в корзине
    function updateCartCount(cart) {
        let totalCount = cart.reduce((sum, item) => sum + item.quantity, 0);
        let cartCountElement = $('.header-action-num');

        if (totalCount > 0) {
            cartCountElement.text(String(totalCount).padStart(2, '0')).show();
        } else {
            cartCountElement.hide();
        }
    }

    // Функция для обновления итоговой стоимости
    function updateGrandTotal(cart) {
        let grandTotal = cart.reduce((sum, item) => {
            let price = parseFloat(item.price.replace('₽', '').trim());
            return sum + (item.quantity * price);
        }, 0);

        // Обновляем элемент с итоговой стоимостью
        $('.grand-totall-title span').text(`${grandTotal} ₽`);
    }

    // Добавление товара в корзину
    $('.add-to-cart').on('click', function() {
        let productElement = $(this).closest('.product');
        let product = {
            id: productElement.data('id'),
            name: productElement.find('.title a').text(),
            price: productElement.find('.new').text(),
            image: productElement.find('.image img').attr('src'),
            quantity: 1,
            url: productElement.find('.title a').attr('href')
        };

        let cart = getCart();
        let existingProduct = cart.find(item => item.id === product.id);

        if (existingProduct) {
            existingProduct.quantity += 1;
        } else {
            cart.push(product);
        }

        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartDisplay();
    });

    // Удаление товара из корзины
    $(document).on('click', '.remove, .remove-from-cart', function(e) {
        e.preventDefault();
        let index = $(this).data('index');
        let cart = getCart();

        cart.splice(index, 1);
        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartDisplay();
    });

    // Очистка корзины
    $('#clear-cart, .cart-clear button').on('click', function() {
        localStorage.removeItem('cart');
        updateCartDisplay();
    });

    // Увеличение количества товара
    $(document).on('click', '.inc.qtybutton', function() {
        let index = $(this).data('index');
        let cart = getCart();

        if (cart[index]) {
            cart[index].quantity += 1;
            localStorage.setItem('cart', JSON.stringify(cart));
            updateCartDisplay();
        }
    });

    // Уменьшение количества товара
    $(document).on('click', '.dec.qtybutton', function() {
        let index = $(this).data('index');
        let cart = getCart();

        if (cart[index] && cart[index].quantity > 1) {
            cart[index].quantity -= 1;
            localStorage.setItem('cart', JSON.stringify(cart));
            updateCartDisplay();
        }
    });

    // Инициализация корзины при загрузке страницы
    updateCartDisplay();
});
