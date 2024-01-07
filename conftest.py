import random

import pytest


@pytest.fixture()
def product_name():
    name = "продукт"
    random_number = random.randint(1, 999999)
    name_product = f"{name}{random_number}"
    return name_product

