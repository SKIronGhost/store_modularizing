from store import Store


store_1 = Store("Store 1")
store_2 = Store("Store 2")
store_3 = Store("Store 3")
store_4 = Store("Store 4")

store_1.add_product("product 1", 500, "furniture").add_product("product 2", 250, "furniture").add_product("product 3", 15, "clothing").add_product("product 4", 60, "clothing").add_product("product 5", 800, "technology")

store_2.add_product("product 1", 500, "furniture").add_product("product 2", 250, "furniture").add_product("product 3", 15, "clothing").add_product("product 4", 60, "clothing").add_product("product 5", 800, "technology")

store_3.add_product("product 1", 500, "furniture").add_product("product 2", 250, "furniture").add_product("product 3", 15, "clothing").add_product("product 4", 60, "clothing").add_product("product 5", 800, "technology")

store_4.add_product("product 1", 500, "furniture").add_product("product 2", 250, "furniture").add_product("product 3", 15, "clothing").add_product("product 4", 60, "clothing").add_product("product 5", 800, "technology")

store_4.inflation(10)
store_3.set_clearance("furniture", 25)
# Se debe ingresar el número de código del producto
store_1.sell_product(6)

