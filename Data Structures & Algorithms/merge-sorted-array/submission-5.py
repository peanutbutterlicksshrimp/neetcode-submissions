class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        e = (m+n) - 1
        while (m+n) > 0:
            if (n <= 0) or (m > 0 and nums1[m-1] >= nums2[n-1]):
                nums1[e] = nums1[m-1]
                m-=1
                print("m: ", m)
            else:
                nums1[e] = nums2[n-1]
                n-=1
                print("n: ", n)
            e-=1
