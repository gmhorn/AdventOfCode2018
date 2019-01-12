from collections import Counter

ids = sorted(list(s.strip() for s in open("input.txt")))

def classify(word):
    two = 0;
    three = 0;
    cnt = Counter(word);
    for (elem, freq) in cnt.items():
        if freq == 2:
            two = 1;
        elif freq == 3:
            three = 1;
    return (two, three)

def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Strings must be equal length")
    return sum(e1 != e2 for e1, e2 in zip(s1, s2))

def a():
    twos = 0
    threes = 0
    for item in ids:
        (is_two, is_three) = classify(item)
        twos += is_two
        threes += is_three
    return twos*threes

def b():
    for i in range(len(ids)):
        s1 = ids[i]
        for s2 in ids[i+1:]:
            if (hamming_distance(s1,s2)==1):
                sol = ''.join([e1 for e1,e2 in zip(s1,s2) if e1==e2])
                return sol
    
if __name__ == "__main__":
    print("a: {}".format(a()))
    print("b: {}".format(b()))
