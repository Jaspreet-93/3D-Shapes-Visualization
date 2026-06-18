
# visualizer.py
from vpython import canvas, box, sphere, cylinder, cone, pyramid, vector, color
from utils import random_color

# === Fullscreen interactive 3D canvas ===
scene = canvas(
    title="3D Shapes Explorer (Move the Shape with Keyboard)",
    width=1920, height=1080,           # set to your screen resolution
    center=vector(0, 0, 0),
    background=color.white
)
scene.userspin = True   # left-drag: rotate camera
scene.userzoom = True   # scroll: zoom camera
scene.userpan  = True   # right-drag: pan camera
scene.forward  = vector(-1, -1, -1)

# Keeps track of the current shape so we can move it
current_object = None

def _clear_scene():
    """Remove previous objects from the scene."""
    global current_object
    # Hide then remove
    for obj in list(scene.objects):
        obj.visible = False
    while len(scene.objects):
        scene.objects.pop()
    current_object = None

def _object_scale():
    """Pick a good move step based on the size of the current object."""
    if current_object is None:
        return 0.1
    try:
        if hasattr(current_object, "radius") and current_object.radius > 0:
            s = current_object.radius
        elif hasattr(current_object, "size"):
            s = max(current_object.size.x, current_object.size.y, current_object.size.z)
        elif hasattr(current_object, "axis"):
            ax = current_object.axis
            s = (ax.x**2 + ax.y**2 + ax.z**2) ** 0.5
        else:
            s = 1.0
    except:
        s = 1.0
    # 5% of the object’s big dimension, with a small minimum
    return max(0.02, 0.05 * s)

def _on_keydown(evt):
    """Keyboard handler: move the actual object in 3D space."""
    global current_object
    if current_object is None:
        return

    # Base step scales with object size
    step = _object_scale()

    # Shift speeds it up (if modifiers available)
    try:
        if 'shift' in evt.modifiers:
            step *= 4
    except Exception:
        pass

    k = evt.key.lower()

    # Move along axes:
    # X: left/right, Y: up/down, Z: forward/back
    if k in ('a', 'left'):
        current_object.pos.x -= step
    elif k in ('d', 'right'):
        current_object.pos.x += step
    elif k in ('r',):     # up
        current_object.pos.y += step
    elif k in ('f',):     # down
        current_object.pos.y -= step
    elif k in ('w', 'up'):      # forward (towards camera by convention)
        current_object.pos.z += step
    elif k in ('s', 'down'):    # backward (away)
        current_object.pos.z -= step
    elif k == 'space':
        current_object.pos = vector(0, 0, 0)  # reset position to origin

# Bind once when this module is imported
scene.bind('keydown', _on_keydown)

def visualize(shape, val1=0.0, val2=0.0, val3=0.0):
    """
    Draw the requested shape in 3D (click canvas to focus, then use keys):
      - A / D or Left / Right : move left/right (X)
      - R / F                 : move up/down (Y)
      - W / S or Up / Down    : move forward/back (Z)
      - Shift                 : faster movement
      - Space                 : reset to origin
    """
    global current_object
    _clear_scene()
    c = random_color()

    if shape == "Cube":
        s = float(val1)
        current_object = box(size=vector(s, s, s), color=c)

    elif shape == "Sphere":
        r = float(val1)
        current_object = sphere(radius=r, color=c)

    elif shape == "Cylinder":
        r, h = float(val1), float(val2)
        current_object = cylinder(pos=vector(0, 0, 0), axis=vector(0, h, 0), radius=r, color=c)

    elif shape == "Cone":
        r, h = float(val1), float(val2)
        current_object = cone(pos=vector(0, 0, 0), axis=vector(0, h, 0), radius=r, color=c)

    elif shape == "Square Pyramid":
        a, h = float(val1), float(val2)
        current_object = pyramid(size=vector(a, h, a), color=c)

    elif shape == "Rectangular Prism":
        l, h, w = float(val1), float(val2), float(val3)
        current_object = box(size=vector(l, h, w), color=c)

    elif shape == "Hemisphere":
        r = float(val1)
        # Simple visual: translucent sphere (hemisphere mesh is more advanced)
        current_object = sphere(radius=r, color=c, opacity=0.7)

    # Nice initial view
    scene.center = vector(0, 0, 0)
    scene.autoscale = True
