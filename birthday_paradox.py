import random 

def paradox(n=None):

    def cumples(p=24, n=10000):
        repeti = 0
        for i in range(n):
            cumples = [random.randint(1,365) for i in range(p)]
            for dia in cumples:
                if dia in cumples[dia+1:]:
                    repeti +=1
                    break
        return f'%{repeti /n*100}'

    if n == None:
        for x in range(5,55,5):
            print(f'\nFor {x} people there are: {cumples(p=x)} of a repeted birthday.')
    else:
        print(f'\nFor {n} people there are: {cumples(n)} of a repeted birthday.')
            



paradox(24)