from extends_.api import Api
import requests


class CommonData:
    @staticmethod
    def get_data(product_name):
        return {
            "product": {
                "arh": False,
                "asbukaId": "test",
                "colvirId": "test",
                "name": product_name,
                "nameEn": "test",
                "nameKaz": "test",
                "productTypeId": 1,
            }
        }


class SpecificException(Exception):
    pass


class ApiCreateProduct(Api):
    def create_product(self, product_name, r_cl_type, r_channel, r_lpur, r_sm_loan, r_mn_loan, r_currency, r_firm,
                       r_lend_kind, r_line_kind, r_sm_line, r_mn_line, r_mn_type, r_pa_mtd, r_season, r_lpg,
                       r_insur_comp, r_pct_loan, r_pct_param):

        selected_params = [
            {"paramId": param_id, "refsId": [ref_id]}
            for param_id, ref_id in [
                (1, r_cl_type), (27, r_channel), (5, r_lpur), (4, r_sm_loan),
                (11, r_mn_loan), (6, r_currency), (7, r_firm), (9, r_lend_kind),
                (25, r_line_kind), (12, r_sm_line), (13, r_mn_line), (2, r_mn_type),
                (22, r_pa_mtd), (10, r_season), (8, r_lpg), (3, r_insur_comp),
                (15, r_pct_loan), (14, r_pct_param)
            ]
        ]

        data = {
            **CommonData.get_data(product_name),
            "selectedParams": selected_params
        }
        try:
            response = requests.post(f"{self.host}/api/pfact/admin/createProduct", headers=self.headers_type,
                                     verify=False, json=data)
            response.raise_for_status()

        except requests.exceptions.RequestException as req_exc:

            raise SpecificException(f"Error in requests: {req_exc}")

        except Exception as e:

            raise SpecificException(f"Unexpected error: {e}")

        return response



