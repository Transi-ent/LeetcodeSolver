import copy
class Solution:

    def reconstructQueue(self, people: list) -> list:

        people.sort(key= lambda p: p[1])
        people.sort(key=lambda p: p[0], reverse=True)

        tmp = copy.deepcopy(people)
        for i, ps in enumerate(tmp):
            # print("===")
            if i==ps[1]:
                continue
            people.pop(i)
            people.insert(ps[1], ps)

        print(people)
        return people

a=[[7,0],[4,4],[7,1], [5,0],[6,1],[5,2]]
print('=============')
print("...")
Solution().reconstructQueue(a)
