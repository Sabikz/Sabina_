import pytest

from extends.api_create_product import ApiCreateProduct
from baseclasses.response import Response
import warnings


@pytest.mark.filterwarnings("ignore::urllib3.exceptions.InsecureRequestWarning")
def test_create_product(product_name):
    create_prod = ApiCreateProduct().create_product(product_name)
    response_data = create_prod
    response = Response(response_data)
    response.assert_status_code(200)

