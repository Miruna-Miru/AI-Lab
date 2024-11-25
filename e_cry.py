from itertools import permutations

def solve_crpt(expression):
    letters=set(c for c in expression if c.isalpha())
    if (len(letters)>10):
        print("More unique letters !!!")
        return None
    if "=" not in expression or "+" not in expression:
        print("Invalid Expression")
        return None
    
    left_side,right_side=expression.split("=")
    left_side=left_side.strip()
    right_side=right_side.strip()

    for perm in permutations(range(10),len(letters)):
        letter_to_digit=dict(zip(letters,perm))

        def replace_letter(expression,mapping):
            return "".join(str(mapping.get(c,c)) for c in expression)
        
        try:
            left_value=replace_letter(left_side,letter_to_digit)
            right_value=replace_letter(right_side,letter_to_digit)

            lef_eval=sum(int(replace_letter(part,letter_to_digit)) for part in left_value.split("+"))
            right_eval=int(right_value)

            def has_leading_zeros(s):
                return s[0]=="0" and len(s)>1
            
            if all(not has_leading_zeros(part) for part in left_value.split("+")+[right_value]):
                if lef_eval==right_eval:
                    return letter_to_digit
                
        except Exception as e:
            continue
    return "No solution found"

exp=input("Enter expression :  ")
res=solve_crpt(exp)
if  isinstance(res,dict):
    print("Solution found!")
    print(res)
else:
    print(res)
        
