def solution(n, lost, reserve):
    #set은 중복 허용 X, -로 차집합 가능 
    set_r = set(reserve) - set(lost)
    set_l = set(lost) - set(reserve)
    
#     print("res",set_r)
#     print("lost",set_l)
    
    #여분이 있는 경우 
    for i in set_r:
        #앞 사람한테 빌려줌 
        if i-1 in set_l:
            set_l.remove(i-1)
        #뒷 사람한테 빌려줌 
        elif i+1 in set_l:
            set_l.remove(i+1)
    return n - len(set_l)