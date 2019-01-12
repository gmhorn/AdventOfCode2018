import itertools
#changes = itertools.cycle([3, 3, 4, -2, -4]);
changes = itertools.cycle([int(l) for l in open("input.txt")])
seen = set();
freq = 0;

for c in changes:
    freq += c;
    if freq in seen:
        break
    seen.add(freq);

print(freq)
