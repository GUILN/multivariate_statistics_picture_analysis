import random
import numpy as np

def select_random_images(total_images: int, number_of_images: int) -> list:
    """
    total_images: Total number of images in the dataset.
    number_of_images: Number of images to be selected.
    
    Selects random images from the dataset.
    """
    random_images_numbers = random.sample(range(1, total_images), number_of_images)
    frontal = [f"{i}a.jpg" for i in random_images_numbers]
    side = [f"{i}b.jpg" for i in random_images_numbers]
    return frontal + side
   
def mlda(X,ns,nt,n):
    assert n <= ns-1, "Reduction of dimension (n) invalid." 
    assert n <= X.shape[1], "Reduction of dimension (n) invalid."
    assert n > 0, "Reduction of dimension (n) invalid."
    O = np.ones((X.shape[0],1)) 
    H = np.repeat(np.eye(ns),nt,axis=0).T
    M = np.mean(X,axis=0)
    # Mg = meang(X,ns,nt)
    # W = X - np.dot(H,Mg)
    # Sw = np.dot(W.T,W)
    # B = np.dot(H,Mg) - np.dot(O,M)
    # Sb = np.dot(B.T,B)
    # Sp = Sw/(X.shape[0]-ns)
    # p = Sp.shape[0]
    # Ip = (np.trace(Sp)/p)*np.eye(p)
    # Sm = mecs(Sp,Ip)
    # Sw = Sm*(X.shape[0]-ns)
    # Qv, Qa = np.linalg.eig(np.dot(np.linalg.inv(Sw),Sb))
    # Ks = np.sort(np.diag(Qa))
    # Ki = np.flipud(np.argsort(np.diag(Qa)))
    # L = Qv[:,Ki[0:n]]
    # K = np.flipud(Ks[0:n])