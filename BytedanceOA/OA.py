#1 Plus one

def Solution(m):
    digit= 1
    res= 0
    for i in m[::-1]:
        res+= i* digit
        digit*= 10
    return str(res+ 1)

#2



#3
class Solution(object):
    def Solution(startTime, duration):
        end = float('-inf')
        res= len(startTime)
        for i in sorted(zip(startTime, duration), key=lambda i:i[0]+ i[1]):
            if i[0]>= end:
            	end= i[0]+ i[1]
            else:
            	res-= 1
        return res

    Solution([3, 1, 5],[2, 2, 2])

#4
def Solution(s, k):
    res= []
    def dfs(ss, path):
        if not ss:
            res.append(path)
        for i in range(1, len(ss)+ 1):
            if 0< int(ss[:i])<= k:
                dfs(ss[i:], path+ [int(ss[:i])])
    dfs(s, [])
    return len(set([tuple(t) for t in res]))