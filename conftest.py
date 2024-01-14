import random
import pytest
from extends.api_create_product import ApiCreateProduct

@pytest.fixture()
def product_name():
    name = "product"
    random_number = random.randint(1, 999)
    name_product = f"{name}{random_number}"
    return name_product


@pytest.fixture()
def r_channel():
    refs_Id = [2, 3, 4, 5, 29, 30, 55, 31]
    random_refsId = random.choice(refs_Id)
    print(random_refsId)
    return random_refsId


@pytest.fixture()
def r_cl_type():
    refs_Id = [1, 2, 3]
    random_refs_Id = random.choice(refs_Id)
    return random_refs_Id


@pytest.fixture()
def r_lpur():
    refs_Id = [1, 2, 3, 4, 5, 6, 7, 103]
    random_refr_Id = random.choice(refs_Id)
    return random_refr_Id


@pytest.fixture()
def r_sm_loan(request):
    refs_Id = [1, 2, 3, 5, 6, 8]
    random_refs_Id = random.choice(refs_Id)

    if "creditSum" in request.fixturename:
        return random_refs_Id  #
    else:
        return {"id": random_refs_Id, "amount": r_sm_loan_amount_mapping(random_refs_Id)}


id_to_amount_mapping = {
    1: [120000, 250000],
    2: [5000, 7000000],
    3: [10000, 2000000],
    5: [300000, 2000000],
    6: [300000, 69000000],
    8: [30000000, 69000000]
}


@pytest.fixture()
def r_sm_loan_amount_mapping(r_sm_loan):
    if isinstance(r_sm_loan, int):  # Проверяем, если это айди
        min_amount, max_amount = id_to_amount_mapping[r_sm_loan]
        return random.randint(min_amount, max_amount)
    else:
        return r_sm_loan


@pytest.fixture()
def creditSum():
    credit = random.randint(5000, 300000000)
    return credit


@pytest.fixture()
def r_mn_loan():
    refs_Id = [1,2,3,6]
    random_refs_Id = random.choice(refs_Id)
    return random_refs_Id


@pytest.fixture()
def r_currency():
    refs_Id = [1, 2,]
    random_refs_Id = random.choice(refs_Id)
    return random_refs_Id


@pytest.fixture()
def r_firm():
    refs_Id = [1, 2, 3, 4, 10, 5]
    random_refs_Id = random.choice(refs_Id)
    return random_refs_Id


@pytest.fixture()
def r_lend_kind():
    refs_Id = [1, 2, 3, 4]
    random_refs_Id = random.choice(refs_Id)
    return random_refs_Id


@pytest.fixture()
def r_line_kind():
    refs_Id = [1, 2]
    random_refs_Id = random.choice(refs_Id)
    return random_refs_Id


@pytest.fixture()
def r_sm_line():
    refs_Id = [1, 2, 3, 4, 5, 6]
    random_refs_Id = random.choice(refs_Id)
    return random_refs_Id


@pytest.fixture()
def r_mn_line():
    refs_Id = [1, 2, 3, 4]
    random_refs_Id = random.choice(refs_Id)
    return random_refs_Id


@pytest.fixture()
def r_mn_type():
    refs_Id = [1, 2, 3, 4]
    random_refs_Id = random.choice(refs_Id)
    return random_refs_Id


@pytest.fixture()
def r_pa_mtd():
    refs_Id = [1, 2, 3]
    random_refs_Id = random.choice(refs_Id)
    return random_refs_Id


@pytest.fixture()
def r_season():
    refs_Id = [1, 2]
    random_refs_Id = random.choice(refs_Id)
    return random_refs_Id


@pytest.fixture()
def seasonMark():
    season = [True, False]
    return random.choice(season)


@pytest.fixture()
def trancheNumber():
    tranche = [1, 2]
    tranche.append(None) if random.choice([True, False]) else None
    return random.choice(tranche)


@pytest.fixture()
def r_lpg():
    refs_Id = [1, 2, 3, 4]
    random_refs_Id = random.choice(refs_Id)
    return random_refs_Id


@pytest.fixture()
def r_insur_comp():
    refs_Id = [1, 2, 15, 14, 12, 13, 18, 19, 2, 3, 4]
    refs_Id.append(None) if random.choice([True, False]) else None
    random_refs_Id = random.choice(refs_Id)
    return random_refs_Id


@pytest.fixture()
def r_pct_loan():
    refs_Id = [1, 2, 3, 4, 5, 6, 13, 12, 20, 21]
    random_refs_Id = random.choice(refs_Id)
    return random_refs_Id


@pytest.fixture()
def r_pct_param():
    refs_Id = [1, 2, 3, 4, 5, 6, 7, 8]
    random_refs_Id = random.choice(refs_Id)
    return random_refs_Id

# @pytest.fixture()
# def create_product_data():
#     product_name = 'product'
#     r_cl_type_value = r_cl_type()
#     r_channel_value = r_channel()
#     r_lpur_value = r_lpur()
#     r_sm_loan_value = r_sm_loan_amount_mapping()
#     r_mn_loan_value = r_mn_loan()
#     r_currency_value = r_currency()
#     r_firm_value = r_firm()
#     r_lend_kind_value = r_lend_kind()
#     r_line_kind_value = r_line_kind()
#     r_sm_line_value = r_sm_line()
#     r_mn_line_value = r_mn_line()
#     r_mn_type_value = r_mn_type()
#     r_pa_mtd_value = r_pa_mtd()
#     r_season_value = r_season()
#     r_lpg_value = r_lpg()
#     r_insur_comp_value = r_insur_comp()
#     r_pct_loan_value = r_pct_loan()
#     r_pct_param_value = r_pct_param()
#
#     return {
#         "product_name": product_name,
#         "r_cl_type": r_cl_type_value,
#         "r_channel": r_channel_value,
#         "r_lpur": r_lpur_value,
#         "r_sm_loan": r_sm_loan_value,
#         "r_mn_loan": r_mn_loan_value,
#         "r_currency": r_currency_value,
#         "r_firm": r_firm_value,
#         "r_lend_kind": r_lend_kind_value,
#         "r_line_kind": r_line_kind_value,
#         "r_sm_line": r_sm_line_value,
#         "r_mn_line": r_mn_line_value,
#         "r_mn_type": r_mn_type_value,
#         "r_pa_mtd": r_pa_mtd_value,
#         "r_season": r_season_value,
#         "r_lpg": r_lpg_value,
#         "r_insur_comp": r_insur_comp_value,
#         "r_pct_loan": r_pct_loan_value,
#         "r_pct_param": r_pct_param_value
#     }
#
# product_data = create_product_data()
# response = ApiCreateProduct().create_product(**product_data)