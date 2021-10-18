import main

for i in range(500):
    for j in range(500):
        assert main.stupid_mul(i, j) == i * j