def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev_row = triangle[i - 1]
            new_row = [1]

            for j in range(1, i):
                new_value = prev_row[j - 1] + prev_row[j]
                new_row.append(new_value)
            new_row.append(1)
            triangle.append(new_row)

    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 3))

n = int(input("Enter the number of rows for Pascal's Triangle: "))
triangle = generate_pascals_triangle(n)
print_pascals_triangle(triangle)

