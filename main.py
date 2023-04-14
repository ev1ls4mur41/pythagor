def find_pythagorean_triples(n):
    # Инициализация списка для хранения троек
    triples = []
    # Перебор всех возможных комбинаций a, b и c
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            for c in range(b + 1, n + 1):
                # Проверка условия чисел Пифагора
                if a ** 2 + b ** 2 == c ** 2:
                    # Добавление тройки в список
                    triples.append((a, b, c))
    # Возврат списка троек
    return triples

n = int(input("Введите количество троек: "))
triples = find_pythagorean_triples(n)
print(f"Найдено {len(triples)} троек:")
for triple in triples:
    print(triple)