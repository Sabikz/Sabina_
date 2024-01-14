
import pytest
from extends.api_create_product import ApiCreateProduct, SpecificException
from baseclasses.response import Response
from extends.api_find_product import ApiFindProduct


def test_create_product(create_product_data):
    try:
        create_prod = ApiCreateProduct().create_product(**create_product_data)
        response_data = create_prod
        response = Response(response_data)
        response.assert_status_code(200)
        print("Product created successfully!")

    except Exception as e:
        print(f"Error creating product: {e}")
        assert False


def test_find_product(create_product_data):
    try:
        r_cl_type = create_product_data["r_cl_type"]
        r_channel = create_product_data["r_channel"]
        r_lpur = create_product_data["r_lpur"]
        r_sm_loan = create_product_data["r_sm_loan"]
        r_mn_loan = create_product_data["r_mn_loan"]
        r_currency = create_product_data["r_currency"]
        r_firm = create_product_data["r_firm"]
        r_lend_kind = create_product_data["r_lend_kind"]
        r_line_kind = create_product_data["r_line_kind"]
        r_sm_line = create_product_data["r_sm_line"]
        r_mn_line = create_product_data["r_mn_line"]
        r_pa_mtd = create_product_data["r_pa_mtd"]
        r_season = create_product_data["r_season"]
        r_lpg = create_product_data["r_lpg"]
        r_insur_comp = create_product_data["r_insur_comp"]

        find_prod = ApiFindProduct().find_product(
            r_cl_type, r_channel, r_lpur, r_sm_loan, r_mn_loan, r_currency, r_firm,
            r_lend_kind, r_line_kind, r_sm_line, r_mn_line, r_pa_mtd, r_season, r_lpg,
            r_insur_comp, trancheNumber, creditSum
        )
        response_data = find_prod
        response = Response(response_data)
        response.assert_status_code(200)
        print("Product found successfully!")

    except Exception as e:
        print(f"Error finding product: {e}")
        assert False