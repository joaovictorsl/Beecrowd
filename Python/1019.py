t = int(input())
h = t//3600
m = t//60-h*60
s = t-h*3600-m*60
print("{}:{}:{}".format(h, m, s))