import math

def ladder_height(length, angle_degrees):
    angle_radians = math.pi * angle_degrees / 180
    height = length * math.sin(angle_radians)
    return height

print("Height for (a) 16 feet and 75 degrees:", ladder_height(16, 75))
print("Height for (b) 20 feet and 0 degrees:", ladder_height(20, 0))
print("Height for (c) 24 feet and 45 degrees:", ladder_height(24, 45))
print("Height for (d) 24 feet and 80 degrees:", ladder_height(24, 80))
