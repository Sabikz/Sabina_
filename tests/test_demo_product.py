# import requests
# import unittest
# from unittest.mock import MagicMock
#
#
# class ProdCreate:
#     def __init__(self, create_product_url):
#         self.create_product_url = create_product_url
#         self.auth_token = auth_token
#
#
#
#     def create_product(self, product_name, prod_params):
#         headers = {"Authorization": f"Bearer {self.auth_token}"}
#         prod_data = {
#             "product": {
#                 "arh": False,
#                 "asbukaId": "as1",
#                 "colvirId": "co1",
#                 "name": product_name,
#                 "nameEn": "prod",
#                 "nameKaz": "prod",
#                 "productTypeId": 1
#             },
#             "selectedParams": [
#                 {"paramId": key, "refsId": [value]} for key, value in prod_params["selected_params"].items()
#             ]
#         }
#         response = requests.post(self.create_product_url, json=prod_data, headers=headers)
#
#         # Печать для отладки
#         print(response.json())
#
#         return response.json()["selectedParams"][0]["refsId"][0]
#
# prod_params = {
#     "product_name": "product",
#     "selected_params": {
#         1: "r_cl_type",
#         27: "r_channel",
#         5: "r_lpur",
#         4: "r_sm_loan",
#         11: "r_mn_loan",
#         6: "r_currency",
#         7: "r_firm",
#         9: "r_lend_kind",
#         25: "r_line_kind",
#         12: "r_sm_line",
#         13: "r_mn_line",
#         2: "r_mn_type",
#         22: "r_pa_mtd",
#         10: "r_season",
#         8: "r_lpg",
#         3: "r_insur_comp",
#         15: "r_pct_loan",
#         14: "r_pct_param"
#     }
# }
# auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJSb2xlIjoicHJvZHVjdGNhdGFsb2d1ZV9hZG1pbiIsIk1ETVVzZXIiOiJkYW5pYWx6MDMwOCIsImlzcyI6InBmYWN0LmFkbWluLmFwaSIsImF1ZCI6WyJwZmFjdC5hZG1pbi5hcGkiXSwiZXhwIjoxNzA1NDI4MDAwLCJuYmYiOjE3MDU0MjMyNzUsImlhdCI6MTcwNTQyMzI3NX0.w7tMf6EVHP7CkkLAO4T29ksF1lMYYDvkcNa1xiDiVEo"
# create_product_url = "https://dev-svc.kmf.kz/api/pfact/admin/createProduct"
# product_creator = ProdCreate(create_product_url)
#
# refs_id = product_creator.create_product(prod_params["product_name"], prod_params)
# print(refs_id)
#
#
# class ProdFind:
#     def __init__(self, find_prod_url):
#         self.find_product_url = find_prod_url
#
#     def find_product(self, r_cl_type, r_channel, r_lpur, r_mn_loan, r_currency, r_firm,
#                         r_lend_kind, r_line_kind, r_sm_line, r_mn_line, r_pa_mtd, r_lpg,
#                         r_insur_comp, trancheNumber, r_sm_loan_amount_mapping):
#         find_product_data = {
#             "channelId": r_channel,
#             "clientTypeId": r_cl_type,
#             "creditPurposeId": r_lpur,
#             "creditSum": r_sm_loan_amount_mapping,
#             "creditTerm": r_mn_loan,
#             "currencyId": r_currency,
#             "firmId": r_firm,
#             "insurId": r_insur_comp,
#             "lendKindId": r_lend_kind,
#             "lineId": None,
#             "lineProductId": r_line_kind,
#             "lineSum": r_sm_line,
#             "lineTerm": r_mn_line,
#             "payMethodId": r_pa_mtd,
#             "productSubTypeId": [r_lpg],
#             "seasonMark": True,
#             "trancheNumber": trancheNumber,
#             "validSince": "16.01.2024"
#         }
#
#         response = requests.post(self.find_product_url, json=find_product_data)
#         return response
#
# find_prod_url = "https://dev-svc.kmf.kz/api/pfact/datahandler/findProduct"
# product_finder = ProdFind(find_prod_url)
#
#
# class TestProdCreateAndFind(unittest.TestCase):
#     def test_create_and_find_product(self):
#         requests.post = MagicMock(return_value=MagicMock(json=lambda: {"selectedParams": [{"refsId": [1]}]}))
#
#         create_product_url = "https://dev-svc.kmf.kz/api/pfact/admin/createProduct"
#         prod_params = {
#             "product_name": "product",
#             "selectedParams": {
#                 1: "r_cl_type",
#                 27: "r_channel",
#                 5: "r_lpur",
#                 4: "r_sm_loan",
#                 11: "r_mn_loan",
#                 6: "r_currency",
#                 7: "r_firm",
#                 9: "r_lend_kind",
#                 25: "r_line_kind",
#                 12: "r_sm_line",
#                 13: "r_mn_line",
#                 2: "r_mn_type",
#                 22: "r_pa_mtd",
#                 10: "r_season",
#                 8: "r_lpg",
#                 3: "r_insur_comp",
#                 15: "r_pct_loan",
#                 14: "r_pct_param"
#             }
#         }
#
#         product_creator = ProdCreate(create_product_url)
#         refs_id = product_creator.create_product(prod_params["product_name"], prod_params)
#
#         find_prod_url = "https://dev-svc.kmf.kz/api/pfact/datahandler/findProduct"
#         product_finder = ProdFind(find_prod_url)
#
#         r_cl_type = 1
#         r_channel = 2
#         r_lpur = 3
#         r_mn_loan = 12
#         r_currency = 1
#         r_firm = 4
#         r_lend_kind = 5
#         r_line_kind = 6
#         r_sm_line = 100000
#         r_mn_line = 24
#         r_pa_mtd = 7
#         r_lpg = 8
#         r_insur_comp = 9
#         trancheNumber = 1
#         r_sm_loan_amount_mapping = 50000
#
#         find_product_response = product_finder.find_product(r_cl_type, r_channel, r_lpur, r_mn_loan, r_currency, r_firm,
#                                                             r_lend_kind, r_line_kind, r_sm_line, r_mn_line, r_pa_mtd,
#                                                             r_lpg, r_insur_comp, trancheNumber, r_sm_loan_amount_mapping)
#
#         self.assertEqual(find_product_response.status_code, 200)
#
# if __name__ == '__main__':
#     unittest.main()
