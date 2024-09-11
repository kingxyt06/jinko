
class TestLogin:

    def test_login(self,get_agw_token):
        login_res = get_agw_token
        print(login_res)
        assert login_res != None