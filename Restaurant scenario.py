class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def calculate_total_price(self, quantity=1):
        return self.price * quantity


class ColombianFood(MenuItem):
    def __init__(self, name, price, typical_ingredients):
        super().__init__(name, price)
        self.typical_ingredients = typical_ingredients


class BandejaPaisa(ColombianFood):
    def __init__(self):
        super().__init__("Bandeja Paisa", 25000, ["Carne asada", "Chicharrón", "Arroz", "Frijoles", "Aguacate", "Huevo", "Plátano maduro", "Arepa"])


class Ajiaco(ColombianFood):
    def __init__(self):
        super().__init__("Ajiaco", 18000, ["Pollo", "Papa criolla", "Mazorca", "Guascas", "Cilantro", "Crema de leche", "Aguacate"])


class Empanadas(ColombianFood):
    def __init__(self):
        super().__init__("Empanadas", 2000, ["Carne molida", "Papa", "Cebolla", "Aji", "Cilantro"])


class Arepas(ColombianFood):
    def __init__(self):
        super().__init__("Arepas", 3000, ["Harina de maíz", "Queso", "Mantequilla"])


class Lechona(ColombianFood):
    def __init__(self):
        super().__init__("Lechona", 35000, ["Cerdo", "Arroz", "Arvejas", "Cebolla", "Ajo", "Comino"])


class AjiGuacamole(ColombianFood):
    def __init__(self):
        super().__init__("Aji guacamole", 5000, ["Aguacate", "Tomate", "Cebolla", "Cilantro", "Aji"])


class Sancocho(ColombianFood):
    def __init__(self):
        super().__init__("Sancocho", 20000, ["Pollo", "Yuca", "Plátano", "Mazorca", "Cilantro", "Arroz"])


class Tamales(ColombianFood):
    def __init__(self):
        super().__init__("Tamales", 5000, ["Masa de maíz", "Pollo", "Cerdo", "Zanahoria", "Cebolla", "Huevo", "Aceituna", "Arroz"])


class Sudado(ColombianFood):
    def __init__(self):
        super().__init__("Sudado de pollo", 18000, ["Pollo", "Tomate", "Cebolla", "Cilantro", "Arroz"])


class AjiacoSantafereño(ColombianFood):
    def __init__(self):
        super().__init__("Ajiaco Santafereño", 20000, ["Pollo", "Papa criolla", "Mazorca", "Guascas", "Cilantro", "Crema de leche", "Aguacate"])


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity=1):
        self.items.append((item, quantity))

    def calculate_total_bill(self):
        total_bill = 0
        for item, quantity in self.items:
            total_bill += item.calculate_total_price(quantity)
        return total_bill

    def apply_discount(self, discount_percentage):
        total_bill = self.calculate_total_bill()
        if len(self.items) >= 3:
            discount_amount = total_bill * (discount_percentage / 100)
            total_bill -= discount_amount
        return total_bill


# Create an order
order = Order()

# Add 10 Colombian dishes to the order
order.add_item(BandejaPaisa(), 2)
order.add_item(Ajiaco())
order.add_item(Empanadas(), 3)
order.add_item(Arepas(), 5)
order.add_item(Lechona())
order.add_item(AjiGuacamole())
order.add_item(Sancocho())
order.add_item(Tamales(), 2)
order.add_item(Sudado())
order.add_item(AjiacoSantafereño())

# Calculate the total bill
total_bill_before_discount = order.calculate_total_bill()
total_bill_after_discount = order.apply_discount(15)
print("Total bill before discount:", total_bill_before_discount)
print("Total bill after 15% discount:", total_bill_after_discount)
