from datetime import datetime, timedelta

def Pythagorean_pants():
    def is_pythagorean_triplet(arr):
        arr.sort()

        # Перевірка умови Піфагора: a^2 + b^2 = c^2
        if arr[0] ** 2 + arr[1] ** 2 == arr[2] ** 2:
            return True
        else:
            return False

    # Тести
    print(is_pythagorean_triplet([5, 3, 4]))    # True
    print(is_pythagorean_triplet([6, 8, 10]))   # True
    print(is_pythagorean_triplet([100, 3, 65])) # False

def Plants_vs_Zombies():
    def battle_result(zombies, plants):
        # Перевірка різної довжини масивів
        if len(zombies) != len(plants):
            return len(zombies) > len(plants)

        # Суми сил атаки зомбі та рослин
        total_zombies_attack = sum(zombies)
        total_plants_attack = sum(plants)

        # Порівняння сум сил атаки
        if total_zombies_attack == total_plants_attack:
            # Якщо сили атаки рівні, перемагає команда з найбільшою початковою силою атаки
            return max(zombies) > max(plants)
        else:
            # Перемагає команда з більшою сумою сил атаки
            return total_zombies_attack > total_plants_attack

    # Тести
    print(battle_result([1, 3, 5, 7], [2, 4, 6, 8]))  # True
    print(battle_result([1, 3, 5, 7], [2, 4]))  # False
    print(battle_result([1, 3, 5, 7], [2, 4, 0, 8]))  # True
    print(battle_result([2, 1, 1, 1], [1, 2, 1, 1]))  # True

def Schedule_generator():
    def generate_schedule(days, work_days, rest_days, start_date):
        schedule = []
        current_date = start_date

        for _ in range(days):
            if current_date.weekday() < 5:  # Перевірка, чи це робочий день (понеділок - п'ятниця)
                schedule.append(current_date)
                work_days -= 1
            else:
                rest_days -= 1

            current_date += timedelta(days=1)

            if work_days == 0 and rest_days == 0:
                break

        return schedule

    # Параметри тесту
    days = 5
    work_days = 2
    rest_days = 1
    start_date = datetime(2020, 1, 30)

    # Тест
    result_schedule = generate_schedule(days, work_days, rest_days, start_date)
    print(result_schedule)

