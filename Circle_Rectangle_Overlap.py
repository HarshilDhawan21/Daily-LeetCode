class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        xc = max(x1, min(xCenter, x2))
        yc = max(y1, min(yCenter, y2))
        hor, ver = xCenter - xc, yCenter - yc
        return hor*hor + ver*ver <= radius*radius
        