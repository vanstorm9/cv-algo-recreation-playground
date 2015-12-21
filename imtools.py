from PIL import Image
from numpy import *
from pylab import *

def imresize(im,sz):
    ''' Resize an array using PIL '''
    pil_im = Image.fromarray(uint8(im))

    return array(pil_im.resize(sz))
    
def histeq(im, nbr_bins=256):
    ''' Histogram equalizaation'''

    # Get image histogram
    imhist, bins = histogram(im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum() # cuumulative distribution function
    cdf = 255 * cdf / cdf[-1] # normalize

    # use linear interpolation of cdf to find new pixel values
    im2 = interp(im.flatten(), bins[:-1],cdf)
    
    return im2.reshape(im.shape), cdf

def pca(X):
    '''
    Principal Component Analysis
    
    input: X, matrix with training data stored as flattened arrays in rows
    return: projection matrix (with important dimensions first), variance and mean
    '''

    # get dimensions
    num_data, dim = X.shape

    # center data
    mean_X = X.mean(axis=0)

    if dim > num_data:
        # PCA - compact trick used
        M = dot(X,X.T) # covariance matrix
        e, EV = linalg.eig(M) # eigenvalues and eigenvectors
        tmp = dot(X.T,EV).T # this is the compact trick
        V = tmp[::-1] # reverse since last eigenvector are the ones we want
        S = sqrt(e)[::-1] # reverse since eigenvalues are in increasing order

        for i in range(V.shape[1]):
            V[:,i] /= S
    else:
        # PCA -SVD used
        U,S,V = linag.svd(X)
        V = V[:num_data] # only makes sense to return the first num_data

        # return the projection matrix, the variance and the mean
        return V,S,mean_X
