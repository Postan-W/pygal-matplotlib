from random_walk import RandomWalk
import matplotlib.pyplot as plt

rw = RandomWalk(50000)
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,c = list(range(rw.num_points)),cmap=plt.cm.Reds,
            edgecolors='none',s = 1)
plt.scatter(0,0,c = 'blue', edgecolors='none', s = 300)
plt.scatter(rw.x_values[-1],rw.y_values[-1],c = 'cyan',edgecolors= 'none',s = 300)
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)
plt.show()