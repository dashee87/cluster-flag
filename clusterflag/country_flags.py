""" countryflags: Reproduce country flags with numpy and pandas
"""

import numpy as np
import pandas as pd
    
def simple_flag(npoints=[100,100,100], colours=['green','white','orange'], 
               ratio=1.5, sep=0.0, horizontal=False):
    
    """Construct a simple flag (e.g. Ireland). 
    
    These are flags that depict equal partitions either horizontally or 
    vertically, where the number of partitions (i.e. stripes) is specified 
    by the user. The function also includes an argument to incorporate a 
    boundary between the partitions, a feature designed for 
    segmentation/clustering purposes.
    
    Parameters
    ----------
    npoints : int list, default [100, 100, 100]
         The number of points uniformly distributed across each partition.
         The length of the array determines the number of partitions.
         Input 0 if you want no points within a partition.
         For example, npoints = [100, 100, 0, 100] creates 4 partitions
         with no points included within the third partition
    
    colours : string list, default ['green','white','orange'] (Irish flag)
         Determines the colour of the generated points, where the i-th value
         determines the colour of the points within the i-th partition
    
    ratio : float, default  1.5
        Determines the length of the flag relative to the width.
        For example, the Swiss flag has a ratio of 1 (i.e. square) and
        the Irish flag has a ratio of 1.5.
    
    sep : float, default  0
        Should be between [0, 1]
        Constructs a boundary between the partitions.
        The value represents the prortion of the flag's area 
        that each boundary encloses
    
    horizontal : boolean, default False
        Horizontal (e.g. Germany) or vertical (e.g. Ireland) partitons/stripes.
        The default is False, meaning vertical stripes are generated.
        
    Returns
    -------
    output : pandas data frame (shape = (sum(npoints), 3))
        x: cartesian coordinates along x-axis
        y: cartesian coordinates along y-axis
        flag_col: colour of point
    """
    
    parts = len(npoints)
    if parts != len(colours):
        raise ValueError("npoints and colours parameters must be same length")
    shrink = (1 - (parts - 1)*sep)/parts
    if horizontal:
        output = [(np.random.uniform(0, shrink, size=(npoints[i], 1)) +
                   (i*(shrink + sep)))
        for i in range(parts) if npoints[i] > 0]
        output = np.concatenate((np.random.random((sum(npoints), 1)) * ratio,
                                 np.concatenate(output)), axis=1)  
    else:
        output=[ratio * (np.random.uniform(0, shrink, size=(npoints[i], 1)) + 
                         (i*(shrink + sep)))
        for i in range(parts) if npoints[i] > 0]
        output = np.concatenate((np.concatenate(output),
                                 np.random.random((sum(npoints), 1))), axis=1)
    output = pd.DataFrame(output, columns = ['x', 'y'])
    output['flag_col'] = [colours[n]  for (n, ttt) in enumerate(npoints)
    for i in range(ttt)]
    return(output)
    
def ellipse_points(npoints, cx, cy, rx, ry, 
                   xlen=None, ylen=None, inside=True):
    
    """Generate points from inside/outside ellipse.
    
    This function Randomly distribute points inside or outside of an ellipse, 
    where the centre position and axes lengths are specified by the user. 
    For points outside of the circle, the user must additionally specify the
    dimensions of the enclosing rectangle.
    
    Parameters
    ----------
    npoints : int, no default, required
         Determines the number of points to be randomly distributed 
         within or outside the circle.
    
    cx : float, no default, required
        The x-coordinate of the ellipse centre
    
    cy : float, no default, required
        The y-coordinate of the ellipse centre
    
    rx : float, no default, required
        Radius of ellipse along x-axis
    
    ry : float, no default, required
        Radius of ellipse along y-axis
        
    xlen : float, no default, required if inside = False
        Width of enclosing rectangle along x-axis 
    
    ylen : float, no default, required if inside = False
        Length of enclosing rectangle along y-axis 
    
    inside : boolean, default True
        Return points inside or outside of circle. The default value is True,
        meaning that random points within the circle are returned.
        
    Returns
    -------
    output : numpy array (shape = (npoints, 2))
    """
    
    if(inside):
        deg = np.random.uniform(0, 2*np.pi, (npoints, 1))
        r0 = np.random.uniform(0, rx, (npoints, 1))
        r1 = np.random.uniform(0,ry, (npoints, 1))
        return(np.concatenate((r0*np.sin(deg) + cx,
                               r1*np.cos(deg) + cy), axis=1))
    else:
        output = np.empty((0, 2))
        while len(output)<npoints:
            xpos = np.random.uniform(0, xlen)
            ypos = np.random.uniform(0, ylen)
            if (xpos-cx)**2/(rx**2) + (ypos-cy)**2/(ry**2) > 1:
                output = np.append(output, np.array([[xpos, ypos]]), axis=0)
    return(output)
 

