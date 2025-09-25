import functions
import variables

products = variables.produits
prix = variables.prix

print("les produits avec le prix :\n", functions.product_prix(products, prix))
print("filtrer les produit de prix > 30 :\n", functions.filter_Product(products, prix))
print(
    "la liste des produits et prix sous forme des phrases : \n",
    functions.transform_to_String(products, prix),
)
print("triage en ordre croissant : \n", functions.ordre_croissant(products, prix))
print("afficher le resultat : \n", functions.afficherList(products, prix))
print("le produit le plus cher : \n", functions.puls_cher(products, prix))
print("le produit le moins cher : \n", functions.moin_cher(products, prix))
print("Bonus : \n", functions.luxe_products(products, prix))
print("autre resultat : ", functions.lambda_luxe(products, prix))
print(functions.ajouter_Product(products, prix))

functions.menu(products, prix)
