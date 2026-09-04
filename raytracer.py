# ASSIGNMENT 2
from matplotlib import pyplot as plt
from math import tan , cos , sin , pi , atan2 , exp

# TASK 1
def draw_directed_segment(dirseg, col):
    pt1 = dirseg [0]
    pt2 = dirseg [1]
    dx = pt2 [0] - pt1 [0]
    dy = pt2 [1] - pt1 [1]
    # This next line is needed to make sure that the axes of the plot
    # include the full range of the directed segment
    plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], '-', color=col)
    plt.quiver(
        pt1[0], pt1[1], dx, dy,
        scale_units='xy', angles='xy', scale=1,
        width=.005,
        color=col
    )
def draw_point(pt , col):
    plt.plot(pt[0] , pt[1] , 'x' , color=col)

def draw_segment(seg , col):
    pt1 = seg[0]
    pt2 = seg[1]
    plt.plot([pt1[0] , pt2[0]] , [pt1[1] , pt2[1]] , color=col)

def draw_path(path , col):
    for i in range(len(path) - 1):
        draw_directed_segment([path[i] , path[i + 1]] , col)

def draw_window(win , col):
    xlst = win[0]
    ylst = win[1]
    y1 = [win[1][0] for i in xlst]
    y2 = [win[1][1] for i in xlst]
    x1 = [win[0][0] for i in ylst]
    x2 = [win[0][1] for i in ylst]
    plt.plot(xlst , y1 , color=col)
    plt.plot(xlst , y2 , color=col)
    plt.plot(x1 , ylst , color=col)
    plt.plot(x2 , ylst , color=col)




# draw_point([0, 1], 'red')
# draw_point([1, 0], 'blue')
# draw_point([1.5, 1], 'pink')
# draw_directed_segment([[0,1], [1,0]], 'green')
# draw_directed_segment([[-1.5,-1.5], [-1.4,-1.5]], 'cyan')
# draw_directed_segment([[1.5,-1.5], [1.47,-1.45]], 'green')
# draw_directed_segment([[1,1], [0,1]], [0, 1, 0])
# draw_path([[-1.75, 0.0], [-1.25, 0.0], [-1.5, 0.5], [-1.0, 1.6]], 'grey')
# draw_segment([[-1,-0.5], [1.5, 0.3]], [1, 1, 0])
# draw_segment([[-1, 1], [1, -1]], [0.5, 0.5, 0.5])
# draw_window([[-2, 2], [-1.8, 1.6]], [1,0,0])
# plt.show()


# TASK 2

def lines_intersect(line1 , line2):
    if abs(line1[0] * line2[1] - line1[1] * line2[0]) < 1e-10:
        return None
    xval = (line1[2]*line2[1] - line2[2]*line1[1]) / (line2[0]*line1[1] - line1[0]*line2[1])
    yval = (line1[2]*line2[0] - line2[2]*line1[0]) / (line1[0]*line2[1] - line2[0]*line1[1])
    return [xval , yval]

# print(lines_intersect ([1, 1, -3], [1, -1, 1]))
# print(lines_intersect ([1, 1, 0], [2, 2, 3]))

# TASK 3a

def line_from_segment(seg):
    ycof = seg[1][0] - seg[0][0]
    xcof = seg[0][1] - seg[1][1]
    cons = seg[0][0]*seg[1][1] - seg[0][1]*seg[1][0]
    return [xcof , ycof , cons]

# print(line_from_segment([[0,0], [1,1]]))

# TASK 3b

def point_on_segment(point , seg):
    x , y = point
    x1 , y1 = seg[0]
    x2 , y2 = seg[1]
    DP = (x - x2)*(x - x1) + (y - y2)*(y - y1)
    return DP <= 0

# print(point_on_segment([0, -1], [[1,1], [3, 5]]))
# print(point_on_segment([2, 3], [[1,1], [3, 5]]))

# TASK 3c

def segments_intersect(seg1 , seg2):
    line1 = line_from_segment(seg1)
    line2 = line_from_segment(seg2)
    pt = lines_intersect(line1 , line2)
    if pt is None:
        return None
    if point_on_segment(pt , seg1) and point_on_segment(pt , seg2):
        return pt
    return None

# TASK 4

def line_from_ray(ray):
    m = tan(ray[1])
    x = ray[0][0]
    y = ray[0][1]
    if abs(cos(ray[1])) < 1e-10:
        return [1 , 0 , -x]
    return [-m , 1 , x*m - y]

def point_on_ray(point , ray):
    xpt = point[0]
    ypt = point[1]
    xr = ray[0][0]
    yr = ray[0][1]
    tht = ray[1]
    return (xpt - xr)*cos(tht) + (ypt - yr)*sin(tht) >= -1e-10

def ray_segment_intersect(ray , seg):
    lineray = line_from_ray(ray)
    lineseg = line_from_segment(seg)
    pt = lines_intersect(lineray , lineseg)
    if pt is None:
        return None
    if point_on_segment(pt , seg) and point_on_ray(pt , ray):
        return pt
    return None

