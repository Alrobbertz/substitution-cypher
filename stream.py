
registers = [0, 0, 0, 1, 1, 0, 1, 0, 0]
connections = [0, 2, 3, 4, 8]


def feedback(registers, connections):
    feed = 0
    for link in connections:
        feed = feed ^ registers[link]
    return feed


def tick(registers, connections):
    feed = feedback(registers, connections)
    lenght = len(registers)
    out = registers[lenght-1]
    for i in range(lenght):
        registers[lenght-i-1] = registers[lenght-i-2]
    registers[0] = feed
    return out


output = []
for i in range(30):
    output.append(tick(registers=registers, connections=connections))

print output


plain = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0,
         1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0]

ciphertext = [output[i] ^ plain[i] for i in range(len(plain))]


print ciphertext
