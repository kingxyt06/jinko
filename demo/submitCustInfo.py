import requests

cookies = {
    'bccpordinscfqa': 'eb981024-93a9-47ff-9509-7aecb5f20151',
    'llsfn-auth-token-qa-current-login': 'fa54cabf0a3d9302da9da271b51af4db',
    'llsfn-auth-token-qa-pc': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWFsTmFtZSI6IuW8oOmHkemHkSIsImxvZ2luVGltZSI6MTcyNTg2MDM5MTAxNCwidXNlck5hbWUiOiIxNTA5MDQxMTQzNyIsImV4cCI6MTcyNTk0Njc5MSwidXNlcklkIjoiMTgyMDI4MDUyNDk1NzYyMjI3MyJ9.ecxU-kWTvsQjsokC2FfqUi3ohdNgCZTxWEkaIrZ4hyE',
    'llsfn-auth-token-qa-pcdate': '1725860391069',
    'llsfn-auth-token-qa-pc-current-login': 'df61d3b162e94feccb1ea98c1dc6f02d',
    'CURRENT-LOGIN': 'fa54cabf0a3d9302da9da271b51af4db',
    'llsfn-auth-token-qa': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWFsTmFtZSI6IueuoeeQhuWRmCIsImxvZ2luVGltZSI6MTcyNTg2MTQ5NDg3MCwidXNlck5hbWUiOiJhZG1pbiIsImV4cCI6MTcyNTk0Nzg5NCwidXNlcklkIjoiMTM1NDQxMzAzMjczMTUyNTEyNSJ9.4Nj5vOdNl0dUnU1_3-6OcNRzM05-0rnIeV2G9LrffRE',
    'llsfn-auth-token-qadate': '1725861494849',
    'llsfn-auth-token-dev-current-login': 'fa54cabf0a3d9302da9da271b51af4db',
    'llsfn-auth-token-dev': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWFsTmFtZSI6IueuoeeQhuWRmCIsImxvZ2luVGltZSI6MTcyNTg4NDQyMzQ1NSwidXNlck5hbWUiOiJhZG1pbiIsImV4cCI6MTcyNTk3MDgyMywidXNlcklkIjoiMTM1NDQxMzAzMjczMTUyNTEyNSJ9.mQ6mUeuzZf6bgEjZi4ZNlKdRy8fEYSO0ZgrWRehQbs4',
    'llsfn-auth-token-devdate': '1725884423434',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': 'bccpordinscfqa=eb981024-93a9-47ff-9509-7aecb5f20151; llsfn-auth-token-qa-current-login=fa54cabf0a3d9302da9da271b51af4db; llsfn-auth-token-qa-pc=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWFsTmFtZSI6IuW8oOmHkemHkSIsImxvZ2luVGltZSI6MTcyNTg2MDM5MTAxNCwidXNlck5hbWUiOiIxNTA5MDQxMTQzNyIsImV4cCI6MTcyNTk0Njc5MSwidXNlcklkIjoiMTgyMDI4MDUyNDk1NzYyMjI3MyJ9.ecxU-kWTvsQjsokC2FfqUi3ohdNgCZTxWEkaIrZ4hyE; llsfn-auth-token-qa-pcdate=1725860391069; llsfn-auth-token-qa-pc-current-login=df61d3b162e94feccb1ea98c1dc6f02d; CURRENT-LOGIN=fa54cabf0a3d9302da9da271b51af4db; llsfn-auth-token-qa=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWFsTmFtZSI6IueuoeeQhuWRmCIsImxvZ2luVGltZSI6MTcyNTg2MTQ5NDg3MCwidXNlck5hbWUiOiJhZG1pbiIsImV4cCI6MTcyNTk0Nzg5NCwidXNlcklkIjoiMTM1NDQxMzAzMjczMTUyNTEyNSJ9.4Nj5vOdNl0dUnU1_3-6OcNRzM05-0rnIeV2G9LrffRE; llsfn-auth-token-qadate=1725861494849; llsfn-auth-token-dev-current-login=fa54cabf0a3d9302da9da271b51af4db; llsfn-auth-token-dev=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWFsTmFtZSI6IueuoeeQhuWRmCIsImxvZ2luVGltZSI6MTcyNTg4NDQyMzQ1NSwidXNlck5hbWUiOiJhZG1pbiIsImV4cCI6MTcyNTk3MDgyMywidXNlcklkIjoiMTM1NDQxMzAzMjczMTUyNTEyNSJ9.mQ6mUeuzZf6bgEjZi4ZNlKdRy8fEYSO0ZgrWRehQbs4; llsfn-auth-token-devdate=1725884423434',
    'Origin': 'https://jinkoscf-agw-dev2.llsstd.com',
    'Pragma': 'no-cache',
    'Referer': 'https://jinkoscf-agw-dev2.llsstd.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'appCode': '5663a065693849daa7bcc619de976314',
    'appVersion': 'V1.4.0',
    'clientType': 'AGW',
    'projectCode': 'fc5c6702f8f14a33954299d010c06614',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'tenantCode': 'DEFAULT_TENANT_CODE',
}

