import re

"""
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
"""

class Claim:

    def __init__(self, match):
        self.id = match.group(1)
        self.x = int(match.group(2))
        self.y = int(match.group(3))
        self.w = int(match.group(4))
        self.h = int(match.group(5))

    def __str__(self):
        return "#{} @ {},{}: {}x{}".format(self.id, self.x, self.y, self.w, self.h)

regex = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
claims = [Claim(regex.match(s.strip())) for s in open("input.txt")]

def build_quilt(claims):
    quilt = {}
    for claim in claims:
        for x in range(claim.x, claim.x+claim.w):
            for y in range(claim.y, claim.y+claim.h):
                if (x,y) in quilt:
                    quilt[(x,y)] = 'X'
                else:
                    quilt[(x,y)] = 'C'
    return quilt;

def patches(claim, quilt):
    for x in range(claim.x, claim.x + claim.w):
        for y in range(claim.y, claim.y + claim.h):
            yield quilt[(x,y)]

def is_uncontested(claim, quilt):
    for patch in patches(claim, quilt):
        if patch == 'X':
            return False
    return True

def a():
    quilt = build_quilt(claims)
    dup_area = 0
    for coords, mark in quilt.items():
        if (mark == 'X'):
            dup_area += 1
    return dup_area

def b():
    quilt = build_quilt(claims)
    for claim in claims:
        if is_uncontested(claim, quilt):
            return claim.id
    return "none"

if __name__ == "__main__":
    print("a: {}".format(a()))
    print("b: {}".format(b()))
