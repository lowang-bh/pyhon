def solution(x):
    # Your code here
    if not isinstance(x, str):
        return x
    min, max = ord('a'), ord('z')
    res =[]
    for ch in x: 
        if str.islower(ch):
            res.append(chr(min + max - ord(ch)))
        else:
            res.append(ch)
            
    return "".join(res)
        
print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
            
    
