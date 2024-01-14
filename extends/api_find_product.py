from extends.api import Api
import requests


class ApiFindProduct(Api):
    def find_product(self, r_cl_type, r_channel, r_lpur, r_sm_loan, r_mn_loan, r_currency, r_firm,
                        r_lend_kind, r_line_kind, r_sm_line, r_mn_line, r_pa_mtd, seasonMark, r_lpg,
                        r_insur_comp, trancheNumber, r_sm_loan_amount_mapping):

        data = {
            "channelId": r_channel,
            "clientTypeId": r_cl_type,
            "creditPurposeId": r_lpur,
            "creditSum": r_sm_loan_amount_mapping,
            "creditTerm": r_mn_loan,
            "currencyId": r_currency,
            "firmId": r_firm,
            "insurId": r_insur_comp,
            "lendKindId": r_lend_kind,
            "lineId": None,
            "lineProductId": r_line_kind,
            "lineSum": r_sm_line,
            "lineTerm": r_mn_line,
            "payMethodId": r_pa_mtd,
            "productSubTypeId": [r_lpg],
            "seasonMark": seasonMark,
            "trancheNumber": trancheNumber,
            "validSince": "08.01.2024"
        }
        response = requests.post(f"{self.host}/api/pfact/datahandler/findProduct", headers=self.headers_type,
                                 verify=False, json=data)
        return response
