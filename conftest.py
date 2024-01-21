import random
import pytest


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
def r_sm_loan():
    refs_Id = [1, 2, 3, 5, 6, 8]
    random_refs_Id = random.choice(refs_Id)
    return random_refs_Id


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
    refs_Id = 1
    # random_refs_Id = random.choice(refs_Id)
    return refs_Id


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
