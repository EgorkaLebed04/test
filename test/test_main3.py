from main.main3 import solve

def test_solve_correct():
    todo_list = [
        ["Разобрать почту", 1],
        ["Обзвонить клиентов", 2],
        ["Запланировать дела на завтра", 0.6],
        ["Сделать презентацию", 3],
        ["Созвон с командой", 0.5]
    ]
    result = round(solve(todo_list), 1)
    assert result == 0.9, f"Время рассчитано неверно: {result}"

def test_solve_incorrect():
    todo_list = [
        ["Разобрать почту", 1],
        ["Обзвонить клиентов", 2],
        ["Запланировать дела на завтра", 0.6],
        ["Сделать презентацию", 3],
        ["Созвон с командой", 0.5]
    ]
    result = round(solve(todo_list), 1)
    assert result != 0.8, f"Время рассчитано неверно: {result}"