import glob
fuck = glob.glob('*.txt')
for i in fuck:
    with open(i) as filelocall:
            print(filelocall.read())



