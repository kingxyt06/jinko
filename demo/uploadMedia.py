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
    'llsfn-auth-token-dev': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWFsTmFtZSI6IueuoeeQhuWRmCIsImxvZ2luVGltZSI6MTcyNTg4MjQxODQ1MiwidXNlck5hbWUiOiJhZG1pbiIsImV4cCI6MTcyNTk2ODgxOCwidXNlcklkIjoiMTM1NDQxMzAzMjczMTUyNTEyNSJ9.MhXyIMN2ogEwfHG4ykDk3az47GEmzbTL2Gm49bRA1pc',
    'llsfn-auth-token-devdate': '1725882418436',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryiEDKcFPip0gcBPEV',
    # 'Cookie': 'bccpordinscfqa=eb981024-93a9-47ff-9509-7aecb5f20151; llsfn-auth-token-qa-current-login=fa54cabf0a3d9302da9da271b51af4db; llsfn-auth-token-qa-pc=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWFsTmFtZSI6IuW8oOmHkemHkSIsImxvZ2luVGltZSI6MTcyNTg2MDM5MTAxNCwidXNlck5hbWUiOiIxNTA5MDQxMTQzNyIsImV4cCI6MTcyNTk0Njc5MSwidXNlcklkIjoiMTgyMDI4MDUyNDk1NzYyMjI3MyJ9.ecxU-kWTvsQjsokC2FfqUi3ohdNgCZTxWEkaIrZ4hyE; llsfn-auth-token-qa-pcdate=1725860391069; llsfn-auth-token-qa-pc-current-login=df61d3b162e94feccb1ea98c1dc6f02d; CURRENT-LOGIN=fa54cabf0a3d9302da9da271b51af4db; llsfn-auth-token-qa=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWFsTmFtZSI6IueuoeeQhuWRmCIsImxvZ2luVGltZSI6MTcyNTg2MTQ5NDg3MCwidXNlck5hbWUiOiJhZG1pbiIsImV4cCI6MTcyNTk0Nzg5NCwidXNlcklkIjoiMTM1NDQxMzAzMjczMTUyNTEyNSJ9.4Nj5vOdNl0dUnU1_3-6OcNRzM05-0rnIeV2G9LrffRE; llsfn-auth-token-qadate=1725861494849; llsfn-auth-token-dev-current-login=fa54cabf0a3d9302da9da271b51af4db; llsfn-auth-token-dev=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZWFsTmFtZSI6IueuoeeQhuWRmCIsImxvZ2luVGltZSI6MTcyNTg4MjQxODQ1MiwidXNlck5hbWUiOiJhZG1pbiIsImV4cCI6MTcyNTk2ODgxOCwidXNlcklkIjoiMTM1NDQxMzAzMjczMTUyNTEyNSJ9.MhXyIMN2ogEwfHG4ykDk3az47GEmzbTL2Gm49bRA1pc; llsfn-auth-token-devdate=1725882418436',
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
    'modelCode': 'MA001',
    'catgId': 'A0006',
    'busiKey': '1833103470227062786',
    'userBusiKey': '',
}

files = {
    'files': ('9842c436-bd15-448b-9a51-38c1dddfa665.jpg', '', 'image/jpeg'),
}

response = requests.post(
    'https://jinkoscf-agw-dev2.llsstd.com/media-web/media/opera/do/uploadMediaFiles',
    params=params,
    cookies=cookies,
    headers=headers,
    files=files,
)
