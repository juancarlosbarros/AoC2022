"""
AOC2022
Day7
"""

# Part 1
datas = open('7.txt')
line = datas.readline()
path = "/"
content = {}
line = datas.readline()
while line != "":
    line = line.strip()
    if line[0:4] == "$ cd":
        if line[5:] == "..":
            right = path.rfind("/", 0, -2)
            path = path[:right+1]
        else:
            path += line[5:] + "/"
    elif line[0:4] == "$ ls":
        content[path] = [0]
    elif line[0:3] == "dir":
        content[path].append(path + line[4:] + "/")
    elif line.split()[0].isnumeric():
        content[path][0] += int(line.split()[0])
    else:
        print("error:", line)
    line = datas.readline()

def sizeof(path):
    sizes = {}
    if path in sizes:
        return sizes[path]
    elif len(content[path]) == 1:
        total = content[path][0]
        sizes[path] = total
        return total
    else:
        total = content[path][0]
        for i in range(1, len(content[path])):
            total += sizeof(content[path][i])
        sizes[path] = total
        return total

part1 = 0
for path in content:
    size_path = sizeof(path)
    if size_path <= 100000:
        part1 += size_path
        # print("+", size_path, "=", part1)
print("Part1")
print(part1)

# Part2
print("Part2")
size_root = sizeof("/")
min_deletion = size_root - 40000000
print("looking for the smallest dir larger than:")
print(size_root, "- 40000000 = ", min_deletion)
min_found = size_root
for path in content:
    size_path = sizeof(path)
    if min_found > size_path >= min_deletion:
        min_found = size_path
        # print("+", size_path, "=", part1)
print(min_found)