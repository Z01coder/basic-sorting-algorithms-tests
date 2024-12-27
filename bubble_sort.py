from main import data

# Пузырьковая сортировка

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Сортировка пузырьком
sorted_data_bubble = bubble_sort(data.copy())
print("Отсортированный пузырьком:", sorted_data_bubble)





