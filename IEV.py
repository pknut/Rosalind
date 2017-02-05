def IEV():
    """Calculating Expected Offspring"""
    with open('data2.txt', 'r') as f:
        read_data = [int(i) for i in next(f).split()]

    print(read_data[0] + read_data[1] + read_data[2] + read_data[3]*0.75 + read_data[4]*0.5)*2