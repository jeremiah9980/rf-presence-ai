from sklearn.cluster import DBSCAN
def cluster(features):
    return DBSCAN(eps=3).fit_predict(features)
