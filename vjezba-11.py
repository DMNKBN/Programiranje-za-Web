#Ispišite sve parne brojeve između 1 i 1000 koji su istovremeno djeljivi s 5 i 13

n = 1000

for x in range(1, n+1):
    if x % 2 == 0 and x % 5 == 0 and x % 13 == 0:
        print(x)
