import pytest

from extends.api_create_product import ApiCreateProduct
from baseclasses.response import Response


@pytest.mark.filterwarnings("ignore::urllib3.exceptions.InsecureRequestWarning")
def test_create_product(product_name, r_cl_type, r_channel, r_lpur, r_sm_loan, r_mn_loan, r_currency, r_firm,
                        r_lend_kind, r_line_kind, r_sm_line, r_mn_line, r_mn_type, r_pa_mtd, r_season):
    create_prod = ApiCreateProduct().create_product(product_name, r_cl_type, r_channel, r_lpur, r_sm_loan, r_mn_loan,
                                                    r_currency, r_firm, r_lend_kind, r_line_kind, r_sm_line, r_mn_line,
                                                    r_mn_type, r_pa_mtd, r_season)
    response_data = create_prod
    response = Response(response_data)
    response.assert_status_code(200)
    print(product_name)

