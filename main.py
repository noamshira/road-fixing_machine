print("enter string of segments")
s=input()
def solution(s):
    count=0
    i=0
    while i<len(s):
        if s[i]=='x':
            i+=3
            count+=1
        else:
            i+=1
    print(count)
solution((s))