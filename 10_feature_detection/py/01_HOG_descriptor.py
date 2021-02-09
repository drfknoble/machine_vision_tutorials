import cv2 as cv
import numpy as np

np.set_printoptions(precision=3,
                    suppress=True)

def HOGDescriptor(img=None):

    g_row = np.empty(img.shape, dtype=np.float32)
    g_row[0, :] = 0
    g_row[-1, :] = 0
    g_row[1:-1, :] = img[2:, :] - img[:-2, :]

    g_col = np.empty(img.shape, dtype=np.float32)
    g_col[:, 0] = 0
    g_col[:, -1] = 0
    g_col[:, 1:-1] = img[:, 2:] - img[:, :-2]

    mag = np.hypot(g_row, g_col)
    ang = np.rad2deg(np.arctan2(g_row, g_col)) % 180

    pixels_per_cell = 8
    cells_per_block = 2
    number_of_bins = 9

    s_row, s_col = img.shape
    c_row, c_col = [pixels_per_cell, pixels_per_cell]
    b_row, b_col = [cells_per_block, cells_per_block]
    n_cells_row = s_row // c_row
    n_cells_col = s_col // c_col

    bin_histogram = np.zeros((n_cells_row, n_cells_col, number_of_bins), dtype=np.float32)

    number_of_bins_per_180 = 180 / number_of_bins

    for i in range(number_of_bins):

        orientation_start = number_of_bins_per_180 * i
        orientation_end = number_of_bins_per_180 * (i + 1)

        for r_i, r in enumerate(range(0, s_row, pixels_per_cell)):

            for c_i, c in enumerate(range(0, s_col, pixels_per_cell)):

                total = 0

                for cell_row in range(0, pixels_per_cell):

                    cell_row_index = cell_row + r

                    for cell_col in range(0, pixels_per_cell):

                        cell_col_index = cell_col + c

                        if (ang[cell_row_index, cell_col_index] < orientation_start or
                            ang[cell_row_index, cell_col_index] >= orientation_end):

                            continue

                        total += mag[cell_row_index, cell_col_index]

                bin_histogram[r_i, c_i, i] = total / (pixels_per_cell ** 2)
       
    n_blocks_row = (n_cells_row - b_row) + 1
    n_blocks_col = (n_cells_col - b_col) + 1

    normalised_blocks = np.zeros((n_blocks_row, n_blocks_col, 
                                  b_row, b_col, number_of_bins))

    for r in range(n_blocks_row):

        for c in range(n_blocks_col):

            block = bin_histogram[r:r + b_row, c:c + b_col, :]

            method = 'L2-Hys'
            eps = 1e-3

            if method == 'L1':
                block = block / (np.sum(np.abs(block)) + eps)
            elif method == 'L1-sqrt':
                block = np.sqrt(block / (np.sum(np.abs(block)) + eps))
            elif method == 'L2':
                block = block / np.sqrt(np.sum(block ** 2) + eps ** 2)
            elif method == 'L2-Hys':
                block = block / np.sqrt(np.sum(block ** 2) + eps ** 2)
                block = np.minimum(block, 0.2)
                block = block / np.sqrt(np.sum(block ** 2) + eps ** 2)
            else:
                raise ValueError('Selected block normalization method is invalid.')

            normalised_blocks[r, c, :] = block

    return np.ravel(normalised_blocks)


def main():

    # Load image

    img = cv.imread("data/person.jpg")

    if img is None:
        print("ERROR::CV::Could not read image.")
        return

    # Resize image

    rows, cols, channels = img.shape

    cv.imshow("img", img)
    cv.waitKey(0)

    # Convert image from BGR to grayscale

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img = cv.resize(img, (64, 128))
    img = np.float32(img)

    # Generate HOGDescriptor() function

    fd = HOGDescriptor(img)

    print("fd[0:36]:\n{},\n fd.shape:\n{}".format(fd[0:36], np.shape(fd)))

    cv.destroyAllWindows()

    return


if __name__ == "__main__":

    main()