from collections import defaultdict

def solution(word, k):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vd = defaultdict(int)
    cd = defaultdict(int)
    cd[0] = -1
    cc = 0
    vd["a"] = -1
    vd["e"] = -1
    vd["i"] = -1
    vd["o"] = -1
    vd["u"] = -1
    
    ans = 0
    
    for i in range(len(word)):
        
        ## populating data
        if word[i] in vowels:
            vd[word[i]] = i
        else:
            cc += 1
            cd[cc] = i 
        
        vmn = min(vd.values())

        if cc >= k and vmn > -1:
            l = cd[cc-k]
            if k > 0:
                r = cd[cc-k+1]
            else: r = i
            if vmn >= l:
                ans += min(vmn, r) - l

            print(f"i={i}, l={l}, r={r}, ans={ans}, vmn={vmn}")

    return ans




word = "aeioqq"
k = 1
# word = "aeiou"
# k = 0
# word = "ieaouqqieaouqq"
# k = 1
word = "auoeia"
k = 0
print(solution(word, k))
