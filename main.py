from data.data_direct import data_direct
from data.data_doc import data_doc   
from funcs import *
import pytest
from pytest_mock import mock
import builtins
import json

class TestDataOrganizer: 
    def setup(self):
        print("method setup")
    def analysis(self):
        print("method analysis")
    def test_shelf_search(self):
        with open('files/data_direct.json', 'r', encoding='utf-8') as f:
            test_dir = json.load(f)
        with mock.patch.object(builtins, 'input', lambda _: '12-3'):
            assert shelf_search() == list(test_dir.keys())[0]
    def test_people_search(self):
        with open('files/data_doc.json', 'r', encoding='utf-8') as f:
            test_doc = json.load(f)
        with mock.patch.object(builtins, 'input', lambda _: '12345'):
            assert people_search() == test_doc[2]['name']
    def test_add_new_doc(self):
        assert add_new_doc('doc_type', 'some_id', 'new_name', '1') == 'документ doc_type some_id new_name был добавлен на  полку 1'
    def test_doc_delete(self):
        assert doc_delete('11-2') == 'Документ 12-3 удалён'

if __name__ == '__main__':
    print(add_new_doc('doc_type', 'some_id', 'new_name', '1'))
