
temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32,
                34, 30, 29, 25, 27, 22, 22, 23, 25, 29,
                29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot = list(filter(lambda temp: temp > 28, temperatures))

max_temp = max(hot)
min_temp = min(hot)
avg_temp = sum(hot) / len(hot)

print(f"Самая высокая температура: {max_temp}")
print(f"Самая низкая температура: {min_temp}")
print(f"Средняя температура: {avg_temp:.2f}")
