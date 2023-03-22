##### A #####

def my_func(x1, x2, x3):

        if isinstance(x1,float) and isinstance(x2,float) and isinstance(x3,float):
            if (x1+x2+x3) == 0:
                return('Not a number – denominator equals zero')
            else:
                return(((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3))
        else:
            if isinstance(x1,int) or isinstance(x2,int) or isinstance(x3,int):
                return ('Error: parameters should be float')
            else:
                return None


print(my_func(2,1.0,2.0))


