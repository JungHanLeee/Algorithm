def solution(new_id):
    #1단계
    new_id=new_id.lower()
    new_list=""
    answer=""
    not_banned=["-","_","."]
#2단계
    for i in new_id:
        if i.isdigit() or i.isalpha() or i in not_banned:
            new_list+=i
#3단계
    for i in range(len(new_list)):
        new_list = new_list.replace('..', '.')
#4단계
    if new_list[0]=='.' and len(new_list)==1:
        new_list=''
    elif new_list[0]=='.':
        new_list=new_list[1:]
    elif new_list[-1]=='.':
        new_list=new_list[:-1]
#5단계
    if not len(new_list):
        new_list='a'
    else:
        new_list=new_list[:15]
#6단계
    if new_list[-1]=='.':
        new_list=new_list[0:-1]
    while(len(new_list)<3):
        new_list+=new_list[-1]

    return new_list