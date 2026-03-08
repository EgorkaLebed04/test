from main.main1 import solve


def test_slice_true():
    result, count = solve([123, 145, 346, 246, 235, 166, 112, 351, 436])
    assert result == [346, 166, 436], f"Список чеков неверный: {result}"
    assert count == 3, f"Количество чеков неверное: {count}"

def test_slice_false():
    result, count = solve([123, 145, 346, 246, 235, 166, 112, 351, 436])
    assert result != [123, 145, 346], f"Список чеков неверный: {result}"
    assert count != 2, f"Количество чеков неверное: {count}"