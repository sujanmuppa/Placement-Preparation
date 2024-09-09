# def question1(X, A):
#     ans = A*1
#     count = 0
#     while ans <= X:
#         ans = A*count
#         req = X - ans
#         if req == 0:
#             break
#         if count % req == 0 and ans < X:
#             return (count, req)
#         count += 1
#     return (-1, -1)

# print(question1(10, 3))

# def question3(str):
#     variables = []
#     operation = []
#     for i in str:
#         if not i.isalpha() and len(variables) < 2:
#             variables.append(i)
#         elif i.isalpha() and len(operation) < 1:
#             operation.append(i)
#         if len(variables) == 2 and len(operation) == 1:
#             if operation[0] == 'A':
#                 temp = int(variables[0]) & int(variables[1])
#                 variables = [temp]
#                 operation = []
#                 print(temp)
#             elif operation[0] == 'B':
#                 temp = int(variables[0]) | int(variables[1])
#                 variables = [temp]
#                 operation = []
#                 print(temp)
#             elif operation[0] == 'C':
#                 temp = int(variables[0]) ^ int(variables[1])
#                 variables = [temp]
#                 operation = []
#                 print(temp)
#     return variables[0]


# print(question3("1A0B1C1"))

# class Solution:

#     def merge(self, nums, start, mid1, mid2, end):
#         print("Before merge", nums[start:end+1])
#         inversions = 0
#         ptr1 = start 
#         ptr2 = mid2
#         result = []
#         offset = 0
#         while ptr1 <= mid1 and ptr2 <= end:
#             if nums[ptr1] > nums[ptr2]:
#                 offset += 1
#                 inversions += offset
#                 offset = 0
#                 result.append(nums[ptr2])
#                 ptr2+=1
#             else:
#                 inversions += offset
#                 result.append(nums[ptr1])
#                 ptr1+=1
#         while ptr1 <= mid1:
#             result.append(nums[ptr1])
#             ptr1+=1
#         while ptr2 <= end:
#             result.append(nums[ptr2])
#             ptr2 += 1 
#         count = 0
#         for i in range (start, end+1):
#             nums[i] = result[count]
#             count += 1 
#         print("Result", result) 
#         print("After merge", nums[start:end+1])
#         return inversions 
            

#     def mergeSort(self, nums, start, end):
#         inversions = 0
#         if start < end:
#             mid = (start+end)//2
#             inversions += self.mergeSort(nums, start, mid)
#             print(nums[start:mid+1], "inversions", inversions)
#             inversions1 = self.mergeSort(nums, mid+1, end)
#             print(nums[mid+1:end+1], "inversions", inversions1)
#             inversions += inversions1
#             inversions += self.merge(nums, start, mid, mid+1, end)
#             print(nums[start:end+1], "inversions", inversions)
#         return inversions 

#     def numberOfInversions(self, nums):
#         n = len(nums)
#         return self.mergeSort(nums, 0, n-1)
    
# sol = Solution()
# print(sol.numberOfInversions([2, 4, 1, 3, 5]))

# class Solution:
#     def merge(self, nums, start, mid, end):
#         inversions = 0
#         left = start 
#         right = mid+1 
#         result = []
#         while left <= mid and right <= end:
#             while right <= end and nums[left] > 2*nums[right]:
#                 right += 1
#             inversions += right - mid - 1
#             left += 1
#             print("Inversions", inversions, left, right)
#         while left <= mid:
#             result.append(nums[left])
#             left += 1
#         while right <= end:
#             result.append(nums[right])
#             right += 1
#         count = 0
#         for i in range(start, end+1):
#             nums[i] = result[count]
#             count += 1
#         return inversions 

#     def mergeSort(self, nums, start, end):
#         inversions = 0
#         if start < end:
#             mid = (end + start)//2
#             inversions += self.mergeSort(nums, start, mid)
#             inversions += self.mergeSort(nums, mid+1, end)
#             inversions += self.merge(nums, start, mid, end)
#         return inversions 
#     def reversePairs(self, nums):
#         return self.mergeSort(nums, 0, len(nums)-1)

class Solution:
    def merge(self, nums, start, mid, end):
        inversions = 0
        left = start 
        right = mid+1 
        result = []
        while left <= mid and right <= end:
            if nums[left] < nums[right]:
                result.append(nums[left])
                left+=1
            else:
                result.append(nums[right])
                right+=1
        while left <= mid:
            result.append(nums[left])
            left += 1
        while right <= end:
            result.append(nums[right])
            right += 1

        
        left = start 
        right = mid+1
        while left <= mid and right <= end:
            while right <= end and nums[left] > 2*nums[right]:
                right += 1
            print("Inversions", "inversions" ,inversions,"left", left,"right", right, "array", nums[start:end+1])
            inversions += right - (mid + 1)
            left += 1

        count = 0
        for i in range(start, end+1):
            nums[i] = result[count]
            count += 1
        return inversions 

    def mergeSort(self, nums, start, end):
        inversions = 0
        if start < end:
            mid = (end + start)//2
            inversions += self.mergeSort(nums, start, mid)
            inversions += self.mergeSort(nums, mid+1, end)
            inversions += self.merge(nums, start, mid, end)
        return inversions 
    def reversePairs(self, nums):
        return self.mergeSort(nums, 0, len(nums)-1)
    
sol = Solution()
print(sol.reversePairs([6, 4, 1, 2, 7]))