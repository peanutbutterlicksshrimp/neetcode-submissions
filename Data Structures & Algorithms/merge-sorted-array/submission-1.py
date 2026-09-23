class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for k in range(0, n):
            nums1[m+k] = nums2[k]

        print(nums1)
        for i in range(1, len(nums1)):
            j = i-1
            while nums1[i] < nums1[j] and j >= 0:
                temp = nums1[j]
                nums1[j] = nums1[i]
                nums1[i] = temp
                j-=1
                i-=1
        print(nums1)
