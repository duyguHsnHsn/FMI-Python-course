
def fix_x_against_borders(x):
    if x < 0:
        x = 0
    if x > 830:
        x = 830
    return x
