# Write your solution here
# (2n-1) x (2n-1)
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

layer = int(input("Layers: "))
size = (2 * layer) - 1
center = layer - 1

for i in range(size):
    for j in range(size):
        dist_to_i = abs(i - center)
        dist_to_j = abs(j - center)
        max_dist = max(dist_to_i, dist_to_j)
        print(alphabet[max_dist], end="")
    print()
