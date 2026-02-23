import csv
with open("test.csv","r") as f:
    next (f)
    for line in f:
        data = line.strip().split(",")
        print(data)
        anh = data[0]
        x = data[1]
        y = data[2]
        print(f"Anh: {anh}, X: {x}, Y: {y}")