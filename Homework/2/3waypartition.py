#########################################
# ------------Initial State-------------
#
#                 Array
# ------------------------------------
# |          |            |          |
# |    p1    |     p2     |    p3    |
# |          |            |          |
# ------------------------------------
# ^                                  ^
# |                                  |
# l, mid                         end, r
#(also pivot but it's value, not index)



def QuickSort(a, start, end):
	# If length of array is 1
	if start>=end:
		return
	# Assigning variables
	pivot = a[start]; l=start; r=end; mid=start
    # Loop until mid index meets right index
	while mid<=r:
		# Moving value that smaller than pivot to
		# left side of mid index and
		# increasing index of left-end of partition 2
		# and mid index
		if a[mid] < pivot:
			a[l], a[mid]=a[mid], a[l]
			l+=1
			mid+=1
		# Moving value that bigger than pivot to
		# right side of mid index and
		# decreasing index of right-end of partition 2
		elif a[mid] > pivot:
			a[mid], a[r]=a[r], a[mid]
			r-=1
		# Increasing mid index
		else:
			mid+=1
	# Recursive call of QuickSort
	QuickSort(a, start, l-1)
	QuickSort(a, r+1, end)

arr=[5,7,9,0,3,1,6,2,4,8]
QuickSort(arr,0,len(arr)-1)
print(arr)