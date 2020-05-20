import numpy as np

def make_cluster(pos=None, num=None, r=None):

    if pos is None:
        return

    if num is None:
        return

    if r is None:
        return

    
    theta = np.random.uniform(0, 2 * np.pi, [num, 1])
    dr = np.random.uniform(0, r, [num, 1])

    dx = dr * np.cos(theta)
    dy = dr * np.sin(theta)
    x = pos[0] + dx
    y = pos[0] + dy

    X = np.hstack([x, y])
    print(np.shape(X))
   
    return X