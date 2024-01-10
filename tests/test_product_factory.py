import pytest

from extends.api_create_product import ApiCreateProduct
from baseclasses.response import Response
from extends.api_find_product import ApiFindProduct


@pytest.fixture
def create_product(request):
    params = request.node.get_closest_marker("product_params").args
    create_prod = ApiCreateProduct().create_product(*params)
    response_data = create_prod.json()
    return response_data


@pytest.mark.filterwarnings("ignore::urllib3.exceptions.InsecureRequestWarning")
@pytest.mark.product_params("product_name", "r_cl_type", "r_channel", "r_lpur", "r_sm_loan", "r_mn_loan", "r_currency",
                           "r_firm", "r_lend_kind", "r_line_kind", "r_sm_line", "r_mn_line", "r_mn_type", "r_pa_mtd",
                           "r_season", "r_lpg", "r_insur_comp", "r_pct_loan", "r_pct_param")
def test_create_product(create_product):
    response = Response(create_product)
    response.assert_status_code(200)
    print(f"Product create: {create_product}")


@pytest.mark.product_find_params("r_cl_type", "r_channel", "r_lpur", "r_sm_loan", "r_mn_loan", "r_currency", "r_firm",
                                   "r_lend_kind", "r_line_kind", "r_sm_line", "r_pa_mtd", "r_season", "r_lpg",
                                   "r_insur_comp", "trancheNumber")
def test_find_product(create_product, request):
    find_params = request.node.get_closest_marker("product_find_params").args
    find_product = ApiFindProduct().find_product(*find_params)
    response_data = find_product.json()
    assert response_data == create_product
    print(f"Product find: {response_data}")