params = {
    'custId': '1833103470227062786',
}

json_data = {
    'id': '1833103470227062786',
    'orgId': '0000000001',
    'orgName': '0',
    'custNo': 'CUST202409090174',
    'custName': '中软国际',
    'custShortName': '',
    'portalNo': '00000000001',
    'custEnglishName': '',
    'certificationNo': '9144030027940776XM',
    'businessLicenseStartTime': '2011-09-08',
    'businessLicenseEndTime': '2031-09-07',
    'timePermanent': 'NO',
    'custFormerName': '',
    'taxpayerIdentificationNo': '',
    'organizationStructureCode': '',
    'establishmentTime': '2011-09-08',
    'registerCapital': '100000',
    'paidInCapital': '',
    'workersNo': '',
    'registeredProvCity': {
        'provinceName': '广东省',
        'province': '440000',
        'cityName': '深圳市',
        'city': '440300',
    },
    'registProvince': '广东省',
    'registProvinceCode': '440000',
    'registCity': '深圳市',
    'registCityCode': '440300',
    'registeredAddress': '注册地址',
    'businessProvince': '',
    'businessProvinceCode': '',
    'businessCity': '',
    'businessCityCode': '',
    'businessAddress': '',
    'contactProvince': '',
    'contactProvinceCode': '',
    'contactCity': '',
    'contactCityCode': '',
    'contactAddress': '',
    'custEmail': '',
    'status': 'ADD',
    'managerName': '',
    'managerOrgId': '1',
    'managerOrgName': '1',
    'enable': 'yes',
    'createId': '1354413032731525125',
    'createName': '管理员',
    'createTime': '2024-09-09 19:29:50',
    'updateName': '管理员',
    'updateTime': '2024-09-09 19:46:59',
    'updateId': '1354413032731525125',
    'companyTypes': [
        'CORE',
        'SUPPLIER',
    ],
    'companyType': 'CORE',
    'signingMode': 'ON_LINE',
    'autoCustBuild': 'NO',
    'level': '',
    'certificationPeriodDTO': {
        'start': '2011-09-08',
        'end': '2031-09-07',
        'status': 'NO',
    },
    'intraGroupCompany': 'NO',
    'custBuildStatus': 'INIT',
    'custBuildType': 'AGW_BUILD',
    'custBuildSource': 'SELF',
    'registCa': 'yes',
    'custSettingConfig': {
        'id': '2',
        'settingNo': 'NO1111111',
        'custBuildAudit': 'yes',
        'signingMode': 'ON_LINE',
        'channelAudit': 'test',
        'faceCheck': 'no',
        'faceCount': 3,
        'smallAuthentication': 'no',
        'changeCustBuildAudit': 'yes',
        'maxApplyRemitCount': 5,
        'maxRemitMistakeCount': 5,
        'keyword': {
            'custKeyInfoList': '[{"editable":false,"enable":true,"isDefault":true,"key":"custName","name":"企业名称","visible":true},{"editable":false,"enable":true,"isDefault":true,"key":"companyTypes","name":"企业角色","visible":true},{"editable":false,"enable":true,"isDefault":true,"key":"managerId","name":"业务经理","visible":true},{"editable":false,"enable":true,"isDefault":true,"key":"parentCompany","name":"关联母公司","visible":true},{"editable":false,"enable":true,"isDefault":true,"key":"certificationPeriod","name":"营业执照有效期","visible":true},{"editable":false,"enable":true,"isDefault":true,"key":"affiliatedCompany","name":"挂靠企业","visible":true},{"editable":false,"enable":false,"isDefault":false,"key":"signingMode","name":"签约模式(改成全局配置了)","visible":false},{"editable":false,"enable":false,"isDefault":false,"key":"registCa","name":"是否注册CA(不支持修改了)","visible":false},{"editable":false,"enable":true,"isDefault":true,"key":"registerCapital","name":"注册资本","visible":true},{"editable":false,"enable":true,"isDefault":true,"key":"registeredProvCity","name":"注册省市","visible":true},{"editable":false,"enable":true,"isDefault":true,"key":"registeredAddress","name":"注册地址","visible":true},{"editable":false,"enable":true,"isDefault":true,"key":"legalAdd","name":"新增法人","visible":false},{"editable":false,"enable":true,"isDefault":true,"key":"legalDelete","name":"删除法人","visible":false},{"editable":false,"enable":true,"isDefault":true,"key":"legalName","name":"法人姓名","visible":true},{"editable":false,"enable":true,"isDefault":true,"key":"legalPhone","name":"法人手机号码","visible":true},{"editable":false,"enable":true,"isDefault":true,"key":"legalEmail","name":"法人邮箱","visible":true},{"editable":false,"enable":true,"isDefault":true,"key":"legalCertificationType","name":"法人证件类型","visible":true},{"editable":false,"enable":true,"isDefault":true,"key":"legalCertificationNo","name":"法人证件号码","visible":true},{"editable":false,"enable":false,"isDefault":false,"key":"legalCertificationPeriod","name":"法人证件有效期","visible":false},{"editable":false,"enable":true,"isDefault":true,"key":"authorAdd","name":"新增客户管理员","visible":false},{"editable":false,"enable":true,"isDefault":true,"key":"authorDelete","name":"删除客户管理员","visible":false},{"editable":false,"enable":true,"isDefault":true,"key":"authorName","name":"客户管理员姓名","visible":true},{"editable":false,"enable":true,"isDefault":true,"key":"authorPhone","name":"客户管理员手机号","visible":true},{"editable":false,"enable":true,"isDefault":false,"key":"authorEmail","name":"客户管理员邮箱","visible":true},{"editable":false,"enable":true,"isDefault":true,"key":"authorCertificationNo","name":"客户管理员证件号","visible":true},{"editable":false,"enable":true,"isDefault":true,"key":"authorCertificationType","name":"客户管理员证件类型","visible":true},{"editable":false,"enable":false,"isDefault":false,"key":"authorCertificationPeriod","name":"客户管理员证件有效期","visible":false},{"editable":true,"enable":true,"isDefault":false,"key":"intraGroupCompany","name":"是否集团内","visible":true},{"editable":true,"enable":true,"isDefault":false,"key":"paidInCapital","name":"实缴资本","visible":true},{"editable":true,"enable":true,"isDefault":false,"key":"custScale","name":"企业规模","visible":true},{"editable":true,"enable":true,"isDefault":false,"key":"industryInvolved","name":"所属行业","visible":true},{"editable":true,"enable":true,"isDefault":false,"key":"businessProvCity","name":"经营省市","visible":true},{"editable":true,"enable":true,"isDefault":false,"key":"businessAddress","name":"经营地址","visible":true},{"editable":false,"enable":false,"isDefault":false,"key":"certificationNo","name":"统一社会信用代码","visible":false},{"editable":false,"enable":false,"isDefault":false,"key":"establishmentTime","name":"成立日期","visible":false},{"editable":false,"enable":false,"isDefault":false,"key":"custBuildType","name":"开户方式","visible":false},{"editable":false,"enable":false,"isDefault":false,"key":"custFormerName","name":"曾用名","visible":false},{"editable":false,"enable":false,"isDefault":false,"key":"workersNo","name":"员工人数","visible":false},{"editable":false,"enable":false,"isDefault":false,"key":"custProfile","name":"企业简介","visible":false},{"editable":true,"enable":true,"isDefault":false,"key":"contactUserName","name":"联系人","visible":true},{"editable":true,"enable":true,"isDefault":false,"key":"contactTel","name":"联系电话","visible":true},{"editable":true,"enable":true,"isDefault":false,"key":"custEmail","name":"联系邮箱","visible":true},{"editable":true,"enable":true,"isDefault":false,"key":"contactProvCity","name":"联系省市","visible":true},{"editable":true,"enable":true,"isDefault":false,"key":"contactAddress","name":"联系地址","visible":true},{"editable":false,"enable":false,"isDefault":false,"key":"invoicingAdd","name":"新增开票信息","visible":false},{"editable":false,"enable":false,"isDefault":false,"key":"invoicingDelete","name":"删除开票信息","visible":false},{"editable":true,"enable":true,"isDefault":false,"key":"invoicingName","name":"开票名称","visible":true},{"editable":true,"enable":true,"isDefault":false,"key":"invoicingTaxpayerNo","name":"开票纳税人识别号","visible":true},{"editable":true,"enable":true,"isDefault":false,"key":"invoicingDepositBank","name":"开票开户行名称","visible":true},{"editable":true,"enable":true,"isDefault":false,"key":"invoicingAccountNo","name":"开票开户行账号","visible":true},{"editable":true,"enable":true,"isDefault":false,"key":"invoicingTel","name":"开票电话","visible":true},{"editable":true,"enable":true,"isDefault":false,"key":"invoicingEmail","name":"开票邮箱","visible":true},{"editable":true,"enable":true,"isDefault":false,"key":"invoicingAddress","name":"开票地址","visible":true},{"editable":true,"enable":false,"isDefault":false,"key":"invoicingDepositBankHeadName","name":"开票联行号-总行名称","visible":false},{"editable":true,"enable":false,"isDefault":false,"key":"invoicingDepositBankHeadProvinceCity","name":"开票联行号-省市名称","visible":false},{"editable":true,"enable":false,"isDefault":false,"key":"invoicingDepositBankBranchName","name":"开票联行号-支行名称","visible":false},{"editable":true,"enable":false,"isDefault":false,"key":"invoicingDepositBankNo","name":"开票联行号-联行号","visible":false}]',
        },
        'defaultKeywordList': [
            'custName',
            'companyTypes',
            'managerId',
            'parentCompany',
            'certificationPeriod',
            'affiliatedCompany',
            'registerCapital',
            'registeredProvCity',
            'registeredAddress',
            'legalName',
            'legalPhone',
            'legalEmail',
            'legalCertificationType',
            'legalCertificationNo',
            'authorName',
            'authorPhone',
            'authorCertificationNo',
            'authorCertificationType',
        ],
        'nonDefaultKeywordList': [
            'authorEmail',
            'intraGroupCompany',
            'paidInCapital',
            'custScale',
            'industryInvolved',
            'businessProvCity',
            'businessAddress',
            'contactUserName',
            'contactTel',
            'custEmail',
            'contactProvCity',
            'contactAddress',
            'invoicingName',
            'invoicingTaxpayerNo',
            'invoicingDepositBank',
            'invoicingAccountNo',
            'invoicingTel',
            'invoicingEmail',
            'invoicingAddress',
        ],
        'sceneType': '多级流转',
        'enable': 'yes',
        'custDataApproval': 'OUTSIDE_GROUP',
        'custDataApprovals': [
            'OUTSIDE_GROUP',
        ],
        'extData': {
            'signModel': 'ON_LINE',
        },
    },
    'legalId': '1833105527432179713',
    'legalName': '法人',
    'legalPhone': '13049000001',
    'legalCertificationType': 'CRET_ID',
    'legalCertificationNo': '440309199004131478',
    'legalPeriodDTO': {
        'start': '1900-01-01',
        'end': '9999-12-31',
        'status': 'YES',
    },
    'authorId': '1833109846352519169',
    'authorName': '法人',
    'authorCellPhone': '13049000001',
    'authorCertificationType': 'CRET_ID',
    'authorCertificationNo': '440309199004131478',
    'authorEmail': '13049000001@qq.com',
    'authorPeriodDTO': {
        'start': '1900-01-01',
        'end': '9999-12-31',
        'status': 'YES',
    },
    'productServiceEnums': [
        'ACFLOW',
    ],
    'certificationWay': 'INVITE',
    'inputWay': 'PLATFORM',
    'registCaResult': 'no',
    'authUserInfos': [
        {
            'id': '1833109846352519169',
            'ssoId': '1057',
            'userName': '13049000001',
            'realName': '法人',
            'cellphone': {
                'value': '13049000001',
            },
            'certificateNo': {
                'value': '440309199004131478',
            },
            'certificateType': 'CRET_ID',
            'certificationStartTime': '1900-01-01',
            'certificationEndTime': '9999-12-31',
            'timePermanent': 'YES',
            'certificationPeriodDTO': {
                'start': '1900-01-01',
                'end': '9999-12-31',
                'status': 'YES',
            },
            'orgType': 'ORG',
            'email': '13049000001@qq.com',
            'enable': 'yes',
            'createId': '1354413032731525125',
            'createName': '管理员',
            'createTime': '2024-09-09 19:46:59',
            'updateId': '1354413032731525125',
            'updateName': '管理员',
            'updateTime': '2024-09-09 19:46:59',
        },
    ],
    'dataChangeHash': 'f0hotsgo',
    'f34a3f63': {},
    'f1un01n5': {
        'modelCode': 'MA001',
        'catgId': 'A0006',
        'busiKey': '1833103470227062786',
        'sceneType': 'mediaType',
        'fileLength': 1,
        'files': [
            {
                'id': '1833110162452045826',
                'name': '9842c436-bd15-448b-9a51-38c1dddfa665.jpg',
                'url': 'https://jinkoscf-sp-dev2.llsstd.com/lls-fs/7482b59286cc5e314c5f01c87a86f6213e3d734f19cef7f57f4ea4b1dce2e703691299540140455582f1523383591df4ce5ba8eccb8cc248fcb633a801364c458034f74290f0112b62ec977e44c2440cd6495001940a72d1083dbbb320a2df76984dda68b2d3551ac739af9e37618e07d6fe84d6875a9b285f16e1c54068e098',
                'filePath': '/jinkoscf/202409/09/19/1833110161474772993.jpg',
                'fileExtension': 'jpg',
                'uid': 1725882494976,
                'status': 'success',
            },
        ],
    },
    'custScale': None,
    'contactProvCity': {},
    'businessProvCity': {},
    'industryInvolved': None,
    'contactUserName': None,
    'contactTel': None,
    'custProfile': None,
    'invoiceAccountInfo': {
        'accountName': '中软国际',
        'invoicingTaxpayerNo': '9144030027940776XM',
        'accountNo': None,
        'telephone': None,
        'email': None,
        'address': None,
        'custAccountBankBaseDTO': {
            'bankBranchId': '',
            'bankBranchName': '',
            'bankCode': '',
            'bankCodeName': '',
            'bankNo': '',
            'bankProvName': '广东省',
            'bankProvCode': '440000',
            'bankCityName': '深圳市',
            'bankCityCode': '440300',
        },
    },
}

