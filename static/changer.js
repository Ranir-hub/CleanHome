function changePrice(){
    const select = document.getElementById('myselect');
    const price = document.getElementById('price');
    const priceItem = select.options[select.selectedIndex];

    price.value = priceItem.getAttribute('data-price');
}

document.addEventListener('DOMContentLoaded', function() {
    changePrice();
    document.getElementById('myselect').addEventListener('change', changePrice);
});