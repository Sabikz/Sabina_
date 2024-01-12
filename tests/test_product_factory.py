from extends.api_create_product import ApiCreateProduct, SpecificException
from baseclasses.response import Response
from extends.api_find_product import ApiFindProduct
import pytest


class TestFailedError(Exception):
    pass


def collect_test_data(self):
    return {
        "product_name": self.product_name,
        "r_cl_type": self.r_cl_type,
        "r_channel": self.r_channel,
        "r_lpur": self.r_lpur,
        "r_sm_loan": self.r_sm_loan,
        "r_mn_loan": self.r_mn_loan,
        "r_currency": self.r_currency,
        "r_firm": self.r_firm,
        "r_lend_kind": self.r_lend_kind,
        "r_line_kind": self.r_line_kind,
        "r_sm_line": self.r_sm_line,
        "r_mn_line": self.r_mn_line,
        "r_mn_type": self.r_mn_type,
        "r_pa_mtd": self.r_pa_mtd,
        "r_season": self.r_season,
        "r_lpg": self.r_lpg,
        "r_insur_comp": self.r_insur_comp,
        "r_pct_loan": self.r_pct_loan,
        "r_pct_param": self.r_pct_param
    }


@pytest.mark.filterwarnings("ignore::urllib3.exceptions.InsecureRequestWarning")
def test_create_product(self, product_name, r_cl_type, r_channel, r_lpur, r_sm_loan, r_mn_loan, r_currency, r_firm,
                        r_lend_kind, r_line_kind, r_sm_line, r_mn_line, r_mn_type, r_pa_mtd, r_season, r_lpg,
                        r_insur_comp, r_pct_loan, r_pct_param):

    self.product_name = product_name
    self.r_cl_type = r_cl_type
    self.r_channel = r_channel
    self.r_lpur = r_lpur
    self.r_sm_loan = r_sm_loan
    self.r_mn_loan = r_mn_loan
    self.r_currency = r_currency
    self.r_firm = r_firm
    self.r_lend_kind = r_lend_kind
    self.r_line_kind = r_line_kind
    self.r_sm_line = r_sm_line
    self.r_mn_line = r_mn_line
    self.r_mn_type = r_mn_type
    self.r_pa_mtd = r_pa_mtd
    self.r_season = r_season
    self.r_lpg = r_lpg
    self.r_insur_comp = r_insur_comp
    self.r_pct_loan = r_pct_loan
    self.r_pct_param = r_pct_param

    try:
        create_prod = ApiCreateProduct().create_product(
            self.product_name, self.r_cl_type, self.r_channel, self.r_lpur, self.r_sm_loan, self.r_mn_loan,
            self.r_currency, self.r_firm, self.r_lend_kind, self.r_line_kind, self.r_sm_line, self.r_mn_line,
            self.r_mn_type, self.r_pa_mtd, self.r_season, self.r_lpg, self.r_insur_comp, self.r_pct_loan,
            self.r_pct_param
        )
        response_data = create_prod
        response = Response(response_data)
        response.assert_status_code(200)

        test_data = self.collect_test_data()
        print("Data collected for the next test:", test_data)

    except SpecificException as e:
        raise TestFailedError(f"ERROR_FOR_DEVOPS: Test failed with the following error - {str(e)}")

    except Exception as e:
        raise TestFailedError(f"ERROR_FOR_DEVOPS: Test failed with an unexpected error - {str(e)}")


@pytest.mark.filterwarnings("ignore::urllib3.exceptions.InsecureRequestWarning")
def test_find_product(r_cl_type, r_channel, r_lpur, r_sm_loan, r_mn_loan, r_currency, r_firm,
                      r_lend_kind, r_line_kind, r_sm_line, r_mn_line, r_pa_mtd, seasonMark, r_lpg,
                      r_insur_comp, creditSum, trancheNumber):


    previous_test_data = TestCreateProduct().collect_test_data()

    #
    try:
        find_product = ApiFindProduct().find_product(
            r_cl_type, r_channel, r_lpur, r_sm_loan, r_mn_loan, r_currency, r_firm,
            r_lend_kind, r_line_kind, r_sm_line, r_mn_line, r_pa_mtd, seasonMark, r_lpg,
            r_insur_comp, creditSum, trancheNumber
        )

        response_data = find_product
        response = Response(response_data)
        print("Response content:", response.response_json)
        response.assert_status_code(200)

    except SpecificException as e:
        raise TestFailedError(f"ERROR_FOR_DEVOPS: Test failed with the following error - {str(e)}")

    except Exception as e:
        raise TestFailedError(f"ERROR_FOR_DEVOPS: Test failed with an unexpected error - {str(e)}")