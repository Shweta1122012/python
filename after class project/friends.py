import math
a = 8
b = 9
c = 7
d = 5

angle_deg = 120
angle_rad = math.radians(angle_deg)

def next_point(x, y, length, angle):
    return (x + length * math.cos(angle), y + length * math.sin(angle))

points = [(0, 0)]
angles = [0]  

lengths = [a, b, c, d]
for i in range(4):
    prev_x, prev_y = points[-1]
    angle = angles[-1]
    new_x, new_y = next_point(prev_x, prev_y, lengths[i], angle)
    points.append((new_x, new_y))
    angles.append(angle + angle_rad)

x4, y4 = points[4]
vx = -x4
vy = -y4
theta_e = angles[4]
theta_f = angles[4] + angle_rad
A = [
    [math.cos(theta_e), math.cos(theta_f)],
    [math.sin(theta_e), math.sin(theta_f)]
]
b_vec = [vx, vy]
det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
if det == 0:
    e, f = None, None
else:
    det_e = b_vec[0]*A[1][1] - A[0][1]*b_vec[1]
    det_f = A[0][0]*b_vec[1] - b_vec[0]*A[1][0]
    e = det_e / det
    f = det_f / det
if e > 0 and f > 0:
    print(f"The remaining sides are: e = {e:.2f}, f = {f:.2f}")
else:
    print("Calculated side lengths are not valid (negative or zero).")
