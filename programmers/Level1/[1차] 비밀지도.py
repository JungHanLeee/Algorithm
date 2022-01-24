def solution(n, arr1, arr2):
    arr1_bin=[]
    map_1=[]
    result=[]
    for i in range(n):
        arr1_bin=str(int(format(arr1[i],'b'))+int(format(arr2[i],'b')))
        map_1=""
        for j in arr1_bin:
            if j>='1':
                map_1+="#"
            else:
                map_1+=" "
        if len(map_1):
            map_1=" "*(n-len(map_1))+map_1
        result.append(map_1)
    return result