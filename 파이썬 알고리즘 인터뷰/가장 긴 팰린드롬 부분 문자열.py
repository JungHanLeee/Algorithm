class Solution:
    def longestPalindrome(self, s: str) -> str:
        a=list(s)
        b=list(reversed(a))
        c=[0]*len(a)
        cnt=0
        for i in range(len(a)):
            if ord(a[i])==ord(b[i]):
                c[i]+=1
            else:
                continue
        for i in range(len(c)):
            if c[i]>0:
                c[i]=a[i]
            else:
                cnt+=1
        for i in range(cnt):
            c.remove(0)
        result1="".join(c)
        return result1
f=Solution()
s1="babad"

print(f.longestPalindrome(s1))
#모범답안1
def longestPalindrome(self,s:str)->str:
    #팰린드롬 판별 및 투 포인터 확장
    def expand(left:int,right:int)->str:
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    #해당사항 없을 때 빠르게 리턴
    if len(s)<2 or s==s[::-1]:
        return s
    result=''

    #슬라이딩 윈도우 우측으로 이동
    for i in range(len(s)-1):
        result=max(result,
                   expand(i,i+1),
                   expand(i,i+2),
                   key=len)
    return result