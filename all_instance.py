from all_class import *

S = System()

S.create_user("Mr.", "Racha", "Tungtrakool", "", "0882932676","")   #user test          ->   username = ''  pass = ''


S.create_admin("12", "12")                                              #create admin

pizza_catalog = Catalog()
drink_catalog = Catalog()

S.add_catalog(pizza_catalog)
S.add_catalog(drink_catalog)


pizza1 = S.admin.create_pizza_product("ROSA GRANDE LIL' RONI CUPS", [390, 650], "ROSA.png")
pizza2 = S.admin.create_pizza_product("KINDNESS PEPPERONI", [285, 490], "KINDNESS.png")
pizza3 = S.admin.create_pizza_product("CLASSIC CHEESE", [285, 490], "CLASSIC.png")
pizza4 = S.admin.create_pizza_product("PEPPERONI", [385, 620], "PEPPERONI.png")
pizza5 = S.admin.create_pizza_product("SEAFOOD DELUXE", [430, 715], "SEAFOOD.png")
pizza6 = S.admin.create_pizza_product("HAM & MUSHROOM", [365, 610], "HAM & MUSHROOM.png")
pizza7 = S.admin.create_pizza_product("HAWAIIAN", [350, 585], "HAWAIIAN.png")
pizza8 = S.admin.create_pizza_product("SUPREME", [410, 685], "SUPREME.png")
pizza9 = S.admin.create_pizza_product("BBQ CHICKEN", [390, 655], "BBQ CHICKEN.png")

drink1 = S.admin.create_drink_product("COKE - 325 ML", [45], "COKE.png")
drink2 = S.admin.create_drink_product("COKE LIGHT - 325 ML", [45], "COKE_LIGHT.png")
drink3 = S.admin.create_drink_product("COKE ZERO NO SUGAR - 325ML", [45], "COKE_ZERO.png")
drink4 = S.admin.create_drink_product("COKE BOTTLE - 1.25L", [80],"COKE_BOTTLE.png")
drink5 = S.admin.create_drink_product("SINGLECUT WEIRD AND GILLY NEIPA - 473ML", [250], "SINGLECUT_WEIRD.png")
drink6 = S.admin.create_drink_product("NIGHT SHIFT WHIRLPOOL NEW ENGLAND PALE ALE", [235], "NIGHT SHIFT WHIRLPOOL NEW ENGLAND PALE ALE.png")
drink7 = S.admin.create_drink_product("KNEE DEEP DEEP HAZE IPA - 355ML", [200], "KNEE DEEP DEEP HAZE IPA - 355ML.png")
drink8 = S.admin.create_drink_product("KNEE DEEP DEEP CLARITY WEST COAST IPA - 355ML", [200],"KNEE DEEP DEEP CLARITY WEST COAST IPA - 355ML.png")
drink9 = S.admin.create_drink_product("REVISION PLAYAFICATION NEIPA - 473ML", [295], "REVISION PLAYAFICATION NEIPA - 473ML.png")


#     for test  admin add pizza      "FOUR CHEESE"       [395, 655]         "FOUR CHEESE.png"

#     for test  admin add drink      "PUSHERS PEACHY SPARKLING TEA - 230ML"             [85]           [PUSHERS PEACHY SPARKLING TEA - 230ML.png] 

    
pizza_catalog.add_item_to_list(pizza1)
pizza_catalog.add_item_to_list(pizza2)
pizza_catalog.add_item_to_list(pizza3)
pizza_catalog.add_item_to_list(pizza4)
pizza_catalog.add_item_to_list(pizza5)
pizza_catalog.add_item_to_list(pizza6)
pizza_catalog.add_item_to_list(pizza7)
pizza_catalog.add_item_to_list(pizza8)
pizza_catalog.add_item_to_list(pizza9)

drink_catalog.add_item_to_list(drink1)
drink_catalog.add_item_to_list(drink2)
drink_catalog.add_item_to_list(drink3)
drink_catalog.add_item_to_list(drink4)
drink_catalog.add_item_to_list(drink5)
drink_catalog.add_item_to_list(drink6)
drink_catalog.add_item_to_list(drink7)
drink_catalog.add_item_to_list(drink8)
drink_catalog.add_item_to_list(drink9)













