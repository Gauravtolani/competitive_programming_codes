"""
HackerEarth July'18 Circuits - Rocket
"""

__author__ = 'Gaurav Tolani'

from math import sqrt
import math

# taking inputs
n, m, r, q = list(map(int, input().split()))

rds_coordinates = []
for _ in range(int(n)):
    i = tuple(map(int, input().split()))
    rds_coordinates.append(i)

line_coordinates = []
for _ in range(int(m)):
    i = tuple(map(int, input().split()))
    line_coordinates.append(i)

queries = []
for _ in range(int(q)):
    i = tuple(map(int, input().split()))
    queries.append(i)


# get intersecting point of two lines if possible
def line_intersect(m1, b1, m2, b2):
    if m1 == m2:
        return None
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y


# calculate distance
def calculate_two_points_distance(x1, y1, x2=0, y2=0):
    return sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))


def find_slope_and_intercept(lx1, ly1, lx2=0, ly2=0):
    slope = float(ly1 - ly2) / float(lx1 - lx2)
    return float(ly1 - ly2) / float(lx1 - lx2), ly2 - slope * lx2


# find intersecting points if line passes from inside of circle
def find_intersecting_point_line_circle(x, y, lx1, ly1, lx2=0, ly2=0):
    line_slope, line_intercept = find_slope_and_intercept(lx1, ly1)
    beta = ly1 - (line_slope * lx1)
    a = 1 + (line_slope ** 2)
    b = -2 * ((line_slope * beta) + x + (y * line_slope))
    c = ((y ** 2) + (x ** 2) + (2 * y * beta) - (r ** 2))
    d = (b**2) - (4*a*c)
    if d == 0:
        x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        y = ((x * line_slope) - beta)
        return x, y
    else:
        x1 = (-b + math.sqrt((b ** 2) - (4 * (a * c)))) / (2 * a)
        x2 = (-b - math.sqrt((b ** 2) - (4 * (a * c)))) / (2 * a)
        y1 = ((x1 * line_slope) - beta)
        y2 = ((x2 * line_slope) - beta)
        return x1, y1, x2, y2


# check if a line and a circle intersect
def check_line_and_circle_intersection(a, b, c, x, y, line_points_list):
    """
    distance of line and circle's center = ax + by + c/sqrt(a**2 + b**2)
    """
    try:
        line_circle_dist = (abs(a * x + b * y + c) / sqrt((a ** 2) + (b ** 2)))
    except:
        return 100000

    if line_circle_dist > r:
        return 100000
    elif line_circle_dist == r:
        int_x, int_y = find_intersecting_point_line_circle(x, y, line_points_list[0], line_points_list[1])
        return calculate_two_points_distance(int_x, int_y)
    elif line_circle_dist == 0:
        int_x1, int_y1, int_x2, int_y2 = find_intersecting_point_line_circle(x, y, line_points_list[0], line_points_list[1])
        return calculate_two_points_distance(int_x1, int_y1), \
               calculate_two_points_distance(int_x2, int_y2)
    else:
        int_x1, int_y1, int_x2, int_y2 = find_intersecting_point_line_circle(x, y, line_points_list[0], line_points_list[1])
        return calculate_two_points_distance(int_x1, int_y1), \
               calculate_two_points_distance(int_x2, int_y2)


def round_to_four_digits(number):
    # number = str(number)
    # temp = round(float(number), int(4 - len(number.split('.')[0])))
    # print(temp)
    # return ''.join(str(temp).split('.'))
    return int(round(number*1000))

# function to calculate shortest distance according to rules of problem
def query_type_1(query):
    distances = []
    input_slope, input_intercept = find_slope_and_intercept(query[1], query[2])

    for each_line in line_coordinates:
        slope, intercept = find_slope_and_intercept(each_line[0], each_line[1], each_line[2], each_line[3])
        if line_intersect(input_slope, slope, input_intercept, intercept):
            distances.append(calculate_two_points_distance(query[1], query[2]))

    for each_circle in rds_coordinates:
        distances.append(
            check_line_and_circle_intersection(input_slope, -1, input_intercept, each_circle[0], each_circle[1],
                                               [query[1], query[2]]))

    distances.append(calculate_two_points_distance(query[1], query[2]))

    updated_dist = []
    for dist in distances:
        if type(dist) == tuple:
            updated_dist.append(dist[0])
            updated_dist.append(dist[1])
        else:
            updated_dist.append(dist)

    updated_dist.sort()

    return round_to_four_digits(updated_dist[0])


for each_query in queries:
    if each_query[0] == 1:
        print(query_type_1(each_query))
    elif each_query[0] == 2:
        rds_coordinates.append((each_query[1], each_query[2]))
    elif each_query[0] == 3:
        line_coordinates.append((each_query[1], each_query[2], each_query[3], each_query[4]))
    elif each_query[0] == 4:
        try:
            rds_coordinates.remove(each_query[1])
        except:
            pass
    elif each_query[0] == 5:
        try:
            line_coordinates.remove(each_query[1])
        except:
            pass