# TASK 5

def intersection_line_segment(line , seg):
    lineseg = line_from_segment(seg)
    pt = lines_intersect(line , lineseg)
    if pt is None:
        return None
    if point_on_segment(pt , seg):
        return pt
    return None

def draw_line_in_window(line , window , col):
    x1 , x2 = window[0]
    y1 , y2 = window[1]
    winsegs = [[[x1 , y1] , [x1 , y2]] , [[x2 , y1] , [x2 , y2]] , [[x1 , y1] , [x2 , y1]] , [[x1 , y2] , [x2 , y2]]]
    pts = [intersection_line_segment(line , i) for i in winsegs]
    pts = [i for i in pts if i is not None]
    if len(pts) >= 2:
        return draw_segment([pts[0] , pts[1]] , col)

# TASK 6

def draw_lines_and_window(line1 , line2 , window):
    draw_window(window , [1,0,0])
    draw_line_in_window(line1 , window , [0.5,0.5,1])
    draw_line_in_window(line2 , window , [0,1,0])
    pt = lines_intersect(line1 , line2)
    if min(window[0][0], window[0][1]) <= pt[0] <= max(window[0][0], window[0][1]) and min(window[1][0], window[1][1]) <= pt[1] <= max(window[1][0], window[1][1]):
        draw_point(pt , [0.25,0.25,0.25])


# TASK 7

def draw_ray_in_window(ray , window , col):
    x = ray[0][0]
    y = ray[0][1]
    x1 , x2 = window[0]
    y1 , y2 = window[1]
    winsegs = [[[x1 , y1] , [x1 , y2]] , [[x2 , y1] , [x2 , y2]] , [[x1 , y1] , [x2 , y1]] , [[x1 , y2] , [x2 , y2]]]
    pts = [ray_segment_intersect(ray , i) for i in winsegs]
    pts = [i for i in pts if i is not None]
    if len(pts) == 1:
        return draw_directed_segment([ray[0] , pts[0]] , col)
    if len(pts) >= 2:
        x1pt , y1pt = pts[0]
        x2pt , y2pt = pts[1]
        dirseg = []
        if (x1pt - x)**2 + (y1pt - y)**2 < (x2pt - x)**2 + (y2pt - y)**2:
            dirseg.append(pts[0])
            dirseg.append(pts[1])
        else:
            dirseg.append(pts[1])
            dirseg.append(pts[0])
        return draw_directed_segment(dirseg , col)

# win = [[-1,1], [0, 1]]
# line1 = [ 1, 1, -1.5]
# line2 = [ 0.1, 1, -0.7 ]
# ray = [[-0.5, 0.3], pi/4]
# ray2 = [[-1.8, 2.1], -pi/4]
# draw_line_in_window(line1, win, 'red')
# draw_line_in_window(line2, win, 'grey')
# draw_ray_in_window(ray, win, 'blue')
# draw_ray_in_window(ray2, win, 'pink')
# plt.show()

# TASK 8

def reflected_ray(ray , seg):
    if seg is None:
        return None
    ptrs = ray_segment_intersect(ray , seg)
    if ptrs is None:
        return None
    theta = ray[1]
    segdx = seg[1][0] - seg[0][0]
    segdy = seg[1][1] - seg[0][1]
    segv = [segdx , segdy]
    segnv = [segdy , -segdx]
#     scal = ((segdy)**2 + (segdx)**2)**(-0.5)
#     usegv = [scal*i for i in segv]
#     usegnv = [scal*i for i in segnv]
#     dp1 = scal*((cos(theta) * segdx) + (sin(theta) * segdy))
#     dp2 = scal*((cos(theta) * segdy) - (sin(theta) * segdx))
#     c1 = [dp1 * i for i in usegv]
#     c2 = [dp2 * j for j in usegnv]
    dp1 = (cos(theta) * segdx) + (sin(theta) * segdy)
    dp2 = (cos(theta) * segdy) - (sin(theta) * segdx)
    c1 = [dp1 * i for i in segv]
    c2 = [dp2 * j for j in segnv]
    outv = [c1[0] - c2[0] , c1[1] - c2[1]]
    phi = atan2(outv[1] , outv[0])
    rayx = [ptrs , phi]
    return rayx

def one_bounce(ray , seg , win):
    ptrs = ray_segment_intersect(ray , seg)
    x1 , x2 = win[0]
    y1 , y2 = win[1]
    winsegs = [[[x1 , y1] , [x1 , y2]] , [[x2 , y1] , [x2 , y2]] , [[x1 , y1] , [x2 , y1]] , [[x1 , y2] , [x2 , y2]]]
    pts = [ray_segment_intersect(ray , i) for i in winsegs]
    pts = [i for i in pts if i is not None]
    if ptrs is None:
        return [ray[0] , pts[0]]
    else:
        rayx = reflected_ray(ray , seg)
        ptsx = [ray_segment_intersect(rayx , i) for i in winsegs]
        ptsx = [i for i in ptsx if i is not None]
        return [ray[0] , ptrs , ptsx[0]]

