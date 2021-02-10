import cv2 as cv
import json
import numpy as np
import time


def main():

    # Load image

    img = cv.imread("data/apples.png")

    if img is None:
        print("ERROR::CV::Could not read image.")
        return

    # Resize image

    rows, cols, channels = img.shape

    rows = rows // 2
    cols = cols // 2

    img = cv.resize(img, (cols, rows))

    cv.imshow("img", img)
    cv.waitKey(1)
    cv.imwrite('../images/03/01.PNG', img)

    data = open("data/matched_features.json", "w")

    json_data = {}

    # Apply a transform

    img = np.float32(img)

    p1 = np.float32([[0, 0], [cols, 0], [0, rows], [cols, rows]])
    p2 = np.float32([[100, 0], [cols-100, 0], [0, rows], [cols, rows]])

    M = cv.getPerspectiveTransform(p1, p2)

    print("Transform: {}".format(M))

    transformed_img = cv.warpPerspective(img, M, (cols, rows))
    transformed_img = np.uint8(transformed_img)

    cv.imshow("Transformed Image", transformed_img)
    cv.waitKey(1)
    cv.imwrite("data/transformed_img.png", transformed_img)
    cv.imwrite('../images/03/02.PNG', transformed_img)

    # ORB

    img = np.uint8(img)
    transformed_img = np.uint8(transformed_img)

    orb = cv.ORB_create(nfeatures=1000)
    kp1, des1 = orb.detectAndCompute(img, None)
    kp2, des2 = orb.detectAndCompute(transformed_img, None)

    json_data.update({
        "ORB":
        {
            "img1_detected_kepoints": len(kp1),
            "img2_detected_kepoints": len(kp2)
        },
    })

    # BF

    best_matches = 20

    start = time.time()

    bf = cv.BFMatcher()
    matches = bf.match(des1, des2)

    elapsed = time.time() - start

    matches = sorted(matches, key=lambda x: x.distance)

    out = cv.drawMatches(img, kp1, transformed_img, kp2,
                         matches[:best_matches], None, [0, 0, 255])

    cv.imshow("BF Matches", out)
    cv.waitKey(1)
    cv.imwrite("data/bf_matched.png", out)
    cv.imwrite('../images/03/03.PNG', out)

    json_data.update({
        "BF":
        {
            "bf_matched_keypoints": len(matches),
            "time_to_match": elapsed
        }

    })

    # FLANN

    FLANN_INDEX_LSH = 6
    index_settings = dict(algorithm=FLANN_INDEX_LSH,
                          table_number=6,
                          key_size=12,
                          multi_probe_level=1)
    search_settings = dict(checks=50)

    start = time.time()

    flann = cv.FlannBasedMatcher(index_settings, search_settings)
    matches = flann.match(des1, des2)

    elapsed = time.time() - start

    matches = sorted(matches, key=lambda x: x.distance)

    out = cv.drawMatches(img, kp1, transformed_img, kp2,
                         matches[:best_matches], None, [0, 0, 255])

    cv.imshow("FLANN Matches", out)
    cv.waitKey(0)
    cv.imwrite("data/flann_matched.png", out)
    cv.imwrite('../images/03/04.PNG', out)

    json_data.update({
        "FLANN":
        {
            "FLANN_matched_keypoints": len(matches),
            "time_to_match": elapsed

        }

    })

    json.dump(json_data, data)

    cv.destroyAllWindows()

    data.close()
    return


if __name__ == "__main__":

    main()
