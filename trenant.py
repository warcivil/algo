def levenstains(words, words2, lena, lenb):  # 1
    if(lena == 0 or lenb == 0):  # 2
        return max(lena, lenb)  # 2
    elif(words[lena-1] == words2[lenb-1]):  # 1
        return levenstains(words, words2, lena-1, lenb-1)  # x
    else:
        return 1 + min(
            levenstains(words, words2, lena, lenb-1),  # x
            levenstains(words, words2, lena-1, lenb),  # x
            levenstains(words, words2, lena-1, lenb-1),  # x
        )
#O(N*M) - difficult


def binary_search(value, left, right, mas):
    mid = (left + right)//2  # 2
    while(left < right):
        if(mas[mid] < value):  # [1, 2, 3]
            left += mid+1  # []
        elif(mas[mid] > value):
            right -= mid-1
        else:
            return mid
        mid = (left + right)//2
    return None
# O(log n)

# smaless sort


def find_small(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in arr:
        if(i<smallest):
            smallest = i
            smallest_index =arr.index(i)
    return smallest_index
def selection_sort(arr):
    sort_mas = []
    while arr:
        smalest = find_small(arr)
        sort_mas.append(arr.pop(smalest))
    return sort_mas
# O(N^2)

def fact(number):
    if(number == 0):
        return 1
    else:
        return number * fact(number-1)
# O(N)

def sumarray(array, length):
    if(length == 0): return array[length]
    else:
        return array[length] + sumarray(array, length-1)
# O(N)

def counter(arr):
    if(arr == []):
        return 0
    else:
        return 1 + counter(arr[1:])
# O(N)

def quick_sort(arr):
    if (len(arr) < 2):
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if pivot <= i] # 
        greater = [i for i in arr[1:] if pivot > i]
        return quick_sort(greater) + [pivot] + quick_sort(less)
# O(NlogN) -> O(N^2)

cache = {}
from random import randint
def tryCache(url):
    global cache
    if(cache.get(url)):
        return cache[url]
    else:
        cache[url] = randint(1, 100)
        return cache[url]
# O(1)
