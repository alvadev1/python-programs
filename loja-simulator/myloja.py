class Loja:
    def __init__(self) -> None:
        self.products = {
            "computador" : 1500.00,
            "smartphone" : 1200.00,
            "headset": 200.00,
            "teclado": 100.00,
            "mouse": 70.00
        }
        self.cart = []

    def display_products(self):
        print("\nprodutos disponiveis")
        for product, value in self.products.items():
            print(f"{product} - {value}R$")

    def choice_products(self, *prods):
        for prod in prods:
            if prod in self.products.keys():
                self.cart.append({
                    "product": prod, "value": self.products[prod]
                })

    def remove_products_cart(self, *prods):
        print("\nremovendo produtos do carrinho")
        prods_cart = []

        for i in range(len(self.cart)):
            prods_cart.append(i)

        prods_cart.sort()
        for index in prods_cart[::-1]:
            if self.cart[index]["product"] in prods:
                print(f"{self.cart[index]['product']} removido do carrinho")
                self.cart.pop(index)

                
    def finalize_purchase(self):
        print("\nfinalizando compra")
        total_value = 0
        for product in self.cart:
            total_value += product["value"]
        print(f"{len(self.cart)} produtos")
        print(f"preco total de {total_value}R$")




if __name__ == "__main__":
    my_loja = Loja()
    my_loja.display_products()
    buys = ("computador", "teclado", "mouse")
    my_loja.choice_products(*buys)
    remove_cart = ("computador", "mouse")
    my_loja.remove_products_cart(*remove_cart)
    my_loja.finalize_purchase()

