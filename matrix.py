import math

def make_bezier():
    b = new_matrix()
    ident(b)
    b[0][0] = -1
    b[1][0] = 3
    b[2][0] = -3
    b[3][0] = 1

    b[0][1] = 3
    b[1][1] = -6
    b[2][1] = 3
    b[3][1] = 0

    b[0][2] = -3
    b[1][2] = 3
    b[2][2] = 0
    b[3][2] = 0

    b[0][3] = 1
    b[3][3] = 0
    return b

def make_hermite():
    h = new_matrix()
    ident(h)
    h[0][0] = 2
    h[1][0] = -2
    h[2][0] = 1
    h[3][0] = 1

    h[0][1] = -3
    h[1][1] = 3
    h[2][1] = -2
    h[3][1] = -1

    h[0][2] = 0
    h[1][2] = 0
    h[2][2] = 1
    h[3][2] = 0

    h[0][3] = 1
    h[3][3] = 0
    return h

def generate_curve_coefs( p1, p2, p3, p4, t ):
    coefs = new_matrix(4, 1)

    if t == 'bezier':
        inverse = make_bezier()
        coefs[0][0] = p1
        coefs[0][1] = p2
        coefs[0][2] = p3
        coefs[0][3] = p4
    else:
        inverse = make_hermite()
        coefs[0][0] = p1
        coefs[0][1] = p3
        coefs[0][2] = p2 - p1
        coefs[0][3] = p4 - p3

    matrix_mult( inverse, coefs )
    return coefs

    

def make_translate( x, y, z ):
    t = new_matrix()
    ident(t)
    t[3][0] = x
    t[3][1] = y
    t[3][2] = z
    return t

def make_scale( x, y, z ):
    s = new_matrix()
    ident(s)
    s[0][0] = x
    s[1][1] = y
    s[2][2] = z
    return s
    
def make_rotX( theta ):    
    rx = new_matrix()
    ident( rx )
    rx[1][1] = math.cos( theta )
    rx[2][1] = -1 * math.sin( theta )
    rx[1][2] = math.sin( theta )
    rx[2][2] = math.cos( theta )
    return rx

def make_rotY( theta ):
    ry = new_matrix()
    ident( ry )
    ry[0][0] = math.cos( theta )
    ry[2][0] = -1 * math.sin( theta )
    ry[0][2] = math.sin( theta )
    ry[2][2] = math.cos( theta )
    return ry

def make_rotZ( theta ):
    rz = new_matrix()
    ident( rz )
    rz[0][0] = math.cos( theta )
    rz[1][0] = -1 * math.sin( theta )
    rz[0][1] = math.sin( theta )
    rz[1][1] = math.cos( theta )
    return rz

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len( matrix ) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

def scalar_mult( matrix, x ):
    for r in range( len( matrix[0] ) ):
        for c in range( len( matrix ) ):
            matrix[c][r] *= x

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    
    t = new_matrix( 4, 1 )

    for c in range( len( m2 ) ):        
        
        for r in range(4):
            t[0][r] = m2[c][r]
            
        for r in range(4):
            m2[c][r] = m1[0][r] * t[0][0] + m1[1][r] * t[0][1] + m1[2][r] * t[0][2] + m1[3][r] * t[0][3]


