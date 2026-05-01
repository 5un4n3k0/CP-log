def input_val():
# numbers of raining terms
    n = int(input())

# data of raining terms
    terms = []
    for i in range(n):
        # input
        terms.append(list(map(int, input().split("-"))))
        
        # round
        sm = terms[i][0] % 100
        
        while sm % 5 != 0:
            sm -= 1

        terms[i][0] = terms[i][0] // 100 * 100 + sm

        em = terms[i][1] % 100

        while em % 5 != 0:
            em += 1

        if em == 60:
            em = 0
            terms[i][1] = (terms[i][1] // 100 + 1) * 100
        else:
            terms[i][1] = terms[i][1] // 100 * 100 + em
    
    return terms

def merge(terms):
    """
    結合する条件
    1. 時間範囲が全く同じだった場合
    2. 降り終わり時間が降り始め時間の後ろの場合
    3. 降り初めから降り終わりの時間の間に後ろのやつが入ってた場合
    """
    return_terms = [terms.pop(0)]

    for t in terms:
        if return_terms[-1] == t:
            continue
        elif return_terms[-1][1] > t[1]:
            continue
        elif return_terms[-1][1] > t[0]:
            return_terms[-1][1] = t[1]
            continue
        elif return_terms[-1][1] == t[0]:
            return_terms[-1][1] = t[1]
            continue 
        else:
            return_terms.append(t)
    
    return return_terms

terms = input_val()
terms = sorted(terms)
terms = merge(terms)

for t in terms:
    print("-".join(list(map(lambda x: str(x).zfill(4), t))))

