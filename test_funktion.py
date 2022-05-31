import pytest
from main import documents, directories, name_by_number, directory_by_document, add_shelf, delete

def setup():
    pass

def teardown():
    pass

@pytest.mark.parametrize(
        'document, res_name',
        [
            ("2207 876234", 'Василий Гупкин'),
            ("11-2", 'Геннадий Покемонов'),
            ("10006", 'Аристарх Павлов'),
            ("1651", 'Такого документа не существует')
        ]
    )
def test_name_by_number(document, res_name):
    assert name_by_number(document) == res_name

@pytest.mark.parametrize(
        'document, res_directory',
        [
            ("2207 876234", '1'),
            ("11-2", '1'),
            ("10006", '2'),
            ("1651", 'Такого документа не существует')
        ]
    )
def test_directory_by_document(document, res_directory):
    assert directory_by_document(document) == res_directory

@pytest.mark.parametrize(
        'shelf, res_directory',
        [
            ("5", {'1': ['2207 876234', '11-2', '5455 028765'], '2': ['10006'], '3': [], '5': []}),
            ("1", 'Такая полка уже существует')
        ]
    )
def test_add_shelf(shelf, res_directory):
    assert add_shelf(shelf) == res_directory

@pytest.mark.parametrize(
        'document, result',
        [
            ('11-2', '11-2'),
            ('10006', '10006'),
            ('2207 876234', '2207 876234'),
            ('651', 'Такого документа не существует')
        ]
    )
def test_delete(document, result):
    assert delete(document) == result


