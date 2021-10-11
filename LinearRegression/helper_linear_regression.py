import numpy as np
import matplotlib.pyplot as plt

def getXY(coefs, datalength, noise):
    x = np.arange(datalength)
    y = np.zeros(x.shape)

    for i, c in enumerate(coefs):
        y += c * (x**i)
    mul = np.max(y) - np.min(y)
    y = [yi + mul * (noise * (2 * np.random.rand() - 1)) for yi in y]
    return np.asarray(x), np.asarray(y)

def plot_fitting_lin(x, y, Th0, Th1):
    fig = plt.figure()
    plt.scatter(x, y)
    y_min = Th0 + Th1 * x.min()
    y_max = Th0 + Th1 * x.max()

    plt.plot([x.min(), x.max()], [y_min, y_max], 'k--', lw=4, color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('y = {} + {} * x'.format(Th0, Th1))

def testcomputeh(compute_h):
    x = np.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    try:
        compute_h(x, 200, -15)
    except NameError:
        print ('The "compute_h" function does not exist, or returns an error.')
    else:
        res = compute_h(x, 200, -15)
        print ("Testing results: ", res)
        if np.array_equal(res, np.array([200,185,170,155,140,125,110,95,80,65])):
            print ("Your code seems to be OK!")
        else:
            print ("There is something wrong with your code. Please check it.")

    
def testcost(cost):
    a = np.asarray([1, 2, 3, 4, 5])
    b = np.asarray([2, 4, 6, 8, 10])
    
    try:
        cost(a, b)
    except NameError:
        print ('The "cost" function does not exist, or returns an error.')
    else:
        if (cost(a, b) == 5.5) and (cost(a, a) == 0) and (cost(b, a) == 5.5):
            print ('Your code seems to be OK!')
        else:
            print ('There is something wrong with your code. Please check it.')
            
def testcomputederivatives(compute_derivatives):
    a = np.arange(10)
    b = a + 1
    dTh0, dTh1 = compute_derivatives(a, b, 0, 1)
    if dTh0 == -1:
        print ('dTh0 seems to be OK.')
    elif dTh0 == 1:
        print('Incorrect result for dTh0. Probably you forgot the "-" in your formula :).')
    else:
        print('Incorrect result for dTh0.')

    if dTh1 == -4.5:
        print ('dTh1 seems to be OK.')
    elif dTh1 == 4.5:
        print('Incorrect result for dTh1. Probably you forgot the "-" in your formula :).')
    else:
        print('Incorrect result for dTh1.')


def testupdatetheta(update_theta):
    t0, t1 = update_theta(10, 4, 5, 2, 0.1)
    if t0 == 9.5:
        print ('theta0 seems to be OK.')
    elif t0 == 10.5:
        print('Incorrect theta0 result. Probably you mistook "-" and "+" in your formula :).')
    elif t0 == 0.5:
        print('Incorrect theta0 result. Probably you fotgot to subtract the results from previous theta0.')        
    else:
        print('Incorrect theta0 result.')

    if t1 == 3.8:
        print ('theta1 seems to be OK.')
    elif t1 == 4.2:
        print('Incorrect theta1 result. Probably you mistook "-" and "+" in your formula :).')
    elif t1 == 0.2:
        print('Incorrect theta1 result. Probably you fotgot to subtract the results from previous theta1.')        
    else:
        print('Incorrect theta1 result.')

            
            
def perform_learning(learning_rate, epochs, compute_h, compute_del, update_theta):
    th0 = 0
    th1 = 0
    for i in range(epochs):
        del0, del1 = compute_del(x, y, th0, th1)
        th0, th1 = update_theta(th0, th1, del0, del1, learning_rate)
        if (i%display_every) == 0:        
            print('Iteration {}, Theta 0: {:.2f}, Theta 1: {:.2f}, Cost: {:.2f}'
                  .format(i, th0, th1, cost(y, compute_h(x, th0, th1))))


def display_results(i, display_every, x, y, th0, th1, compute_h, cost, cost_list, iter_list):
    if (i%display_every) == 0:
        curr_cost = cost(y, compute_h(x, th0, th1))
        cost_list.append(curr_cost)
        iter_list.append(i)
        print('Iteration {}, Theta 0: {:.2f}, Theta 1: {:.2f}, Cost: {:.2f}'
              .format(i, th0, th1, curr_cost))
    return cost_list, iter_list