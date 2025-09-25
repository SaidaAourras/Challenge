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


# def mySort1(x):
#      x.values()[1]


def ordre_croissant(products, prix):
    my_dict = (product_prix(products, prix)).items()
    # my_dict1 = product_prix(products, prix)
    return sorted(my_dict, key=mySort)


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


#  luxe products ny lambda
def lambda_luxe(products, prix):
    return list(
        map(
            lambda x: (
                f"{x[0]} cout de {x[1]} (LUXE)"
                if x[1] > 1000
                else f"{x[0]} cout de {x[1]}"
            ),
            ordre_croissant(products, prix),
        )
    )


# etap2


def recherche_par_nom(products, prix):
    product = input("donner le nom du produit : ")
    for i, j in (product_prix(products, prix)).items():
        if i.lower() == product.lower():
            return f"{i} cout de {j} dh"


def ajouter_Product(products, prix):
    product = input("donner le nom du produit : ")
    price = input("donner le prix du produit : ")
    new_dict = product_prix(products, prix)
    new_dict[product] = price
    return new_dict


def menu(products, prix):
    a = 0
    while True:
        match a:
            case 0:
                print("1 - pour chercher un produit par nom ")
                print("2 - pour ajouter un produit  ")
                print("3 - pour quiter  ")
                a = int(input("taper le votre choix : "))
            case 1:
                print(recherche_par_nom(products, prix))
                a = 0
            case 2:
                print(ajouter_Product(products, prix))
                a = 0
            case _:
                break
