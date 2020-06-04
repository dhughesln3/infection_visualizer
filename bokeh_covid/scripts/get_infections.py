#this calculates the probability distribution
import numpy as np

def get_infections(N, p, T, I):

    def prob(N, p, I):
        P=(1-p)**I
        Q=1-(1-p)**I
        probs=[P**(N-I)]
        for k in range(N-I):
            probs.append(((N-I-k)/(k+1))*probs[-1]*Q/P)
        return np.array(probs)

    P = np.zeros((N+1,N+1))
    for i in range(N+1):
        P[i]=np.concatenate((np.zeros(i), prob(N,p,i)))
    return (np.linalg.matrix_power(P,T))[I]

# Get expected infections

def E(arr):
    return sum([i*arr[i] for i in range(len(arr))])
