import requests
from pprint import pprint

def create_YD_files(yd_token, file_name):
    auth = {'Authorization': f'OAuth {yd_token}'}
    create_file = requests.put(f'https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2F{file_name}',
                            headers=auth)
    response = create_file.json()
    return response

class TestYDAPI: 
    def setup(self):
        print("method setup")
    def analysis(self):
        print("method analysis")
    def test_create_files(self):
        assert create_YD_files('correct_token', '111')['method'] == 'GET'
    def test_create_same_file(self):
        assert create_YD_files('correct_token', '111')['message'] == 'По указанному пути "disk:/111" папка с таким именем существует .'
    def test_wrong_token(self):
        assert create_YD_files('wrong_token', '111')['description'] == 'Unauthorized'

if __name__ == '__main__':
    yd_token = ''
    file_name = '111'
    response = create_YD_files(yd_token,file_name)