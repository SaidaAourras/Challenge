import association_produit_prix

products_prix = association_produit_prix.dic_product_prix


def prix_sup_30(element):
    if int(element[1]) >= 30:
        return True
    else:
        return False


filtered_products = list(filter(prix_sup_30, products_prix.items()))
print(filtered_products)
