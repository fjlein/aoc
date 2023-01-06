input = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""


class Valve:
    all_valves = []

    def __init__(self, name, flowrate):
        self.name = name
        self.flowrate = flowrate
        self.tunnels = set()

    def __str__(self):
        s = ""
        for t in self.tunnels:
            s += t.name + " "
        return self.name + " " + str(self.flowrate) + " -> " + s


valves = {}

lines = input.split("\n")

for line in lines:
    line = line.split(" ")
    valves[line[1]] = Valve(line[1], int(line[4][5:-1]))

for line in lines:
    line = line.split(" ")
    current = valves[line[1]]
    for tunnel in line[9:]:
        current.tunnels.add(valves[tunnel[:2]])
    # current.tunnels.add()

for valve in valves.values():
    print(valve)

print("##########")


current = valves["AA"]
for i in range(30):
    # entweder move

    # oder öffnen









    print(str(i) + " " + str(current))
    high = list(current.tunnels)[0]
    for tunnel in current.tunnels:
        if tunnel.flowrate > high.flowrate:
            high = tunnel
    print(high)
