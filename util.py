import math 
from dataclasses import dataclass

@dataclass
class Vertex:
    position: list[float]
    uv: list[float]

def polarToCart(r, t, f):
    x = r*math.cos(t)*math.sin(f)
    y = r*math.sin(t)*math.sin(f)
    z = r*math.cos(f)
    return [x, y, z]

def cartToPolar(x, y, z):
    if x == 0:
        x += .0001
    if y == 0:
        y += .0001
    if z == 0:
        z += .0001
    
    r = math.sqrt(x**2 + y**2 + z**2)
    t = math.atan(math.sqrt(x**2 + y**2) / z)
    f = math.atan(y/x) if x >= 0 else math.atan(y/x) + math.pi

    return [r, t, f]

def defineSphere(radius, resolution) -> list[Vertex]:
    fi_min = 0
    fi_max = math.pi
    dfi = math.pi / (resolution * 2)
    dt = math.pi / resolution

    t = 0
    t_max = 2*math.pi

    vertices: list[Vertex] = []

    while t <= t_max:
        fi = fi_min
        while fi <= fi_max:
            x, y, z = polarToCart(radius, t, fi)
            vertex = [x, y, z]
            
            # PRIMEIRO TRIANGULO ------------------------------
            
            uv = [t/t_max, fi/fi_max]
            position = vertex
            vertices.append(Vertex(position, uv))

            uv = [t/t_max, (fi+dfi)/fi_max]
            position = polarToCart(radius, t, fi+dfi)
            vertices.append(Vertex(position, uv))

            uv = [(t+dt)/t_max, (fi+dfi)/fi_max]
            position = polarToCart(radius, t+dt, fi+dfi)
            vertices.append(Vertex(position, uv))

            # SEGUNDO TRIANGULO --------------------------------

            uv = [t/t_max, fi/fi_max]
            position = vertex
            vertices.append(Vertex(position, uv))

            uv = [(t+dt)/t_max, fi/fi_max]
            position = polarToCart(radius, t+dt, fi)
            vertices.append(Vertex(position, uv))

            uv = [(t+dt)/t_max, (fi+dfi)/fi_max]
            position = polarToCart(radius, t+dt, fi+dfi)
            vertices.append(Vertex(position, uv))

            # -------------------------------------------------

            fi += dfi
        t += dt
    
    return vertices