response = requests.post(
    'https://jinkoscf-agw-dev2.llsstd.com/cust-web/acflowCustInfo/submitCustInfo',
    params=params,
    cookies=cookies,
    headers=headers,
    json=json_data,
)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"id":"1833103470227062786","orgId":"0000000001","orgName":"0","custNo":"CUST202409090174","custName":"中软国际","custShortName":"","portalNo":"00000000001","custEnglishName":"","certificationNo":"9144030027940776XM","businessLicenseStartTime":"2011-09-08","businessLicenseEndTime":"2031-09-07","timePermanent":"NO","custFormerName":"","taxpayerIdentificationNo":"","organizationStructureCode":"","establishmentTime":"2011-09-08","registerCapital":"100000","paidInCapital":"","workersNo":"","registeredProvCity":{"provinceName":"广东省","province":"440000","cityName":"深圳市","city":"440300"},"registProvince":"广东省","registProvinceCode":"440000","registCity":"深圳市","registCityCode":"440300","registeredAddress":"注册地址","businessProvince":"","businessProvinceCode":"","businessCity":"","businessCityCode":"","businessAddress":"","contactProvince":"","contactProvinceCode":"","contactCity":"","contactCityCode":"","contactAddress":"","custEmail":"","status":"ADD","managerName":"","managerOrgId":"1","managerOrgName":"1","enable":"yes","createId":"1354413032731525125","createName":"管理员","createTime":"2024-09-09 19:29:50","updateName":"管理员","updateTime":"2024-09-09 19:46:59","updateId":"1354413032731525125","companyTypes":["CORE","SUPPLIER"],"companyType":"CORE","signingMode":"ON_LINE","autoCustBuild":"NO","level":"","certificationPeriodDTO":{"start":"2011-09-08","end":"2031-09-07","status":"NO"},"intraGroupCompany":"NO","custBuildStatus":"INIT","custBuildType":"AGW_BUILD","custBuildSource":"SELF","registCa":"yes","custSettingConfig":{"id":"2","settingNo":"NO1111111","custBuildAudit":"yes","signingMode":"ON_LINE","channelAudit":"test","faceCheck":"no","faceCount":3,"smallAuthentication":"no","changeCustBuildAudit":"yes","maxApplyRemitCount":5,"maxRemitMistakeCount":5,"keyword":{"custKeyInfoList":"[{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"custName\\",\\"name\\":\\"企业名称\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"companyTypes\\",\\"name\\":\\"企业角色\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"managerId\\",\\"name\\":\\"业务经理\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"parentCompany\\",\\"name\\":\\"关联母公司\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"certificationPeriod\\",\\"name\\":\\"营业执照有效期\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"affiliatedCompany\\",\\"name\\":\\"挂靠企业\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":false,\\"isDefault\\":false,\\"key\\":\\"signingMode\\",\\"name\\":\\"签约模式(改成全局配置了)\\",\\"visible\\":false},{\\"editable\\":false,\\"enable\\":false,\\"isDefault\\":false,\\"key\\":\\"registCa\\",\\"name\\":\\"是否注册CA(不支持修改了)\\",\\"visible\\":false},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"registerCapital\\",\\"name\\":\\"注册资本\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"registeredProvCity\\",\\"name\\":\\"注册省市\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"registeredAddress\\",\\"name\\":\\"注册地址\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"legalAdd\\",\\"name\\":\\"新增法人\\",\\"visible\\":false},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"legalDelete\\",\\"name\\":\\"删除法人\\",\\"visible\\":false},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"legalName\\",\\"name\\":\\"法人姓名\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"legalPhone\\",\\"name\\":\\"法人手机号码\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"legalEmail\\",\\"name\\":\\"法人邮箱\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"legalCertificationType\\",\\"name\\":\\"法人证件类型\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"legalCertificationNo\\",\\"name\\":\\"法人证件号码\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":false,\\"isDefault\\":false,\\"key\\":\\"legalCertificationPeriod\\",\\"name\\":\\"法人证件有效期\\",\\"visible\\":false},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"authorAdd\\",\\"name\\":\\"新增客户管理员\\",\\"visible\\":false},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"authorDelete\\",\\"name\\":\\"删除客户管理员\\",\\"visible\\":false},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"authorName\\",\\"name\\":\\"客户管理员姓名\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"authorPhone\\",\\"name\\":\\"客户管理员手机号\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"authorEmail\\",\\"name\\":\\"客户管理员邮箱\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"authorCertificationNo\\",\\"name\\":\\"客户管理员证件号\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":true,\\"isDefault\\":true,\\"key\\":\\"authorCertificationType\\",\\"name\\":\\"客户管理员证件类型\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":false,\\"isDefault\\":false,\\"key\\":\\"authorCertificationPeriod\\",\\"name\\":\\"客户管理员证件有效期\\",\\"visible\\":false},{\\"editable\\":true,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"intraGroupCompany\\",\\"name\\":\\"是否集团内\\",\\"visible\\":true},{\\"editable\\":true,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"paidInCapital\\",\\"name\\":\\"实缴资本\\",\\"visible\\":true},{\\"editable\\":true,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"custScale\\",\\"name\\":\\"企业规模\\",\\"visible\\":true},{\\"editable\\":true,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"industryInvolved\\",\\"name\\":\\"所属行业\\",\\"visible\\":true},{\\"editable\\":true,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"businessProvCity\\",\\"name\\":\\"经营省市\\",\\"visible\\":true},{\\"editable\\":true,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"businessAddress\\",\\"name\\":\\"经营地址\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":false,\\"isDefault\\":false,\\"key\\":\\"certificationNo\\",\\"name\\":\\"统一社会信用代码\\",\\"visible\\":false},{\\"editable\\":false,\\"enable\\":false,\\"isDefault\\":false,\\"key\\":\\"establishmentTime\\",\\"name\\":\\"成立日期\\",\\"visible\\":false},{\\"editable\\":false,\\"enable\\":false,\\"isDefault\\":false,\\"key\\":\\"custBuildType\\",\\"name\\":\\"开户方式\\",\\"visible\\":false},{\\"editable\\":false,\\"enable\\":false,\\"isDefault\\":false,\\"key\\":\\"custFormerName\\",\\"name\\":\\"曾用名\\",\\"visible\\":false},{\\"editable\\":false,\\"enable\\":false,\\"isDefault\\":false,\\"key\\":\\"workersNo\\",\\"name\\":\\"员工人数\\",\\"visible\\":false},{\\"editable\\":false,\\"enable\\":false,\\"isDefault\\":false,\\"key\\":\\"custProfile\\",\\"name\\":\\"企业简介\\",\\"visible\\":false},{\\"editable\\":true,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"contactUserName\\",\\"name\\":\\"联系人\\",\\"visible\\":true},{\\"editable\\":true,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"contactTel\\",\\"name\\":\\"联系电话\\",\\"visible\\":true},{\\"editable\\":true,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"custEmail\\",\\"name\\":\\"联系邮箱\\",\\"visible\\":true},{\\"editable\\":true,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"contactProvCity\\",\\"name\\":\\"联系省市\\",\\"visible\\":true},{\\"editable\\":true,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"contactAddress\\",\\"name\\":\\"联系地址\\",\\"visible\\":true},{\\"editable\\":false,\\"enable\\":false,\\"isDefault\\":false,\\"key\\":\\"invoicingAdd\\",\\"name\\":\\"新增开票信息\\",\\"visible\\":false},{\\"editable\\":false,\\"enable\\":false,\\"isDefault\\":false,\\"key\\":\\"invoicingDelete\\",\\"name\\":\\"删除开票信息\\",\\"visible\\":false},{\\"editable\\":true,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"invoicingName\\",\\"name\\":\\"开票名称\\",\\"visible\\":true},{\\"editable\\":true,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"invoicingTaxpayerNo\\",\\"name\\":\\"开票纳税人识别号\\",\\"visible\\":true},{\\"editable\\":true,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"invoicingDepositBank\\",\\"name\\":\\"开票开户行名称\\",\\"visible\\":true},{\\"editable\\":true,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"invoicingAccountNo\\",\\"name\\":\\"开票开户行账号\\",\\"visible\\":true},{\\"editable\\":true,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"invoicingTel\\",\\"name\\":\\"开票电话\\",\\"visible\\":true},{\\"editable\\":true,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"invoicingEmail\\",\\"name\\":\\"开票邮箱\\",\\"visible\\":true},{\\"editable\\":true,\\"enable\\":true,\\"isDefault\\":false,\\"key\\":\\"invoicingAddress\\",\\"name\\":\\"开票地址\\",\\"visible\\":true},{\\"editable\\":true,\\"enable\\":false,\\"isDefault\\":false,\\"key\\":\\"invoicingDepositBankHeadName\\",\\"name\\":\\"开票联行号-总行名称\\",\\"visible\\":false},{\\"editable\\":true,\\"enable\\":false,\\"isDefault\\":false,\\"key\\":\\"invoicingDepositBankHeadProvinceCity\\",\\"name\\":\\"开票联行号-省市名称\\",\\"visible\\":false},{\\"editable\\":true,\\"enable\\":false,\\"isDefault\\":false,\\"key\\":\\"invoicingDepositBankBranchName\\",\\"name\\":\\"开票联行号-支行名称\\",\\"visible\\":false},{\\"editable\\":true,\\"enable\\":false,\\"isDefault\\":false,\\"key\\":\\"invoicingDepositBankNo\\",\\"name\\":\\"开票联行号-联行号\\",\\"visible\\":false}]"},"defaultKeywordList":["custName","companyTypes","managerId","parentCompany","certificationPeriod","affiliatedCompany","registerCapital","registeredProvCity","registeredAddress","legalName","legalPhone","legalEmail","legalCertificationType","legalCertificationNo","authorName","authorPhone","authorCertificationNo","authorCertificationType"],"nonDefaultKeywordList":["authorEmail","intraGroupCompany","paidInCapital","custScale","industryInvolved","businessProvCity","businessAddress","contactUserName","contactTel","custEmail","contactProvCity","contactAddress","invoicingName","invoicingTaxpayerNo","invoicingDepositBank","invoicingAccountNo","invoicingTel","invoicingEmail","invoicingAddress"],"sceneType":"多级流转","enable":"yes","custDataApproval":"OUTSIDE_GROUP","custDataApprovals":["OUTSIDE_GROUP"],"extData":{"signModel":"ON_LINE"}},"legalId":"1833105527432179713","legalName":"法人","legalPhone":"13049000001","legalCertificationType":"CRET_ID","legalCertificationNo":"440309199004131478","legalPeriodDTO":{"start":"1900-01-01","end":"9999-12-31","status":"YES"},"authorId":"1833109846352519169","authorName":"法人","authorCellPhone":"13049000001","authorCertificationType":"CRET_ID","authorCertificationNo":"440309199004131478","authorEmail":"13049000001@qq.com","authorPeriodDTO":{"start":"1900-01-01","end":"9999-12-31","status":"YES"},"productServiceEnums":["ACFLOW"],"certificationWay":"INVITE","inputWay":"PLATFORM","registCaResult":"no","authUserInfos":[{"id":"1833109846352519169","ssoId":"1057","userName":"13049000001","realName":"法人","cellphone":{"value":"13049000001"},"certificateNo":{"value":"440309199004131478"},"certificateType":"CRET_ID","certificationStartTime":"1900-01-01","certificationEndTime":"9999-12-31","timePermanent":"YES","certificationPeriodDTO":{"start":"1900-01-01","end":"9999-12-31","status":"YES"},"orgType":"ORG","email":"13049000001@qq.com","enable":"yes","createId":"1354413032731525125","createName":"管理员","createTime":"2024-09-09 19:46:59","updateId":"1354413032731525125","updateName":"管理员","updateTime":"2024-09-09 19:46:59"}],"dataChangeHash":"f0hotsgo","f34a3f63":{},"f1un01n5":{"modelCode":"MA001","catgId":"A0006","busiKey":"1833103470227062786","sceneType":"mediaType","fileLength":1,"files":[{"id":"1833110162452045826","name":"9842c436-bd15-448b-9a51-38c1dddfa665.jpg","url":"https://jinkoscf-sp-dev2.llsstd.com/lls-fs/7482b59286cc5e314c5f01c87a86f6213e3d734f19cef7f57f4ea4b1dce2e703691299540140455582f1523383591df4ce5ba8eccb8cc248fcb633a801364c458034f74290f0112b62ec977e44c2440cd6495001940a72d1083dbbb320a2df76984dda68b2d3551ac739af9e37618e07d6fe84d6875a9b285f16e1c54068e098","filePath":"/jinkoscf/202409/09/19/1833110161474772993.jpg","fileExtension":"jpg","uid":1725882494976,"status":"success"}]},"custScale":null,"contactProvCity":{},"businessProvCity":{},"industryInvolved":null,"contactUserName":null,"contactTel":null,"custProfile":null,"invoiceAccountInfo":{"accountName":"中软国际","invoicingTaxpayerNo":"9144030027940776XM","accountNo":null,"telephone":null,"email":null,"address":null,"custAccountBankBaseDTO":{"bankBranchId":"","bankBranchName":"","bankCode":"","bankCodeName":"","bankNo":"","bankProvName":"广东省","bankProvCode":"440000","bankCityName":"深圳市","bankCityCode":"440300"}}}'.encode()
#response = requests.post(
#    'https://jinkoscf-agw-dev2.llsstd.com/cust-web/acflowCustInfo/submitCustInfo',
#    params=params,
#    cookies=cookies,
#    headers=headers,
#    data=data,
#)