def japan_flag(npoints=[100,100], cenx=0.5, ceny=0.5, rx=0.3, ry=0.3, sep=0.0, 
              colours=['red','white'], ratio=1.5):
    
    """Flag with a circle
    
    Construct a flag composed of a circle (actually an ellipse) 
    within a rectangle (e.g. Japan). The user specifies the location of the 
    ellipse centre, radius along each axis, flag ratio and even a boundary
    between the ellipse and the rest of the rectangle.
    
    Parameters
    ----------
    npoints : int list (length = 2), default [100, 100]
         The number of points uniformly distributed across each partition.
         The length of the array must be 2.
         The first and second values in the array represent the elliptical 
         part amd background, respectively.
         Input 0 if you want no points within a partition.
    
    cx : float, default 0.5
        The x-coordinate of the ellipse centre
    
    cy : float, default 0.5
        The y-coordinate of the ellipse centre
    
    rx : float, default 0.3
        Radius of ellipse along x-axis (greater than 0 and less than 0.5)
    
    ry : float,  default 0.5
        Radius of ellipse along y-axis (greater than 0 and less than 0.5)
        
    sep : float, default  0
        Should be drawn from [0, 0.5]
        Constructs a boundary around the ellipse.
        You can think that the flag is enclosed within another ellipse of
        radii rx+sep and ry+sep.
            
    ratio : float, default  1.5
        Determines the length of the flag relative to the width.
        For example, the Swiss flag has a ratio of 1 (i.e. square) and
        the Irish flag has a ratio of 1.5.
        
    Returns
    -------
    output : pandas data frame (shape = (sum(npoints), 3))
        x: cartesian coordinates along x-axis
        y: cartesian coordinates along y-axis
        flag_col: colour of point
    """
    if rx >= 0.5 or rx <= 0 or ry >= 0.5 or ry <= 0:
        raise ValueError("Radii must be greater than 0 and less than 0.5")
    if sep<0 or sep >= 0.5:
        raise ValueError("sep must be not be negative or greater than 0.5")
    if len(npoints) != len(colours):
        raise ValueError("npoints and colours parameters must be same length")    
    fground = ellipse_points(npoints[0], cenx*ratio, ceny, 
                              rx, ry, ratio, 1, inside=True)    
    bground = ellipse_points(npoints[1],cenx*ratio, ceny, 
                              rx+sep, ry+sep, ratio, 1, inside=False)
    output = np.concatenate((fground, bground))
    output = pd.DataFrame(output, columns=['x', 'y'])
    output['flag_col']= [colours[n]  for (n, ttt) in enumerate(npoints) 
    for i in range(ttt)]
    return(output)