# seg = [[0,3], [3,0]]
# win = [[-1,4], [-1, 4]]
# print(one_bounce([[1,1], pi/6], seg, win))
# print(one_bounce([[0.75, 2], pi+0.1], seg, win))

# TASK 9

def draw_one_bounce(path , seg , win):
    draw_window(win , [1,0,0])
    draw_segment(seg , [0,1,0])
    for i in range(len(path) - 1):
        draw_directed_segment([path[i] , path[i + 1]] , [0,0,1])

# window = [[0 , 1] , [0 , 1]]
# obstacle = [[0.25 , 0.75] , [0.75 , 0.25]]
# path = one_bounce([[0.1 , 0.1] , pi/4] , obstacle , window)
# draw_one_bounce(path , obstacle , window)
# plt.show()

# TASK 10

def multi_bounce(ray , seglist , win , maxpathlen):
    path = [ray[0]]
    curray = ray
    x1 , x2 = win[0]
    y1 , y2 = win[1]
    winsegs = [[[x1 , y1] , [x1 , y2]] , [[x2 , y1] , [x2 , y2]] , [[x1 , y1] , [x2 , y1]] , [[x1 , y2] , [x2 , y2]]]
    for i in range(maxpathlen):
        ptnearest = None
        segnearest = None
        mindist = None
        x , y = curray[0]
        for sego in seglist:
            pt = ray_segment_intersect(curray , sego)
            if pt is not None:
                dx = pt[0] - curray[0][0]
                dy = pt[1] - curray[0][1]
                d2 = dx**2 + dy**2
                if d2 > 1e-10:
                    if (mindist is None) or (d2 < mindist):
                        mindist = d2
                        ptnearest = pt
                        segnearest = sego
        if ptnearest is None:
            ptrw = [(ray_segment_intersect(curray , i) , i) for i in winsegs]
            ptrw = [i for i in ptrw if i[0] is not None]
            ptnearest = ptrw[0][0]
        path.append(ptnearest)
        curray = reflected_ray(curray , segnearest)
        if curray is None:
            return path
    return path

# TASK 11

def draw_multi_bounce(path , seglist , win):
    draw_window(win , [1,0,0])
    for i in seglist:
        draw_segment(i , [0,1,0])
    for i in range(len(path) - 1):
        draw_directed_segment([path[i] , path[i + 1]] , [0,0,1])

# TASK 12

def draw_n_multi_bounce(pathlist , seglist , win):
    draw_window(win , [1,0,0])
    for i in seglist:
        draw_segment(i , [0,1,0])
    for path in pathlist:
        for j in range(len(path) - 1):
            draw_directed_segment([path[j] , path[j + 1]] , [1/(pathlist.index(path)+1),1 - 1/(pathlist.index(path)+1),0.5])
# written as so to differ colours between the n particles as much as possible

# TASK 13

def multi_bounce_wrap(ray , seglist , window , pathlen):
    newray = ray
    path = multi_bounce(ray , seglist , window , pathlen)
    pathtotal = [path[0]]
    if len(path) <= pathlen:
        while len(pathtotal) <= pathlen:
            pathnew = multi_bounce(newray , seglist , window , pathlen)
            if len(pathtotal) + len(pathnew) -1 > pathlen:
                i = 1
                while len(pathtotal) <= pathlen:
                    pathtotal.append(pathnew[i])
                    i = i + 1
                return pathtotal
            if len(pathtotal) + len(pathnew) -1 <= pathlen:
                pathtotal.extend(pathnew[1:])
            lastpt = pathtotal[-1]
            lasttheta = atan2((pathtotal[-1][1] - pathtotal[-2][1]) , (pathtotal[-1][0] - pathtotal[-2][0]))
            x1 , x2 = window[0]
            y1 , y2 = window[1]
            if abs(lastpt[0] - x1) < 1e-10:
                newpt = [x2 , lastpt[1]]
            if abs(lastpt[0] - x2) < 1e-10:
                newpt = [x1 , lastpt[1]]
            if abs(lastpt[1] - y1) < 1e-10:
                newpt = [lastpt[0] , y2]
            if abs(lastpt[1] - y2) < 1e-10:
                newpt = [lastpt[0] , y1]
            pathtotal.append(newpt)
            newray = [newpt , lasttheta]
        return pathtotal
    return path


window = [[0, 10], [0, 10]]
segs = [[[7,1],[9.5,2]],[[4,6],[2,9]],[[4,5],[2,1]],[[0.5,5],[1,8]],[[8,4],[5,7]]]
rayz = [[7,4],pi/3]
rayzs = [[[1,1],pi/4],[[9,8],-pi/2],[[4,8],-4*pi/5]]
path = multi_bounce_wrap(rayz , segs , window , 16)
pathlst = [multi_bounce_wrap(i , segs , window , 11) for i in rayzs]
draw_multi_bounce(path , segs , window)
draw_n_multi_bounce(pathlst , segs , window)
plt.show()
