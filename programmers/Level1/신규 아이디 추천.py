#3 4 5 11 15
id=input()
#1단계
id=id.lower()
new_list=""
answer=""
not_banned=["-","_","."]

print(id)

#2단계
for i in id:
    if i.isdigit() or i.isalpha() or i in not_banned:
        new_list += i
print(new_list,len(new_list))
#3단계
answer=new_list
new_list=answer[0]
for i in range(1,len(answer)):
    if answer[i]=='.':
        if answer[i-1]!='.':
            new_list+=answer[i]
    else:
        new_list+=answer[i]
print(new_list)
#4단계
if new_list[0]=='.' and len(new_list)==1:
    new_list=''
elif new_list[0]=='.':
    new_list=new_list[1:]
elif new_list[-1]=='.':
    new_list=new_list[:-1]
print(new_list)
#5단계
if not len(new_list):
    new_list='a'
else:
    new_list=new_list[:15]
print(new_list)
#6단계

if new_list[-1]=='.':
    new_list=new_list[0:-1]
while(len(new_list)<3):
    new_list+=new_list[-1]

print(new_list)