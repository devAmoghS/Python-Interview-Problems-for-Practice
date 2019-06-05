# The effective time complexity of this improved version is O(1).
# For the problem statement, refer `josephus.py`

def josephus_v3(soldiers):
    # Convert to binary.
    binary = bin(soldiers)
    # Get the first digit and put it as last.
    shift = '0b' + binary[3::] + binary[2:3:]
    # Convert to decimal.
    return int(shift, 2)

winning = josephus_v3(soldiers=41)
print(winning) #Winning Soldier: 19

winning = josephus_v3(soldiers=100)
print(winning) #Winning Soldier: 73

winning = josephus_v3(soldiers=1000)
print(winning) #Winning Soldier: 977

# Testing:
test_josephus = {
    1: 1,
    2: 1,
    3: 3,
    4: 1,
    5: 3,
    6: 5,
    7: 7,
    8: 1,
    9: 3,
    10: 5,
    11: 7,
    12: 9,
    13: 11,
    16: 1,
    41: 19
}
for soldiers, expected_winner in test_josephus.items():
    assert josephus_v3(soldiers=soldiers) == expected_winner
