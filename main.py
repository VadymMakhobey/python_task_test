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



