student_data = [
    {'name': 'Алексей', 'scores': [85, 92, 78, 95]},
    {'name': 'Марина', 'scores': [65, 70, 58, 82]},
    {'name': 'Светлана', 'scores': [98, 95, 100]}
]
def calculate_average_score(scores, ignore_lowest=False): # если ignore_lowest = True, отбрасывает наименьшую оценку
    scores_to_use = scores.copy()
    if ignore_lowest and len(scores_to_use) > 1: # если нужно игнорировать наименьшую оценку и оценок больше одной
        scores_to_use.remove(min(scores_to_use))
    average = sum(scores_to_use) / len(scores_to_use) #считаем ср.балл
    return average
for student in student_data: # вычисляем средний балл учитывая все оценки
    average = calculate_average_score(student['scores'])
    print(f"{student['name']}: {average}")
for student in student_data: # вычисляем отбрасывая худшую оценку
    average = calculate_average_score(student['scores'], ignore_lowest=True)
    print(f"{student['name']}: {average}")