def laos_flag(npoints=[100,100,100], cenx=0.5, ceny=0.5, rx=0.2, ry=0.2, 
             rect=0.25, colours=['red', 'white', 'blue'], ratio=1.5, 
             horizontal=True):
    
    """Flag with a circle between two borders
    
    Construct a flag composed of a circle (actually an ellipse) within a 
    rectangle that is enclosed by two further rectangles (see flag of Laos).
    The user specifies the location of the ellipse centre, radius along each
    axis and the dimensions of the various rectangles.
    
    Parameters
    ----------
    npoints : int list (length = 3), default [100, 100, 100]
         The number of points uniformly distributed across each partition.
         The length of the array must be 3.
         The first value in the array determines the number of points in each
         border rectangle.
         The second and third values in the array represent the elliptical
         part and the background, respectively.
         Input 0 if you want no points within a partition.
    
    cx : float, default 0.5
        The x-coordinate of the ellipse centre
    
    cy : float, default 0.5
        The y-coordinate of the ellipse centre
    
    rx : float, default 0.2
        Radius of ellipse along x-axis (greater than 0 and less than 0.5)
    
    ry : float,  default 0.2
        Radius of ellipse along y-axis (greater than 0 and less than 0.5)
        
    rect : float,  default 0.2
        Should be between (0, 1)
        Determines the size of the border rectangles.
        The value represents the prortion of the flag's area 
        that each rectangle encloses             
    
    ratio : float, default  1.5
        Determines the length of the flag relative to the width.
        For example, the Swiss flag has a ratio of 1 (i.e. square) and
        the Irish flag has a ratio of 1.5.
        
    horizontal : boolean, default True
        Horizontal (e.g. Laos) or vertical (no examples) border stripes.
        The default is True, meaning horizontal border stripes are generated.    
        
    Returns
    -------
    output : pandas data frame (shape = (sum(npoints), 3))
        x: cartesian coordinates along x-axis
        y: cartesian coordinates along y-axis
        flag_col: colour of point
    """
    if rect <=0 or rect>=0.5:
        raise ValueError("rect should be drawn from (0, 0.5)")
    if len(npoints) != len(colours):
        raise ValueError("npoints and colours parameters must be same length")
    if not horizontal:
        top_rect = np.concatenate((np.random.uniform((1 - rect)*ratio, ratio,
                                                     size=(npoints[0], 1)),
                                   np.random.uniform(0, 1,
                                                     size=(npoints[0], 1))),
                                  axis=1)
        bottom_rect = np.concatenate((np.random.uniform(0, ratio*rect,
                                                        size=(npoints[0], 1)),
                                      np.random.uniform(0, 1, 
                                                        size=(npoints[0], 1))),
                                    axis=1)
        middle_part =  japan_flag(npoints[1:3],cenx=cenx, ceny=ceny, 
                                  rx=rx/(1 - 2*rect), ry=ry, sep=0,
                                 colours=colours[1:3], ratio=1.5)
        middle_part['x'] = rect*ratio + middle_part['x']*(1 - 2*rect)
    else:
        top_rect = np.concatenate((np.random.uniform(0, ratio,
                                                     size=(npoints[0], 1)),
                                   np.random.uniform(1-rect, 1,
                                                     size=(npoints[0], 1))),
                                  axis=1)
        bottom_rect = np.concatenate((np.random.uniform(0, ratio,
                                                        size=(npoints[0], 1)),
                                      np.random.uniform(0, rect,
                                                        size=(npoints[0], 1))),
                                  axis=1)
        middle_part = japan_flag(npoints[1:3], rx=rx/(1 - 2*rect), 
                                 ry=ry/(1 - 2*rect), colours=colours[1:3], 
                                 ratio=ratio/(1 - 2*rect))
        middle_part['x'] = middle_part['x']*(1 - 2*rect)
        middle_part['y'] = rect + middle_part['y']*(1 - 2*rect)
    rects=pd.DataFrame(np.concatenate((top_rect, bottom_rect)),
                       columns=['x', 'y'])
    rects['flag_col'] = colours[0]
    return(pd.concat([rects, middle_part]))
    
