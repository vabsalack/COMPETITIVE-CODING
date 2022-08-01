def mergesort(arr):

    if len(arr) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(arr)//2
        l = arr[:r]
        m = arr[r:]

        #  sort the two halves

        mergesort(l)
        mergesort(m)

        i = j = k = int()

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]

        length_l = len(l)
        length_m = len(m)

        while i < length_l and j < length_m:

            if l[i] < m[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = m[j]
                j += 1

            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]

        while i < length_l:
            arr[k] = l[i]
            i += 1
            k += 1

        while j < length_m:
            arr[k] = m[j]
            j += 1
            k += 1

        
