import requests
import json
from uuid import uuid1
import random


def get_random_product_full_data():
    response = requests.get('https://dummyjson.com/products')
    response.raise_for_status()

    products = response.json()['products']
    return random.choice(products)


def download_file(file_url: str) -> str:
    response = requests.get(file_url)
    response.raise_for_status()

    path = f'images/{uuid1()}.webp'
    with open(path, 'wb') as f:
        f.write(response.content)

    return path


def get_product_data(product: dict):
    image_path = download_file(product['thumbnail'])

    return {
        "id": product['id'],
        "title": product['title'],
        "description": product['description'],
        "category": product['category'],
        "price": product['price'],
        "path": image_path
    }


def main() -> None:
    products = []

    for i in range(10):
        product = get_random_product_full_data()
        products.append(get_product_data(product))

    with open('products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=4, ensure_ascii=False)


main()
