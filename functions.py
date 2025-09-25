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


def filter_Product(products, prix):
    filtered_products = list(
        filter(prix_sup_30, (product_prix(products, prix)).items())
    )
    return filtered_products


# 3


def transform_to_String(products, prix):
    result = []
    for product, key in zip(products, prix):
        result.append(f"{product} coute {key} DH")
    return result


# 4
def mySort(x):
    return x[1]


def ordre_croissant(products, prix):
    my_dict = list((product_prix(products, prix)).items())
    # print(my_dict)
    my_dict.sort(key=mySort)
    return my_dict


# 5 - 6


def afficherList(products, prix):
    resultat_final = []
    for i in ordre_croissant(products, prix):
        resultat_final.append(i)
    return resultat_final


# 7


def puls_cher(products, prix):
    return ordre_croissant(products, prix)[-1]


def moin_cher(products, prix):
    return ordre_croissant(products, prix)[0]


# 8


def is_greater_1000(element):
    if element[1] > 1000:
        return f"{element[0]} cout de {element[1]} (LUXE)"
    else:
        return f"{element[0]} cout de {element[1]}"


def luxe_products(products, prix):
    return list(map(is_greater_1000, ordre_croissant(products, prix)))
