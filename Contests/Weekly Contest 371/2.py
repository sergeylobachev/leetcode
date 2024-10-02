from collections import defaultdict

def solution(access_times):
    a = access_times
    d = defaultdict(list)
    answer = []

    for employee, timestamp in a:
        time = int(timestamp[:2]) * 60 + int(timestamp[2:])
        d[employee].append(time)

    for employee in d:
        times = d[employee]
        times.sort()
        N = len(times)

        for start in range(N-2):
            if times[start+1] - times[start] < 60 and times[start+2] - times[start] < 60:
                answer.append(employee)
                break
    
    return answer
 







access_times = [["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]]
access_times = [["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]]
access_times = [["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]]
print(solution(access_times))
