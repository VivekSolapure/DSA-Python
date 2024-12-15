# for i in range(3):
#             for j in range(i):
#                 print('*',end=' ')
#             print()

class Test:
    def __init__(self,loop):
        self.loop=loop



    def Right_Angled_Triangle(a):
        '''
        * 
        * * 
        * * * 
        * * * * 
        '''
        for i in range(a):
            for j in range(i+1):
                print('*',end=' ')
            print()
    def Right_Angled_Number_Pyramid(a):
        '''
        1 
        1 2 
        1 2 3 
        1 2 3 4     
        '''
        for i in range(a):
            for j in range(i+1):
                print(j+1,end=' ')
            print()
    def Right_Angled_Number_Pyramid_2(a):
        '''
        1 
        2 2
        3 3 3
        4 4 4 4
        '''
        for i in range(a):
            for j in range(i+1):
                print(i+1,end=' ')
            print()
    def Inverted_Right_Pyramid(a):
        '''
        * * * * 
        * * *
        * *
        *
        '''
        for i in range(a):
            for j in range(a):
                print('*',end=' ')
            a-=1
            print()
    def Inverted_Numbered_Right_Pyramid(a):
        '''
        1 2 3 4 
        1 2 3
        1 2
        1
        '''
        for i in range(a):
            for j in range(a):
                print(j+1,end=' ')
            a-=1
            print()
    def Star_Pyramid(a):
        '''
          *
         ***
        *****
        '''
        a=3
        for i in range(a):
            for j in range(a-i-1):
                print("s",end='')
            for k in range(2*i+1):
                print('*',end='')
            # for l in range(a-i-1):
            #     print(' ',end='')
            print()
    def Inverted_Star_Pyramid(a):
        '''
        *****
         ***
          *
        '''
        a=3
        for i in range(a):
            for j in range(i):
                print(" ",end='')
            for k in range(2*a-1):
                print('*',end='')
            for l in range(i):
                print(' ',end='')
            a-=1
            print()
    def Diamond_Star_Pattern(a):
        '''
          *  
         ***
        *****
        *****
         ***
          *
        '''
        a=3
        for i in range(a):
            for j in range(a-i-1):
                print(" ",end='')
            for k in range(2*i+1):
                print('*',end='')
            for l in range(a-i-1):
                print(' ',end='')
            print()
        for i in range(a):
            for j in range(i):
                print(" ",end='')
            for k in range(2*a-1):
                print('*',end='')
            for l in range(i):
                print(' ',end='')
            a-=1
            print()
    def Half_Diamond_Star_Pattern(a):
        '''
        * 
        * *
        * * *
        * *
        *
        '''
        Test.Right_Angled_Triangle(3)
        Test.Inverted_Right_Pyramid(2)
    def Binary_Number_Triangle_Pattern():
        '''
        0
        10
        010
        '''
        a=3
        start=1
        end=0
        for i in range(a):
            if(i%2==0):
                start=1
            if(i%2==1):
                start=0
            for j in range(i+1):
                start=1-start
                print(start,end='')
            print()
    def Number_Crown_Pattern():
        '''
        1      1
        12    21
        123  321
        12344321
        '''
        n=4
        for i in range(n):
            space=n+2
            for j in range(i+1):
                print(j+1,end='')

            for k in range(space):
                print(' ',end='')
            ll=i+1
            for l in range(i+1):
                print(ll,end='')
                ll-=1
            n-=2
          
            print()
    def Increasing_Number_Triangle_Pattern():
        '''
        1
        23
        456
        78910
        1112131415
        '''
        n=5
        num=1
        for i in range(n):
            for j in range(i+1):
                print(num,end='')
                num+=1
            print()
            
    def Increasing_Letter_Triangle_Pattern():
        '''
        A
        AB
        ABC
        ABCD
        '''
        n=4
        for i in range(n):
            jj=65
            for j in range(i+1):
                print('%c'%jj,end='')
                jj+=1
            print()
    def Reverse_Letter_Triangle_Pattern():
        '''
        A B C D E F
        A B C D E 
        A B C D
        A B C
        A B
        A
        '''
        n=4
        for i in range(n):
            char=65
            for j in range(n):
                print('%c'%char,end='')
                char+=1
            n-=1
            print()
    def Alpha_Ramp_Pattern():
        '''
        A 
        B B
        C C C
        D D D D
        E E E E E
        F F F F F F
        '''
        n=5
        jj=65
        for i in range(n):
            for j in range(i+1):
                print('%c'%jj,end='')
            jj+=1
            print()
    def Alpha_Hill_Pattern():
        '''
             A     
            ABA    
           ABCBA   
          ABCDCBA  
         ABCDEDCBA 
        ABCDEFEDCBA
        '''
        # print('aaa',int(3/2)+1)
        n=3
        for i in range(n):
            char=65
            for j in range(n-i-1):
                print(" ",end='')
            part1=(((2*i+1)/2)-1)
            for k in range(2*i+1):
                print('%c'%char,end=' ')
                if k<=part1: 
                    char+=1
                else: 
                    char-=1
            print()
    def Alpha_Triangle_Pattern():
        '''
        C 
        C B
        C B A
        '''
        n=3
        add=n-1
        for i in range(n):
            char=65+add
            for j in range(i+1):
                print('%c'%char,end=' ')
                char-=1
            n-=1
            print()
    def Symmetric_Void_Pattern():
        '''
        **********
        ****  ****
        ***    ***
        **      **
        *        *
        *        *
        **      **
        ***    ***
        ****  ****
        **********
        '''
        n=5
        s1=n
        for i in range(s1):
            for j in range(s1):
                print("*",end='')
            for k in range(i+1):
                if(k>0):
                    print("  ",end='')    
            for j in range(s1):
                print("*",end='')        
            s1-=1
            print()
        s1=1
        for i in range(n):            
            for j in range(s1):
                print("*",end='')
            for k in range(n):
                if(k>0):
                    print("  ",end='')    
            for j in range(s1):
                print("*",end='')   
            s1+=1 
            n-=1
            print()
    def Symmetric_Butterfly_Pattern():
        '''
        *            *
        **          **
        ***        ***
        ****      ****
        *****    *****
        ******  ******
        **************
        ******  ******
        *****    *****
        ****      ****
        ***        ***
        **          **
*            *
        '''
        n=7
        space=n*2-2
        for i in range(n):
            for j in range(i+1):
                print('*',end='')
            for k in range(space):
                print(" ",end='')
            for l in range(i+1):
                print('*',end='')
            space-=2
            print()
        space=2
        for i in range(n):
            for j in range(n-1):
                print('*',end='')
            for k in range(space):
                print(' ',end='')
            for l in range(n-1):
                print('*',end='')
            space+=2
            n-=1
            print()
    def Hollow_Rectangle_Pattern():
        '''
        ******
        *    *
        *    *
        *    *
        *    *
        ******
        '''
        n=6
        # for i in range(n):
        #     if(i==0):
        #         for j in range(n):
        #             print('*',end='')
        #         print()    
        #     if(i>0 and i<n-1):                
        #         print('*',end='')
        #         for k in range(n-2):
        #             print(' ',end='')
        #         print('*')
        #     if(i==n-1 and i>0):
        #         for j in range(n):
        #             print('*',end='')
        for i in range(n):
            for j in range(n):
                if(j==0 or i==0 or i==n-1 or j==n-1):
                    print('*',end='')
                else:print(' ',end='')
            print()
        
    
            
        
    def test(self):
        Test.Hollow_Rectangle_Pattern()
obj1=Test(5)
print(obj1.test())