import itertools


class Switch:
    def __init__(self, win, lose, nothing, name):
        self.win = win
        self.lose = lose
        self.nothing = nothing
        self.name = name


A = Switch(0.53, 0.21, 0.26, 'A')
B = Switch(0.04, 0.27, 0.69, 'B')
C = Switch(0.04, 0.95, 0.01, 'C')
D = Switch(0.59, 0.21, 0.20, 'D')
E = Switch(0.22, 0.34, 0.44, 'E')
F = Switch(0.43, 0.41, 0.16, 'F')
G = Switch(0.32, 0.28, 0.40, 'G')
H = Switch(0.13, 0.66, 0.21, 'H')
I_ = Switch(0.06, 0.26, 0.68, 'I')
J = Switch(0.42, 0.10, 0.48, 'J')
K = Switch(0.20, 0.33, 0.47, 'K')
L = Switch(0.07, 0.44, 0.49, 'L')


def evaluate_sequence(lst):
    nothing = 1
    win_prob = 0
    for elem in lst:
        win_prob += nothing * elem.win
        nothing = nothing * elem.nothing
    return win_prob


Switches = [A, B, C, D, E, F, G, H, I_, J, K, L]

max_prob = 0
best_perm = None
# This might take 5-10 min, we are searching 479'000'000 permutations!
for perm in itertools.permutations(Switches):
    _win_prob = evaluate_sequence(perm)
    if _win_prob > max_prob:
        max_prob = _win_prob
        best_perm = perm

print([e.name for e in best_perm])
print(max_prob)
