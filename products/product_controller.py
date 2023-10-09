from products.product import create_product


# To showcase all the products
def show_products():
    try:
        with open("products.txt", "r") as file:
            product_list = file.readlines()
            for product in product_list:
                # Converting each product to list for better formatting
                product = product.split(",")
                print(product)

    except FileNotFoundError:
        print("There are no Products Available")


# Find Product by name
def find_product(name):
    with open("products.txt", "r") as file:
        product_list = file.readlines()
        for product in product_list:
            product = product.split(",")
            # Comparing Name
            if name.strip().lower() == product[1].strip().lower():
                return product
        print("Product Not Found")


# To get product by name
def get_product_by_name():
    try:
        name = input("Enter the product name: ")
        product = find_product(name)
        if product != None:
            print(product)

    except FileNotFoundError:
        print("There are no Products Available")


# Update Product (only owner can perform)
# find that product and delete it then create new product and append it
def update_product():
    lists = []
    name = input("Enter the product you want to be updated: ")

    # Find Product
    product_to_be_updated = find_product(name)
    if product_to_be_updated == None:
        return

    # Delete Product Logic
    product_to_be_updated = (",").join(product_to_be_updated)
    with open("products.txt", "r") as file:
        product_list = file.readlines()
        for product in product_list:
            if product.strip() == product_to_be_updated.strip():
                continue
            lists.append(product)
    with open("products.txt", "w") as file:
        file.writelines(lists)

    # call create product for updated product
    create_product()


# Delete Product (only owner can perform)
def delete_product():
    lists = []
    name = input("Enter the name the product you want to delete: ")
    product_to_be_deleted = find_product(name)
    if product_to_be_deleted == None:
        return
    product_to_be_deleted = (",").join(product_to_be_deleted)
    with open("products.txt", "r") as file:
        product_list = file.readlines()
        for product in product_list:
            if product.strip() == product_to_be_deleted.strip():
                continue
            lists.append(product)

    with open("products.txt", "w") as file:
        file.writelines(lists)

    print("Product Deleted Successfully")