def cross_flag(npoints=[100, 100, 100, 100, 100], cenx=0.5, ceny=0.5,
               rectx=0.2, recty=0.2, 
               colours=['red', 'blue', 'white', 'green', 'orange'], ratio=1.5):
    
    """Generate flag with a cross
    
    Construct a flag composed of a cross that seperates four rectangles
    (e.g. Scandinavian countries). The user specifies the location of the 
    cross centre as well as its width.
    
    Parameters
    ----------
    npoints : int list (length = 5), default [100, 100, 100, 100, 100]
         The number of points uniformly distributed across each partition.
         The length of the array must be 5.
         The first four values in the array determine the number of points in 
         each rectangle
         The order is: top left, bottom left, top right, bottom right
         The fifth value in the array represents the cross part of the flag.
         Input 0 if you want no points within a partition.
    
    cx : float, default 0.5
        The x-coordinate of the cross centre
    
    cy : float, default 0.5
        The y-coordinate of the cross centre
    
    rectx : float, default 0.2
        Width of cross along x-axis (irrespective of ratio value)
    
    recty : float,  default 0.5
        Width of cross along y-axis
    
    ratio : float, default  1.5
        Determines the length of the flag relative to the width.
        For example, the Swiss flag has a ratio of 1 (i.e. square) and
        the Irish flag has a ratio of 1.5.
        
    Returns
    -------
    output : pandas data frame (shape = (sum(npoints), 3))
        x: cartesian coordinates along x-axis
        y: cartesian coordinates along y-axis
        flag_col: colour of point
    """
    if len(npoints) != len(colours):
        raise ValueError("npoints and colours parameters must be same length")
    shift_rectx = rectx/ratio
    small_rects_x = [np.random.uniform(shift, rect_size + shift, (p)) 
                     for (p,rect_size, shift) in 
                      zip(npoints[:4],
                          [cenx - shift_rectx/2,cenx - shift_rectx/2,
                           1 - (cenx + shift_rectx/2),
                           1 - (cenx + shift_rectx/2)],
                          [0, 0, cenx + shift_rectx/2, 
                           cenx + shift_rectx/2])]
    small_rects_y = [np.random.uniform(shift, rect_size + shift, (p)) 
                     for (p,rect_size, shift) in 
                      zip(npoints[:4],
                          [1 - (ceny + recty/2),ceny - recty/2,
                             1 - (ceny + recty/2),ceny - recty/2],
                          [ceny + recty/2, 0, ceny + recty/2, 0])]                          
    output = np.vstack((np.concatenate(small_rects_x)*ratio,
                                     np.concatenate(small_rects_y)))
    output = pd.DataFrame(np.transpose(output), columns=['x', 'y']) 
    output['flag_col'] = [colours[n]  
           for (n, ttt) in enumerate(npoints[:4]) for i in range(ttt)]
    if(npoints[4] < 1):
        return(output)
    horizes = np.random.uniform(0, 1, npoints[4]) > 0.5
    striped_part = np.random.uniform(0, 1, (npoints[4], 2))
    striped_part[horizes] = striped_part[horizes]*[[ratio,recty]] + \
                            [[0, ceny - recty/2]]
    striped_part[np.invert(horizes)] = striped_part[np.invert(horizes)] * \
                                       [[rectx, 1]] + \
                                       [[(cenx*ratio) - rectx/2, 0]]
    striped_part = pd.DataFrame(striped_part,columns=['x', 'y'])
    striped_part['flag_col'] = colours[4]
    return(pd.concat([output, striped_part]))

