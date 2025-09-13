def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i]  # Текущий элемент для вставки
        j = i - 1  # Индекс предыдущего элемента

        # Сдвигаем элементы больше key вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Сдвигаем элемент вправо
            j -= 1

        # Вставляем key на правильную позицию
        arr[j + 1] = key

    return arr