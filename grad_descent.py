import numpy as np
import matplotlib.pyplot as plt




def gradient_descent(x, y, m_init, b_init, lr, iterations):
    x=np.array(x)
    y=np.array(y)
    m_curr = m_init
    b_curr = b_init
    lr = lr
    n = len(x)

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = 1 / n * sum([val ** 2 for val in (y - y_predicted)])
        d_m = -(2 / n) * sum(x * (y - y_predicted))
        d_b = -(2 / n) * sum(y - y_predicted)
        m_curr = m_curr - lr * d_m
        b_curr = b_curr - lr * d_b
        print("iterations {}, m {}, b {},cost {}".format(iterations, m_curr, b_curr, cost))

    return m_curr, b_curr




if __name__=='__main__':

    """TODO : animate graph"""

    x_points = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    y_points = [1, 2, 3, 1, 4, 5, 6, 4, 7, 10, 15, 9]

    m,b =gradient_descent(x_points, y_points, 0, 0, 0.01, 1000)

    plt.plot(x_points,y_points,'ro')
    plt.plot(x_points,[(m*x + b) for x in x_points],'b')
    plt.show()




