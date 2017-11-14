import numpy as np


def get_sorted_indices(data_points):
    indexed_coordinates = []

    for index, data_point in data_points.items():
        indexed_coordinate = [index]
        for coordinate in data_point.split()[1].split(':'):
            indexed_coordinate.append(int(coordinate))
        indexed_coordinates.append(indexed_coordinate)

    indexed_coordinates = np.array(indexed_coordinates)

    return indexed_coordinates[np.lexsort((indexed_coordinates[:, 2], indexed_coordinates[:, 3], indexed_coordinates[:, 1]))][:, 0]


def main():

    with open("../../data/arxiv_ordered.txt", "w") as ordered_data_file:
        with open("../../data/arxiv_unordered.txt", "r") as unordered_data_file:
            coordinates = ''
            data_points = {}
            for index, data in enumerate(unordered_data_file):
                if data == "\n":
                    if data_points:
                        ordered_data_file.write(coordinates)
                        for ordered_index in get_sorted_indices(data_points=data_points):
                            ordered_data_file.write(data_points[ordered_index])
                        ordered_data_file.write("\n")
                        data_points = {}

                else:
                    if len(data.split()) > 1:
                        data_points[index] = data
                    else:
                        coordinates = data

    pass


if __name__ == '__main__':
    main()
