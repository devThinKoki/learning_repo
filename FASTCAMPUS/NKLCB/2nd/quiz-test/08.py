# 리스트 a의 크기를 N이라고 할 때, 아래의 시간복잡도는?
def proob3(a: list[int]):
    answer = []
    for x in a:
        b = list(map(lambda b: b**x, a))
        print(b)
        for y in b:
            print(set(a))
            if y in set(a):
                answer += y # 에러 발생
    return answer
print(proob3([2,3,5,7]))
O(N^2)

# 해시충돌을 방지하기 위한 코드를 작성하기.
class HashSet:
    def __init__(self, table_size = 16, hash_fnc = None):
        if hash_fnc is None:
            self.hash_fnc = hash
        else:
            self.hash_fnc = hash_fnc
        
        self.table_size = table_size
        self.table = [None]*table_size
        
    def add(self, data):
        ind = self.hash_fnc(data) % self.table_size
        if self.table[ind] is None or self.table[ind] == data:
            self.table[ind] = data
        else:
            # 해시 충돌 방지를 위한 코드: self.table[ind]에 다른 값이 있을 때,
            while self.table[ind]:
                ind = (ind+1) % self.table_size
            self.table[ind] = data
        return 
    def search(self, data):
        ind = self.hash_fnc(data) % self.table_size
        prob_ind = ind
        while self.table[prob_ind]:
            print('going on')
            if self.table[prob_ind] == data:
                print('found in index: ', prob_ind)
                return True
            prob_ind = (prob_ind + 1) % self.table_size
            # 한바퀴를 순회하였다면... 
            if prob_ind == ind:
                break

        # 해당 해쉬주소에 값이 없다면, False 리턴
        return False

# hs = HashSet(4)
# print(hs.table_size)
# print(hs.table)
# ind1 = hash('da') % 4
# ind2 = hash('ak') % 4
# ind3 = hash('dc') % 4
# ind4 = hash('dqwe') % 4
# print(ind1,ind2,ind3,ind4)
# hs.add('da')
# print(hs.table)
# hs.add('ak')
# print(hs.table)
# hs.add('dc')
# print(hs.table)
# hs.add('dqwe')
# print(hs.table)
# hs.search('da')
# hs.search('ak')
# hs.search('dc')
# hs.search('dqwe')