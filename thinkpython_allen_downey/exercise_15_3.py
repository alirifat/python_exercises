def move_rectangle(rect, dx, dy):
    import copy
    rect_copy = copy.deepcopy(rect)
    rect_copy.corner.x += dx
    rect_copy.corner.y += dy
    return rect_copy