def crescent_points(bcx, bcy, scx, scy, bradius, sradius, 
                   starcx=0.6, starcy=0.6, starrx=0.1, starry=0.1,
                   rect=0, xlen=None, ylen=None, 
                   inside=True, bigCirc=True, 
                   star=False, horizontal=True):
    
    """Randomly distribute points inside or outside of a crescent (partially
    overlapping circles), where the centre positions and axes lengths are 
    specified by the user. 
    For points outside of the crescent, the user must additionally specify the
    dimensions of the enclosing rectangle.
    
    Parameters
    ----------
    npoints : int, no default, required
         Determines the number of points to be randomly distributed 
         within or outside the circle.
    
    bcx : float, no default, required
        The x-coordinate of the big (or outer) circle
    
    bcy : float, no default, required
        The y-coordinate of the big (or outer) circle
        
    scx : float, no default, required
        The x-coordinate of the small (or inner) circle
    
    scy : float, no default, required
        The y-coordinate of the small (or inner) circle        
    
    bradius : float, no default, required
        Radius of big (outer) circle (greater than 0 and less than 0.5)
    
    sradius : float, no default, required
        Radius of small (inner) circle (greater than 0 and less than 0.5)

    starcx : float, default 0.6
        Centre of star (actually a rectangle) on the x-axis        

    starcy : float, default 0.6
        Centre of star (actually a rectangle) on the y-axis

    starrx : float, default 0.6
        Length of star (actually a rectangle) along x-axis        

    starry : float, default 0.6
        Length of star (actually a rectangle) along y-axis

    rect : float,  default 0
        Should be between [0, 0.5)
        Determines the size of the border rectangles.
        The value represents the prortion of the flag's area 
        that each rectangle encloses.                      
        
    xlen : float, no default, required if inside = False or star = False
        Width of enclosing rectangle along x-axis 
    
    ylen : float, no default, required if inside = False or star = False
        Length of enclosing rectangle along y-axis 
    
    inside : boolean, default True
        Return points inside or outside of circles. The default value is True,
        meaning that random points within the circles are returned.

    bigCirc : boolean, default True
        If inside = True, then this parameter determines whether points are
        distributed within the big (inner) or small (outer) circle.
        The default value is True, meaning points are drawn from within the
        big circle.
        
    star : boolean, default False
        If set to True, this parameter supersedes the inside and bigCirc
        parameters and generates points drawn uniformly from the star region.
        
    horizontal : boolean, default False
        Horizontal (e.g. Libya) or vertical (no examples) border stripes.
        The default is True, meaning horizontal border stripes are considered.        
        
    Returns
    -------
    output : numpy array (shape = (npoints, 2))
    """
    
    if bradius >= 0.5 or bradius <= 0 or sradius >= 0.5 or sradius <= 0:
        raise ValueError("Radii must be greater than 0 and less than 0.5")
    crit = True
    if star:
        while crit:
            if horizontal:
                thepoint = np.random.uniform(low=[[0, rect]], 
                                             high=[[xlen, ylen-rect]])
            else:
                thepoint = np.random.uniform(low=[[rect, 0]], 
                                             high=[[xlen-rect, ylen]])
            if np.sum((thepoint - [bcx,bcy])**2) < bradius**2 and \
               np.sum((thepoint - [scx,scy])**2) > sradius**2:
                continue
            elif starcx-starrx < thepoint[0,0] < starcx+starrx and \
                 starcy-starry < thepoint[0,1] < starcy+starry:
                    continue
            else:
                crit=False
    elif inside and bigCirc:
        while crit:
            thepoint = np.random.uniform(low=[[bcx-bradius, bcy-bradius]],
                                         high=[[bcx+bradius, bcy+bradius]])
            if np.sum((thepoint - [bcx, bcy])**2) < bradius**2 and \
               np.sum((thepoint - [scx, scy])**2) > sradius**2:
                crit = False
    elif inside and not bigCirc:
        while crit:
            thepoint = np.random.uniform(low=[[scx-sradius, scy-sradius]],
                                         high=[[scx+sradius, scy+sradius]])
            if np.sum((thepoint - [bcx, bcy])**2) > bradius**2 and \
               np.sum((thepoint - [scx, scy])**2) < sradius**2:
                crit = False
    else:
        while crit:
            thepoint = np.random.uniform(high = [[xlen, ylen]])               
            if np.sum((thepoint - [bcx, bcy])**2) > bradius**2 and \
               np.sum((thepoint - [scx, scy])**2) > sradius**2:
                crit = False
    return(thepoint)
    
  
