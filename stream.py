# Set the Initial State in the Registers
registers = [0, 0, 0, 1, 1, 0, 1, 0, 0]
# Set which registers contribute to feedback
# WARNING: index 0 in the array actually represents register 8, and index 7 in the array represents register 0
connections = [0, 2, 3, 4, 8]


# Generate the Feedback Bit given connections
def feedback(registers, connections):
    feed = 0
    for link in connections:
        feed = feed ^ registers[link]
    return feed


# Do one clock cycle of the registers
def tick(registers, connections):
    # Find the feedback bit
    feed = feedback(registers, connections)
    lenght = len(registers)
    # Find the output bit
    out = registers[-1]
    for i in range(lenght):
        registers[lenght-i-1] = registers[lenght-i-2]
    registers[0] = feed
    return out


# Do 30 clock cycles on the registers
output = []
for i in range(30):
    output.append(tick(registers=registers, connections=connections))

print("LFSR Out:", output)


# Vernam Cipher Plaintext
plain = [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0,
         1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0]
# Reverse the LFSR output, so that the least significant bits match (Both supposed to be at index [-1])
output.reverse()

# Do a bit-wise XOR of the plaintext and LFSR output
ciphertext = [output[i] ^ plain[i] for i in range(len(plain))]

print("Cipher Out:", ciphertext)
