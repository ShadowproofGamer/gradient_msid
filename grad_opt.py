import numpy as np


def gradient_descent(

    gradient, start, learn_rate, n_iter=50, tolerance=1e-03, change=lambda n:1, orig_func=lambda vec:vec[0]+vec[1]

):

    i=0
    vector = np.array(start)
    print("dane początkowe - vector: {}, tolerancja: {}, ".format(vector, tolerance))

    prev_stop=9999999999999
    #prev_vec = np.array(9999, 9999)
    for _ in range(n_iter):

        diff = -learn_rate* change(i+1) * np.array(gradient(vector))
        #print(diff)
        stop = ((diff[0])**2+(diff[1])**2 + (orig_func(vector)-orig_func(vector+diff))**2)**(1/2)
        
        i+=1
        vector += diff

        stop2 = orig_func(vector) 
        if (stop <= tolerance 
        #    or stop2>prev_stop
            ):
            if(orig_func):
                print("iteracja: {}, x1,x2: {}, wynik: {}, stop: {}".format(i, vector, orig_func(vector), stop))
            else:
                print("iteracja: {}, x1,x2: {}, stop: {}".format(i, vector, stop))
            break

        
        
        prev_stop=stop2
        print("iteracja: {}, warunek stop: {}<{}, result: {}, diff:{}, wynik:{}".format(i, stop, tolerance, vector, np.array(gradient(vector)), orig_func(vector)))
    
    return vector

#lista4

#zad3
#f3 = x1**2 + x2**2

#gradient_descent(lambda vec: [2*(vec[0]), 2*(vec[1])], [4.0, 4.0], 0.03, 500, 0.01, lambda n:n, (lambda vec:vec[0]**2 + vec[1]**2))

#zad4
#f4 = 2.5(vec[0]**2 -vec[1])**2 + (1 -vec[0])**2
#deriv4 = lambda vec: [10*vec[0]**3 + vec[0]*(2-10*vec[1])-2, -5*(vec[0]**2 - vec[1])]
#func4 = lambda vec: 2.5*((vec[0]**2 -vec[1])**2) + (1 -vec[0])**2

#gradient_descent(deriv4, [-0.5, 1.0], 0.0007, 500, 0.001, lambda n:n, func4)
#gradient_descent(deriv4, [-0.5, 1.0], 0.000701, 500, 0.001, lambda n:n, func4)
#gradient_descent(deriv4, [-0.5, 1.0], 0.03, 500, 0.001, lambda n:n**(1/2), func4)
#gradient_descent(deriv4, [-0.5, 1.0], 0.03, 500, 0.001, lambda n:n**(1/4), func4)


#lista7
#zad 3
func_7_3 = lambda vec: 3*(vec[0]**2 - vec[1])**2 + 2*(1-vec[1])**2
deriv_7_3 = lambda vec:[12*vec[0]*(vec[0]**2 - vec[1]), -6*vec[0]**2 + 10*vec[1] - 4]
gradient_descent(deriv_7_3, [0.5, 1], 0.2, 50, 0.01, lambda n:1, func_7_3)













def gradient_descent_2d(

    gradient, start, learn_rate, n_iter=50, tolerance=1e-03, r_iter=2, r=1

):
    k=0
    x, y = start
    prev_x = x
    prev_y = y
    for _ in range(n_iter):
        
        temp_grad = gradient(x, y, k*0.1)
        print("krok {}, grad: {}".format(k, temp_grad))
        diff = [-learn_rate * temp_grad[0], -learn_rate * temp_grad[1]]
        
        stop = ((diff[0])**2 + (diff[1])**2)**(1/2)
        #if np.all(np.abs(diff) <= tolerance): break
        if stop <= tolerance: break

        x+= diff[0]
        y+= diff[1]
        k+= 1
        #learn_rate*=0.98
        #r*=r_iter

    print("iteracja: {}, warunek stop: {}<{}, result: {}, {}".format(k, stop, tolerance, x, y))
    return x, y






#lista 5
#zad2 gradient
#grad2=lambda x1, x2: [x2*(x2-1)*(2*x2-1)+4*r*(x1**2 -2*x1+x2**2)*(x1-1), x2*(x2-1)*(2*x2-1)+4*r*(x1**2 -2*x1+x2**2)*(x2)]
#def grad2(x1, x2, r=0.05):
#    if((x1**2 -2*x1 + x2**2)>0):
#        return [x2*(x2-1)*(2*x2-1)+4*r*(x1**2 -2*x1+x2**2)*(x1-1), x2*(x2-1)*(2*x2-1)+4*r*(x1**2 -2*x1+x2**2)*(x2)]
#    else:
#        return [x2*(x2-1)*(2*x2-1), x2*(x2-1)*(2*x2-1)]
#
#def orig_func2(vector):
#    x1, x2 = vector
#    print("wynik: ", (x1-1)*(x2-1)*x1*x2)
#
#orig_func2(gradient_descent_2d(grad2, (2, 2), 0.01, 5000, 0.0001, 1.05, 0.1))
#
#
#
#
#
#
#
##zad3
#def grad3(x1, x2, r=0.05, r_iter=1):
#    r*=r_iter
#    if((x1**2 -2*x1 + x2**2)>0):
#        return [x2*(x2-1)*(2*x2-1)+4*r*(x1**2 -2*x1+x2**2)*(x1-1), x2*(x2-1)*(2*x2-1)+4*r*(x1**2 -2*x1+x2**2)*(x2)]
#    else:
#        return [x2*(x2-1)*(2*x2-1), x2*(x2-1)*(2*x2-1)]
#
#def orig_func3(vector):
#    x1, x2 = vector
#    print("wynik: ", (x1-1)*(x2-1)*x1*x2)
