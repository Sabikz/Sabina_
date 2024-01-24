from extends.api_create_product import ApiCreateProduct, SpecificException
from baseclasses.response import Response
from extends.api_find_product import ApiFindProduct
import pytest
import allure


class TestFailedError(Exception):
    pass


@allure.feature("Product Factory")
@allure.story("Product")
@pytest.mark.filterwarnings("ignore::urllib3.exceptions.InsecureRequestWarning")
def test_create_product(product_name, r_cl_type, r_channel, r_lpur, r_sm_loan, r_mn_loan, r_currency, r_firm,
                        r_lend_kind, r_line_kind, r_sm_line, r_mn_line, r_mn_type, r_pa_mtd, r_season, r_lpg,
                        r_insur_comp, r_pct_loan, r_pct_param):
    try:
        with allure.step("Create product"):
            create_prod = ApiCreateProduct().create_product(product_name, r_cl_type, r_channel, r_lpur, r_sm_loan, r_mn_loan,
                                                        r_currency, r_firm, r_lend_kind, r_line_kind, r_sm_line, r_mn_line,
                                                        r_mn_type, r_pa_mtd, r_season, r_lpg, r_insur_comp, r_pct_loan,
                                                        r_pct_param)
            response_data = create_prod
            response = Response(response_data)
        with allure.step("Results"):
            response.assert_status_code(200)
            print(
                f"product_name: {product_name}, r_cl_type: {r_cl_type}, r_channel: {r_channel}, "
                f"r_lpur: {r_lpur}, r_sm_loan: {r_sm_loan}, r_mn_loan: {r_mn_loan}, "
                f"r_currency: {r_currency}, r_firm: {r_firm}, r_lend_kind: {r_lend_kind}, "
                f"r_line_kind: {r_line_kind}, r_sm_line: {r_sm_line}, r_mn_line: {r_mn_line}, "
                f"r_mn_type: {r_mn_type}, r_pa_mtd: {r_pa_mtd}, r_season: {r_season}, "
                f"r_lpg: {r_lpg}, r_insur_comp: {r_insur_comp}, r_pct_loan: {r_pct_loan}, "
                f"r_pct_param: {r_pct_param}"
            )

    except SpecificException as e:
        raise TestFailedError(f"ERROR_FOR_DEVOPS: Test failed with the following error - {str(e)}")

    except Exception as e:

        raise TestFailedError(f"ERROR_FOR_DEVOPS: Test failed with an unexpected error - {str(e)}")


# @pytest.mark.filterwarnings("ignore::urllib3.exceptions.InsecureRequestWarning")
# def test_find_product(r_cl_type, r_channel, r_lpur, r_sm_loan, r_mn_loan, r_currency, r_firm,
#                         r_lend_kind, r_line_kind, r_sm_line, r_mn_line,  r_pa_mtd, seasonMark, r_lpg,
#                         r_insur_comp, creditSum, trancheNumber):
#
#     find_product = ApiFindProduct().find_product(r_cl_type, r_channel, r_lpur, r_sm_loan, r_mn_loan, r_currency, r_firm,
#                         r_lend_kind, r_line_kind, r_sm_line, r_mn_line, r_pa_mtd, seasonMark, r_lpg,
#                         r_insur_comp, creditSum, trancheNumber)
#     response_data = find_product
#     response = Response(response_data)
#     print("Response content:", response.response_json)
#     response.assert_status_code(200)
