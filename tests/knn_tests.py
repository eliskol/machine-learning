import sys
sys.path.insert(1, sys.path[0].replace('tests', 'src'))
from k_nearest_neighbors import KNearestNeighborsClassifier


x = [[ 0.14,       0.14,      0.28,     0.44],
 [0.10,       0.18,      0.28,     0.44],
 [0.12,       0.10,      0.33,     0.45],
 [0.10,       0.25,      0.25,     0.40],
 [0.00,       0.10,      0.40,     0.50],
 [0.00,       0.20,      0.40,     0.40],
 [0.10,       0.08,      0.35,     0.47],
 [0.00,       0.05,      0.30,     0.65],
 [0.20,       0.00,      0.40,     0.40],
 [0.25,       0.10,      0.30,     0.35],
 [0.22,       0.15,      0.50,     0.13],
 [0.15,       0.20,      0.35,     0.30],
 [0.22,       0.00,      0.40,     0.38]]

y = ['Shortbread',
     'Shortbread',
     'Shortbread',
     'Shortbread',
     'Sugar',
     'Sugar',
     'Sugar',
     'Sugar',
     'Fortune',
     'Fortune',
     'Fortune',
     'Fortune',
     'Fortune']


knn = KNearestNeighborsClassifier(k=5)
knn.fit(x, y)
observation = [0.10, 0.15, 0.30, 0.45]
assert knn.classify(observation) == 'Shortbread'
assert knn.compute_distances(observation) == [0.04690415759823429, 0.037416573867739396, 0.061644140029689765, 0.1224744871391589, 0.15811388300841897, 0.158113883008419,
                                              0.08831760866327845, 0.24494897427831783, 0.21213203435596428, 0.18708286933869708, 0.3959797974644666, 0.17320508075688776, 0.22759613353482086]

knn2 = KNearestNeighborsClassifier(k=6)
knn2.fit(x, y)
observation = [0.20, 0.10, 0.40, 0.28]
assert knn2.classify(observation) == 'Fortune'
assert knn2.compute_distances(observation) == [0.21260291625469296, 0.23748684174075832, 0.20049937655763422, 0.2634387974463898, 0.2973213749463701, 0.25377155080899044,
                                  0.22135943621178653, 0.43520110293977887, 0.1562049935181331, 0.1319090595827292, 0.1881488772222678, 0.1240967364599086, 0.142828568570857]
