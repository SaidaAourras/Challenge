import functions
import variables

products = variables.produits
prix = variables.prix

print(functions.product_prix(products, prix))
print(functions.filter_Product(products, prix))
print(functions.transform_to_String(products, prix))
print(functions.ordre_croissant(products, prix))
print(functions.afficherList(products, prix))
print(functions.puls_cher(products, prix))
print(functions.moin_cher(products, prix))
print(functions.luxe_products(products, prix))
