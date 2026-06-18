import math

# Shape formulas + results
def calculate(shape, val1=0, val2=0, val3=0):
    if shape == "Cube":
        a = val1
        return {
            "formula": "V = a³ | SA = 6a²",
            "volume": a**3,
            "surface": 6 * a**2,
            "example": "Dice, Rubik’s Cube"
        }

    elif shape == "Sphere":
        r = val1
        return {
            "formula": "V = 4/3 π r³ | SA = 4π r²",
            "volume": (4/3) * math.pi * r**3,
            "surface": 4 * math.pi * r**2,
            "example": "Football, Ball"
        }

    elif shape == "Cylinder":
        r, h = val1, val2
        return {
            "formula": "V = πr²h | SA = 2πr(h+r)",
            "volume": math.pi * r**2 * h,
            "surface": 2 * math.pi * r * (h+r),
            "example": "Water Tank, Candle"
        }

    elif shape == "Cone":
        r, h = val1, val2
        l = math.sqrt(r**2 + h**2)
        return {
            "formula": "V = 1/3 πr²h | SA = πr(r+l)",
            "volume": (1/3) * math.pi * r**2 * h,
            "surface": math.pi * r * (r+l),
            "example": "Ice Cream Cone"
        }

    elif shape == "Square Pyramid":
        a, h = val1, val2
        l = math.sqrt((a/2)**2 + h**2)
        return {
            "formula": "V = 1/3 a²h | SA = a² + 2al",
            "volume": (1/3) * a**2 * h,
            "surface": a**2 + 2*a*l,
            "example": "Egyptian Pyramid"
        }

    elif shape == "Rectangular Prism":
        l, w, h = val1, val2, val3
        return {
            "formula": "V = lwh | SA = 2(lw+wh+lh)",
            "volume": l * w * h,
            "surface": 2*(l*w + w*h + l*h),
            "example": "Bricks, Boxes"
        }

    elif shape == "Hemisphere":
        r = val1
        return {
            "formula": "V = 2/3 π r³ | SA = 3π r²",
            "volume": (2/3) * math.pi * r**3,
            "surface": 3 * math.pi * r**2,
            "example": "Dome"
        }

    return None
