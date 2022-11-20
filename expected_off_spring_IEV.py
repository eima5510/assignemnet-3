def calculate_expectedOffspring(l):
    offsprings_expected = (1*l[0] + 1*l[1] + 1*l[2] + 0.75*l[3] + 0.5*l[4] + 0*l[5]) * 2
    return offsprings_expected 

if __name__ == "__main__":
    data_set="18387 16387 17828 16402 19662 16824"
    l = [float(i) for i in data_set.strip().split(" ")]
    print(calculate_expectedOffspring(l))