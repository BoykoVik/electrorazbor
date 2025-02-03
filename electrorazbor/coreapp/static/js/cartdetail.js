$(document).ready(function() {
    // Функция для обновления отображения корзины
    function updateCartDisplay() {
        // Получаем корзину из localStorage или создаем пустой массив, если данных нет
        let cart;
        try {
            cart = JSON.parse(localStorage.getItem('cart')) || [];
        } catch (e) {
            // Если данные в localStorage повреждены, создаем пустой массив
            cart = [];
        }

        // Проверяем, что cart является массивом
        if (!Array.isArray(cart)) {
            cart = [];
        }

        let cartHtml = '';

        // Перебираем товары в корзине и формируем HTML
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

        // Вставляем сформированный HTML в контейнер корзины
        $('.minicart-product-list').html(cartHtml);

        // Обновляем количество товаров в корзине
        updateCartCount();
    }

    // Функция для обновления количества товаров в корзине
    function updateCartCount() {
        // Получаем корзину из localStorage или создаем пустой массив, если данных нет
        let cart;
        try {
            cart = JSON.parse(localStorage.getItem('cart')) || [];
        } catch (e) {
            // Если данные в localStorage повреждены, создаем пустой массив
            cart = [];
        }

        // Проверяем, что cart является массивом
        if (!Array.isArray(cart)) {
            cart = [];
        }

        // Считаем общее количество товаров в корзине
        let totalCount = cart.reduce((sum, item) => sum + item.quantity, 0);

        // Обновляем значение элемента <span class="header-action-num">
        $('.header-action-num').text(String(totalCount).padStart(2, '0'));
    }

    // Добавление товара в корзину с главной страницы
    $('.add-to-cart').on('click', function() {
        let productElement = $(this).closest('.product');
        let product = {
            id: productElement.data('id'), // Получаем ID товара
            name: productElement.find('.title a').text(),
            price: productElement.find('.new').text(),
            image: productElement.find('.image img').attr('src'),
            quantity: 1,
            url: productElement.find('.title a').attr('href')
        };

        // Получаем корзину из localStorage или создаем пустой массив, если данных нет
        let cart;
        try {
            cart = JSON.parse(localStorage.getItem('cart')) || [];
        } catch (e) {
            // Если данные в localStorage повреждены, создаем пустой массив
            cart = [];
        }

        // Проверяем, что cart является массивом
        if (!Array.isArray(cart)) {
            cart = [];
        }

        // Проверяем, есть ли товар в корзине
        let existingProduct = cart.find(item => item.id === product.id);

        if (existingProduct) {
            existingProduct.quantity += 1; // Увеличиваем количество, если товар уже в корзине
        } else {
            cart.push(product); // Добавляем новый товар в корзину
        }

        // Сохраняем обновленную корзину в localStorage
        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartDisplay();
    });

    // Добавление товара в корзину со страницы деталей товара
    $('.add-cart').on('click', function() {
        let productElement = $(this).closest('.product-details-content');
        let quantity = parseInt(productElement.find('.cart-plus-minus-box').val(), 10);

        let product = {
            id: productElement.data('id'), // Получаем ID товара
            name: productElement.find('h2').text(),
            price: productElement.find('.new-price').text(),
            image: productElement.find('.swiper-slide img').attr('src'),
            quantity: quantity,
            url: window.location.href
        };

        // Получаем корзину из localStorage или создаем пустой массив, если данных нет
        let cart;
        try {
            cart = JSON.parse(localStorage.getItem('cart')) || [];
        } catch (e) {
            // Если данные в localStorage повреждены, создаем пустой массив
            cart = [];
        }

        // Проверяем, что cart является массивом
        if (!Array.isArray(cart)) {
            cart = [];
        }

        // Проверяем, есть ли товар в корзине
        let existingProduct = cart.find(item => item.id === product.id);

        if (existingProduct) {
            existingProduct.quantity += quantity; // Увеличиваем количество, если товар уже в корзине
        } else {
            cart.push(product); // Добавляем новый товар в корзину
        }

        // Сохраняем обновленную корзину в localStorage
        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartDisplay();
    });

    // Удаление товара из корзины
    $(document).on('click', '.remove', function(e) {
        e.preventDefault();
        let index = $(this).data('index');

        // Получаем корзину из localStorage или создаем пустой массив, если данных нет
        let cart;
        try {
            cart = JSON.parse(localStorage.getItem('cart')) || [];
        } catch (e) {
            // Если данные в localStorage повреждены, создаем пустой массив
            cart = [];
        }

        // Проверяем, что cart является массивом
        if (!Array.isArray(cart)) {
            cart = [];
        }

        // Удаляем товар по индексу
        cart.splice(index, 1);

        // Сохраняем обновленную корзину в localStorage
        localStorage.setItem('cart', JSON.stringify(cart));
        updateCartDisplay();
    });

    $('#clear-cart').on('click', function() {
        // Удаляем корзину из localStorage
        localStorage.removeItem('cart');
        // Обновляем отображение корзины
        updateCartDisplay();
    });

    // Инициализация корзины при загрузке страницы
    updateCartDisplay();
});