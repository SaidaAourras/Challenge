 # 1
def product_prix(products, prix):
    dic_product_prix = {}
    for a, b in zip(products, prix):
        dic_product_prix[a] = b
    return dic_product_prix

# 2

def prix_sup_30(element):
    if int(element[1]) >= 30:
        return True
    else:
        return False

def filter_Product():
    filtered_products = list(filter(prix_sup_30, product_prix.items()))
    return filtered_products

# def transform_to_String(products, prix):
    for a , b in zip(products, prix):
         
        