def crescent_flag(npoints=[100,100,100,100,100], bcx=0.5, bcy=0.5, 
                        scx=0.53, scy=0.5, bradius=0.125, sradius=0.1, 
                        starcx=0.6, starcy=0.5, starrx=0.05, 
                        starry=0.05, rect=0.2,
                        colours=['white', 'white', 'black', 'green', 'red'], 
                        ratio=1.5, horizontal=True):
    
    """Flags with a crescent
    
    Reproduce flags that include a crescent and a star (e.g. Turkey, Libya).
    I couldn't come up with a way to efficiently draw numbers from a star, so
    I substituted the star with a rectangle (most simple option). 
    My apologies to Turks, Tunisians, Maldivians, etc.
    
    Parameters
    ----------
    npoints : int list (length = 5), default [100, 100, 100, 100, 100]
         The number of points uniformly distributed across each partition.
         The length of the array must be 5.
         npoints[0]: Crescent
         npoints[1]: Star
         npoints[2]: Background between borders
         npoints[3]: Bottom/left Border
         npoints[4]: Top/right Border
         Input 0 if you want no points within a partition.
    
    bcx : float, no default, required
        The x-coordinate of the big (or outer) circle
    
    bcy : float, no default, required
        The y-coordinate of the big (or outer) circle
        
    scx : float, no default, required
        The x-coordinate of the small (or inner) circle
    
    scy : float, no default, required
        The y-coordinate of the small (or inner) circle        
    
    bradius : float, no default, required
        Radius of big (outer) circle (must be greater than 0 and less than 0.5)
    
    sradius : float, no default, required
        Radius of small (inner) circle (greater than 0 and less than 0.5)

    starcx : float, default 0.6
        Centre of star (actually a rectangle) on the x-axis        

    starcy : float, default 0.6
        Centre of star (actually a rectangle) on the y-axis

    starrx : float, default 0.6
        Length of star (actually a rectangle) along x-axis        

    starry : float, default 0.6
        Length of star (actually a rectangle) along y-axis

    rect : float,  default 0
        Should be drawn from [0, 0.5)
        Determines the size of the border rectangles.
        The value represents the prortion of the flag's area 
        that each rectangle encloses.
        If you don't wish to include borders, 
        set  rect = npoint[4] = npoints[5] = 0.
                         
    xlen : float, no default, required if inside = False or star = False
        Width of enclosing rectangle along x-axis 
    
    ylen : float, no default, required if inside = False or star = False
        Length of enclosing rectangle along y-axis 
    
    inside : boolean, default True
        Return points inside or outside of circles. The default value is True,
        meaning that random points within the circles are returned.

    bigCirc : boolean, default True
        If inside = True, then this parameter determines whether points are
        distributed within the big (inner) or small (outer) circle.
        The default value is True, meaning points are drawn from within the
        big circle.
        
    star : boolean, default False
        If set to True, this parameter supersedes the inside and bigCirc
        parameters and generates points drawn uniformly from the star region.
        
    ratio : float, default  1.5
        Determines the length of the flag relative to the width.
        For example, the Swiss flag has a ratio of 1 (i.e. square) and
        the Irish flag has a ratio of 1.5.        
        
    horizontal : boolean, default False
        Horizontal (e.g. Libya) or vertical (no examples) border stripes.
        The default is True, meaning horizontal border stripes are considered.
        
        
    Returns
    -------
    output : pandas data frame (shape = (sum(npoints), 3))
        x: cartesian coordinates along x-axis
        y: cartesian coordinates along y-axis
        flag_col: colour of point
    """
    
    if len(npoints) != len(colours):
        raise ValueError("npoints and colours parameters must be same length")
    if rect < 0 or rect >= 0.5:
        raise ValueError("rect should be from [0,0.5)")
    crescent_part = [crescent_points(bcx=bcx*ratio, bcy=bcy, scx=scx*ratio, 
                                     scy=scy,bradius=bradius, sradius=sradius,
                                     starcx=starcx*ratio, starcy=starcy,
                                     starrx=starrx, starry=starry,
                                     xlen=ratio, ylen=1, inside=True, 
                                     bigCirc=True, rect=rect, 
                                     horizontal=horizontal, star=False) 
                    for k in range(npoints[0])]
    if npoints[0]<1:
        crescent_part = np.array([crescent_part]).reshape(0, 2)
    else:                             
        crescent_part = np.vstack(crescent_part)
    
    star_part = np.random.uniform(low=[[starcx*ratio - starrx, starcy-starry]],
                                 high=[[starcx*ratio + starrx, starcy+starry]],
                                 size=(npoints[1], 2))
    bground_part = [crescent_points(bcx=bcx*ratio, bcy=bcy, scx=scx*ratio, 
                                    scy=scy, bradius=bradius, sradius=sradius,
                                    starcx=starcx*ratio, starcy=starcy, 
                                    starrx=starrx, starry=starry,
                                    xlen=ratio, ylen=1, inside=True, 
                                    bigCirc=True, rect=rect, 
                                    horizontal=horizontal, star=True) 
                    for k in range(npoints[2])]
    if npoints[2]<1:
        bground_part = np.array([bground_part]).reshape(0, 2)
    else:                             
        bground_part = np.vstack(bground_part)

    middle_part = np.concatenate((crescent_part, star_part, bground_part))
        
    if not any(npoints[3:5]):
        striped_part = np.array([]).reshape(0,2)
    else:
        if horizontal:
            striped_part=[np.random.uniform([0, (1-rect)*i],
                                             [ratio, rect + (1-rect)*i],
                                              size=(npoints[i+3], 2))
                          for i in range(2) if npoints[i+3] > 0]
        else:
            striped_part=[np.random.uniform([(1 - rect)*i*ratio, 0],
                                             [(rect+(1-rect)*i)*ratio,1],
                                              size = (npoints[i+3], 2))
                          for i in range(2) if npoints[i+3] > 0]
        striped_part = np.concatenate(striped_part, axis=0)
    output = pd.DataFrame(np.concatenate((middle_part, striped_part), axis=0),
                          columns=['x', 'y'])
    output['flag_col'] = [colours[n] for (n,ttt) in enumerate(npoints) 
                         for i in range(ttt)]
    return(output)
    
    
