
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
