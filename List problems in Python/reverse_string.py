# returns a string with the words in the reverse order

def rev_words(s):
    return " ".join(reversed(s.split()))
s = 'ooeaA'

#transform to lowercase
def lower(s):
    return s.lower()


#do we have duplicates in a string?
def duplicates(s):
    return len(set(s))==len(s)


#count the number of same characters and substitute the copies with their number
#such as AAAA = 4A. Separate capital from small letters.

def subs(s):
    if len(s)==0:           #empty string
        return 0
    if len(s)==1:           #one element
        return s+str(len(s))
    cnt = 1
    out = []
    i = 1
    while i<(len(s)):
        if s[i-1]==s[i]:
            cnt+=1
        else:
            out.append(s[i-1]+str(cnt))
            cnt = 1
        i+=1
    out.append(s[len(s)-1]+str(cnt))
    return out
l = ''.join(subs(s))
       
            