#function for pi digits
def pi_digits():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(5000): 
        if 4 * q + r - t < m * t:
            yield m #pause
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


digits = pi_digits()
pi_list = []
pi_array = []

for i in pi_digits():
    pi_array.append(str(i))

pi_array = pi_array[:1] + ['.'] + pi_array[1:]
pi_string = "".join(pi_array)
print("Pi string:\n %s" % pi_string)

pi_string[:1000]
