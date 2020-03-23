def containsNearbyAlmostDuplicate( nums: list, k: int, t: int) -> bool:
    left, right, s = 0, 0, set()
    while right < len(nums):
        if nums[right] in s:
            return True
        for i in s:
            if abs(i - nums[right])<=t:
                return True
        else:
            s.add(nums[right])

        if right - left < k:
            right += 1
        else:
            s.remove(nums[left])
            left += 1
            right += 1

    return False


def containsNearbyAlmostDuplicate2( nums: list, k: int, t: int) -> bool:
    #TODO: XXXXX 一个桶只能放一个元素，
    if t<0: return False

    n, d, w = len(nums), {}, t+1
    #分别为元素个数，存放元素的桶组， 桶的宽度

    for i in range(n):
        key = nums[i] // w
        if key in d:
            return True
        if key - 1 in d and abs(nums[i] - d[key-1]) < w:
            return True
        if key + 1 in d and abs(nums[i] - d[key+1]) < w:
            return True

        d[key] = nums[i]
        if i>=k:
            del d[nums[i-k]//w]

    return False
