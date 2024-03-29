from matplotlib import pyplot as plt

def plot_points(points, label="", color="orange"):
    x = []
    y = []
    for point in points:
        x.append(point.x)
        y.append(point.y)
    plt.scatter(x, y, label=label, color=color)

def plot_line(points, label="", color="blue"):
    x = []
    y = []
    for point in points:
        x.append(point.x)
        y.append(point.y)
    plt.plot(x, y, label=label, color=color)

def set_range(min, max):
    plt.xticks(range(min,max,1))
    plt.yticks(range(min,max,1))

def set_title(title):
    plt.title(title)

def set_labels(x="x", y="y"):
    plt.xlabel(x)
    plt.ylabel(y)

def show_graph():
    plt.legend()
    plt.show()