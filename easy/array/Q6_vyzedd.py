#My dumb solution

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = []

        if len(nums1) >= len(nums2):
            temp = nums2[:]
            for i in temp:
                if (i in nums2) and (i in nums1):
                    res.append(i)
                    nums2.pop(nums2.index(i))
                    nums1.pop(nums1.index(i))
        
        else:
            temp = nums1[:]
            for i in temp:
                if (i in nums2) and (i in nums1):
                    res.append(i)
                    nums2.pop(nums2.index(i))
                    nums1.pop(nums1.index(i))
                    
        return res

#Smarter solution from internet -> Two Pointers, ignore which array is longer

class Solution(object):
    def intersect(self, nums1, nums2):

        nums1, nums2 = sorted(nums1), sorted(nums2)
        pt1 = pt2 = 0
        res = []

        while True:
            try:
                if nums1[pt1] > nums2[pt2]:
                    pt2 += 1
                elif nums1[pt1] < nums2[pt2]:
                    pt1 += 1
                else:
                    res.append(nums1[pt1])
                    pt1 += 1
                    pt2 += 1
            except IndexError:
                break

        return res


