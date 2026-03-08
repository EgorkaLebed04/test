from main4 import create_folder, get_folder


def test_create_folder():
    response =  create_folder()
    assert str(response.status_code)[0] == '2'

def test_folder_in_disk():
    response = get_folder()
    assert response.json()["path"] == 'disk:/pd-fpy_140'