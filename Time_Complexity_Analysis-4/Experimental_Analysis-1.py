import time
# Try it all on problems and algorithms
# Merge Sort
def merge(a1, a2 ,a):
    i = 0
    j = 0
    k = 0
    while(i < len(a1) and j < len(a2)): # Comparision of elements of 2 lists
        if(a1[i] < a2[j]):
            a[k] = a1[i]
            k += 1
            i += 1

        else:
            a[k] =a2[j]
            k += 1
            j += 1

    while (i < len(a1)): # Adding data in first list
        a[k] = a1[i]
        k += 1
        i += 1

    while (j < len(a2)):  # Adding data in second list
        a[k] = a2[j]
        k += 1
        j += 1

def mergeSort(a):
        n = len(a)
        if (n == 0 or n == 1):
            return -1

        mid = (n) // 2
        a1 = a[0:mid]
        a2 = a[mid:]

        mergeSort(a1)
        mergeSort(a2)

        merge(a1, a2, a)


# Selection Sort
def selection_sort(a):
    for i in range(len(a)):
        mid_idx = 1
        for j in range(i + 1, len(a)):
            if(a[mid_idx] > a[j]):
                mid_idx = j
        a[i], a[mid_idx] = a[mid_idx], a[i]        

def create_rev_array(n):
    a = []
    for i in range(n, 0, -1):
        a.append(i)
    return a 


n = 100000


# a = create_rev_array(n) # start time
# start = time.time()

# mergeSort(a) # stop time
# end = time.time()

# print(n, end - start)


# a = create_rev_array(n) # start time
# start = time.time()

# selection_sort(a) # stop time
# end = time.time()

# print(n, end - start)



