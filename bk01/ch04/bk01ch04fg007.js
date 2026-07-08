export function calculateTotal(itemsInCart) {
  return itemsInCart.reduce((total, item) => total + item.price * item.quantity, 0);
}
