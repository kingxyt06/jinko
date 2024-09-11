import json


class TestCheckEquality:
    #校验债权人和债务人
    def test_checkEquality(self, get_agw_token, req_AGW):
        params = {
            'supplierCompanyId': '1818580248779436034',
            'coreCompanyId': '1818578591995801601',
        }

        json_data = {
            'supplierCompanyId': '1818580248779436034',
            'coreCompanyId': '1818578591995801601',
            'busiCoreCompanyId': None,
            'hasOldBuyer': '0',
            'oldBuyerId': None,
            'fundsId': None,
            'assetAmount': '10000',
            'accountReceivableDueDate': '2024-09-30',
            'contractTradeName': None,
            'contractTradeNo': None,
            'contractTradeSignDate': None,
            'dataChangeHash': 'f3199h8v',
        }
        cookies = get_agw_token
        r = req_AGW
        url = 'asset-web/asset/checkEquality'
        res = r.visit(method='POST',
                      url=url,
                      params=params,
                      cookies=cookies,
                      json=json_data,
                      )
        res = json.loads(res.text)
        assert res['data'] == True
