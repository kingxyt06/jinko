import json


class TestSaveAsset:
    def test_saveAsset(self, get_agw_token, req_AGW):
        json_data = {
            'supplierCompanyId': '1818580248779436034',
            'coreCompanyId': '1818578591995801601',
            'busiCoreCompanyId': None,
            'hasOldBuyer': '0',
            'oldBuyerId': None,
            'fundsId': None,
            'assetAmount': '10001',
            'accountReceivableDueDate': '2024-09-30',
            'contractTradeName': None,
            'contractTradeNo': None,
            'contractTradeSignDate': None,
            'dataChangeHash': 'f3199h8v',
        }
        print(type(json_data))
        cookies = get_agw_token
        r = req_AGW
        # url = 'asset-web/asset/saveAsset.yaml'
        # res = r.visit(method='POST',
        #               url=url,
        #               cookies=cookies,
        #               json=json_data,
        #               )
        # res = json.loads(res.text)
        # print(res)
        # assert res['data'] == True
