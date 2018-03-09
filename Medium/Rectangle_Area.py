"""
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

"""


class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):

        width = min(C, G) - max(A, E)
        height = min(D, H) - max(B, F)

        if width <= 0 or height <= 0:
            return (C - A) * (D - B) + (G - E) * (H - F)
        else:
            return (C - A) * (D - B) + (G - E) * (H - F) - width * height
