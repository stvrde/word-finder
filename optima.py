
from timeit import default_timer as timer
from itertools import permutations
from tqdm import tqdm

f = open("test5.txt",encoding='utf-8')


def main():

    novi=[]
    for word in f:
        if len(word)>3:
            word=word.strip()
            novi.append(word)
    
    print('kraj = 1')
    slova=0
    while slova != '1':
        print()
        slova = input("Unesi slova: ")
        print('3 ',end="")
        start = timer()
        #trazi sve permutacije pocetnog stringa od 3 char i vece i zapisuje u listu 'b'
        b=[''.join(perm) for length in tqdm(range(3, len(slova) + 1)) for perm in permutations(slova, length)]        
        br = 4
        broj = 0
        presjek=list(set(novi).intersection(b))#nade presjek od set(b) i set(novi) i ispise sve sta se poklapa
        presjek.sort()
        # malo lipsi ispis isto kosta nesto vrimena
        for s in sorted(presjek,key=len):
            if (len(s) < br) & (broj < 4):
                broj+=1            
                print("|",s ,'', end="")                
            elif (len(s) < br) & (broj >= 4):
                broj=0
                print()                
                string=(br*'--------')
                string=string[0 : (6-br*2)-br+5]
                print(string)
                print(br-1,"|",s,'', end="")
            else:
                broj=0
                print('\n\n\n')
                print(br,"|",s,'', end="")
                br+=1
        end = timer()
        print('\n\n')
        print('Uneseno',len(slova), "slova.\n\n")
        print('Timer: ',end - start)
    

if __name__=='__main__':
    main()