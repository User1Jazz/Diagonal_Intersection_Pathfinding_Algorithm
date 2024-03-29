from pathfinding import point, get_intersection_point
import plotter
import numpy as np

def main():
    #uniform_test()
    #nonuniform_test()
    cones_test()
    return

def cones_test():
    frequency = 10 #20
    left_cones, right_cones = generate_track(width=3, length=10, frequency=10, amplitude=5, smooth_fac=50, offset=9)
    path_points = []
    for i in range(len(left_cones)):
        if i >= len(left_cones)-1 or i >= len(right_cones)-1:
            break
        E = get_intersection_point(left_cones[i], right_cones[i+1], left_cones[i+1], right_cones[i])
        if E != None:
            path_points.append(E)
    plotter.plot_points(left_cones, label="Cones", color="red")
    plotter.plot_points(right_cones, color="red")
    plotter.plot_points(path_points, label="path points", color="yellow")
    plotter.plot_line(path_points, label="path", color="blue")
    #plotter.set_range(0,12)
    plotter.set_labels(x="track length", y="track width")
    plotter.set_title("Diagonal Intersection Pathfinding")
    plotter.show_graph()
    return

def uniform_test():
    A = point(1,1)
    B = point(1,2)
    C = point(2,2)
    D = point(2,1)
    E = get_intersection_point(A,C,B,D)
    print(E.values())
    quad = [A, B, C, D, A]
    diagonal1 = [A,C]
    diagonal2 = [B,D]
    plotter.plot_line(quad, label="Nonuniform quadrilateral", color="blue")
    plotter.plot_line(diagonal1, label="Diagonals", color="green")
    plotter.plot_line(diagonal2, color="green")
    plotter.plot_points([E], label="Intersection", color="red")
    plotter.show_graph()
    return

def nonuniform_test():
    A = point(1,2)
    B = point(2,1)
    C = point(3,1)
    D = point(3,3)
    E = get_intersection_point(A,C,B,D)
    print(E.values())
    quad = [A, B, C, D, A]
    diagonal1 = [A,C]
    diagonal2 = [B,D]
    plotter.plot_line(quad, label="Nonuniform quadrilateral", color="blue")
    plotter.plot_line(diagonal1, label="Diagonals", color="green")
    plotter.plot_line(diagonal2, color="green")
    plotter.plot_points([E], label="Intersection", color="red")
    plotter.show_graph()
    return

def generate_track(width=1, length=10, frequency=10, amplitude=5, smooth_fac=50, offset=0):
    # Parameters for the sine waves
    x_values = np.linspace(0, length, num=smooth_fac)
    phase_shift = np.pi  # To ensure the waves are out of phase

    # Generate the sine waves
    left_side_y = amplitude * np.sin(2 * np.pi * frequency * x_values)
    right_side_y = left_side_y - width
    left_side_y = left_side_y[:-offset].copy()

    left_track = []
    right_track = []
    for i in range(len(left_side_y)):
        #left_track.append(point(left_x[i], left_y[i]))
        left_track.append(point(x_values[i], left_side_y[i]))
    for i in range(len(right_side_y)):
        right_track.append(point(x_values[i], right_side_y[i]))

    return left_track, right_track

if __name__ == "__main__":
    main()