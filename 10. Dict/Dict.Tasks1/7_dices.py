from random import randint


def throw_dices():
    return randint(1, 6) + randint(1, 6)


def get_probability():
    probabilities = {}

    for _ in range(1000):
        result = throw_dices()

        if result not in probabilities:
            probabilities[result] = 1
        else:
            probabilities[result] += 1

    probabilities = dict(sorted(probabilities.items()))

    for key in probabilities:
        probabilities[key] /= 1000

    return probabilities


def get_combinations_quantity(dice_sum):
    dice1 = 1
    max = 6
    qty = 0
    while dice1 <= max and dice1 < dice_sum:
        dice2 = dice_sum - dice1
        if dice2 > 6:
            dice2 = 6
            dice1 = dice_sum - dice2
        dice1 += 1
        qty += 1
    return qty


def get_expected_probability():
    expected_probabilities = {}
    for sum in range(2, 13):
        expected_probabilities[sum] = get_combinations_quantity(sum) / 36
    return expected_probabilities


probabilities = get_probability()
expected_probabilities = get_expected_probability()

print(f"{'Sum':<7} {'Simulated %':<15} {'Expected %':<10}")
for (key1, value1), (key2, value2) in zip(probabilities.items(), expected_probabilities.items()):
    val1 = "{:.2f}".format(value1 * 100)
    val2 = "{:.2f}".format(value2 * 100)
    print(f"{key1:<8} {val1:<15} {val2:<10}")
