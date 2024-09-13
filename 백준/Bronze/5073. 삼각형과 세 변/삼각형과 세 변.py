while True:
    leg1, leg2, leg3 = map(int, input().split())
    
    if leg1 == 0 and leg2 == 0 and leg3 == 0:
        break
        
    Max_leg = max(leg1, leg2, leg3)
    
    if Max_leg >= leg1 + leg2 + leg3 - Max_leg:           # sum()은 iterable 자료형만 받는다
        print("Invalid")
    else:
        num_of_equal_legs = len(set([leg1, leg2, leg3]))  # set()도 마찬가지이다
        
        if num_of_equal_legs == 1:
            print("Equilateral")
        elif num_of_equal_legs == 2:
            print("Isosceles")
        else:
            print("Scalene")