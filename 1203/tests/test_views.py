from mock_data import CONFIG_VALUE_COMPLETE_DATA, CONFIG_VALUE_DATA_PORTFOLIO_LIST


class AESCipher(object):

    def decrypt(self, value):
        return str(value)


class TestViews(object):
    def test_index(self, client,mocker):

        mocker.patch('app.views.read_data_store', return_value=CONFIG_VALUE_COMPLETE_DATA)
        test_obj = AESCipher()
        mocker.patch('app.views.AESCipher', return_value=test_obj)
        mocker.patch('app.views.render_template', return_value="Get Called")
        url = '/' or '/index'
        response = client.get(url)
        assert response.get_data() == "Get Called"

    def test_index_portfolio_list(self, client, mocker):
        mocker.patch('app.views.read_data_store', return_value=CONFIG_VALUE_DATA_PORTFOLIO_LIST)
        test_obj = AESCipher()
        mocker.patch('app.views.AESCipher', return_value=test_obj)
        mocker.patch('app.views.render_template', return_value="Get Called")
        url = '/' or '/index'
        response = client.get(url)
        assert response.get_data() == "Get Called"

    # def test_post_call(self, client, mocker):
    #     mocker.patch('app.views.read_data_store', return_value=CONFIG_VALUE_COMPLETE_DATA)
    #     test_obj = AESCipher()
    #     mocker.patch('app.views.AESCipher', return_value=test_obj)
    #     mocker.patch('app.views.render_template', return_value="Post Called")
    #     url = '/'
    #     response = client.post(url, data={"Hello": "hi", "csrf_token": False})
    #     print(response.data)
