import variables

products = variables.produits
prix = variables.prix

dic_product_prix = {}
for a, b in zip(products, prix):
    dic_product_prix[a] = b

print(dic_product_prix)
