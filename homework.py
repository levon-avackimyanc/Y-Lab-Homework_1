from itertools import permutations


def calc(point_1, point_2):
    return ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5


points = [(2, 5), (5, 2), (6, 6), (8, 3)]
start_point = (0, 2)

perms = list(permutations(points))
buff = 0
res_list_dist = []
for i in perms:
    list_perms = []
    list_dist = []
    for j in i:
        if i.index(j) == 0:
            list_dist.append(calc(start_point, j))
            list_perms.append(start_point)
            list_perms.append(j)
        else:
            list_dist.append(calc(list_perms[-1], j))
            list_perms.append(j)
    for k in list_dist:
        buff += k
    res_list_dist.append(buff)
    buff = 0
index_of_min_dist = res_list_dist.index(min(res_list_dist))
result_path = [start_point]
result_path += perms[index_of_min_dist]
result_path.append(start_point)
print(start_point, end='')
for i in range(len(result_path) - 1):
    buff += calc(result_path[i], result_path[i + 1])
    print(f' -> {result_path[i + 1]}[{buff}]', end='')
print(f' = {buff} ')
