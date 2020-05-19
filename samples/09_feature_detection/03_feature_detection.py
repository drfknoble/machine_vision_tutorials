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
    cv.waitKey(0)
   
    data = open("data/detected_features.json", "w")

    json_data = {}

    # KAZE

    start = time.time()

    kaze = cv.KAZE_create()
    kp = kaze.detect(img, None)
    kp, des = kaze.compute(img, kp)

    elapsed = time.time() - start

    kaze_img = cv.drawKeypoints(img, kp, None, color=[0, 0, 255])

    cv.imshow("KAZE Features", kaze_img)
    cv.waitKey(0)
    cv.imwrite("data/kaze_features.png", kaze_img)

    json_data.update( \
    { "KAZE" :
        {
            "detected_kepoints": len(kp),
            "time_to_create_detect_compute": elapsed
        }
    })

    # json.dump(json_data, data)

    # AKAZE

    start = time.time()

    akaze = cv.AKAZE_create()
    kp = akaze.detect(img, None)
    kp, des = akaze.compute(img, kp)

    elapsed = time.time() - start

    akaze_img = cv.drawKeypoints(img, kp, None, color=[0, 0, 255])

    cv.imshow("AKAZE Features", akaze_img)
    cv.waitKey(0)
    cv.imwrite("data/akaze_features.png", akaze_img)

    json_data.update( \
    { "AKAZE" : 
        {
            "detected_kepoints": len(kp),
            "time_to_create_detect_compute": elapsed
        }
    })

    # json.dump(json_data, data)

    # FAST

    start = time.time()

    fast = cv.FastFeatureDetector_create()
    kp = fast.detect(img, None)
    # kp, des = fast.compute(img, kp)

    elapsed = time.time() - start

    fast_img = cv.drawKeypoints(img, kp, None, color=[0, 0, 255])

    cv.imshow("FAST Features", fast_img)
    cv.waitKey(0)
    cv.imwrite("data/fast_features.png", fast_img)

    json_data.update( \
    {"FAST":
        {
            "detected_kepoints": len(kp),
            "time_to_create_detect": elapsed,
            "NOTE": "only a feature detector."
        }
     })

    # json.dump(json_data, data)

    # BRISK

    start = time.time()

    brisk = cv.BRISK_create()
    kp = brisk.detect(img, None)
    kp, des = brisk.compute(img, kp)

    elapsed = time.time() - start

    brisk_img = cv.drawKeypoints(img, kp, None, color=[0, 0, 255])

    cv.imshow("BRISK Features", brisk_img)
    cv.waitKey(0)
    cv.imwrite("data/brisk_features.png", brisk_img)

    json_data.update( \
    { "BRISK" :
        {
            "detected_kepoints": len(kp),
            "time_to_create_detect_compute": elapsed
        }
    })

    # json.dump(json_data, data)

    # ORB 500

    start = time.time()

    orb = cv.ORB_create(nfeatures = 500)
    kp = orb.detect(img, None)
    kp, des = orb.compute(img, kp)

    elapsed = time.time() - start

    orb_img = cv.drawKeypoints(img, kp, None, color=[0, 0, 255])

    cv.imshow("ORB Features", orb_img)
    cv.waitKey(0)
    cv.imwrite("data/orb_features.png", orb_img)

    json_data.update( \
    { "ORB 500" :
        {
            "detected_kepoints": len(kp),
            "time_to_create_detect_compute": elapsed
        }
    })

    # json.dump(json_data, data)

    # ORB 1000

    start = time.time()

    orb = cv.ORB_create(nfeatures = 1000)
    kp = orb.detect(img, None)
    kp, des = orb.compute(img, kp)

    elapsed = time.time() - start

    orb_img = cv.drawKeypoints(img, kp, None, color=[0, 0, 255])

    cv.imshow("ORB Features", orb_img)
    cv.waitKey(0)
    cv.imwrite("data/orb_features.png", orb_img)
  
    json_data.update( \
    { "ORB 1000" :
        {
            "detected_kepoints": len(kp),
            "time_to_create_detect_compute": elapsed
        }
    })

    # json.dump(json_data, data)

    # MSER

    start = time.time()

    mser = cv.MSER_create()
    kp = mser.detect(img, None)
    # kp, des = mser.compute(img, kp)

    elapsed = time.time() - start

    mser_img = cv.drawKeypoints(img, kp, None, color=[0, 0, 255])

    cv.imshow("MSER Features", mser_img)
    cv.waitKey(0)
    cv.imwrite("data/msr_features.png", mser_img)
    
    json_data.update( \
    {"MSER":
        {
            "detected_kepoints": len(kp),
            "time_to_create_detect": elapsed,
            "NOTE": "only a feature detector."
        }
     })

    # json.dump(json_data, data)

    # Simple

    start = time.time()

    simple = cv.SimpleBlobDetector_create()
    kp = simple.detect(img, None)
    # kp, des = simple.compute(img, kp)

    elapsed = time.time() - start

    simple_img = cv.drawKeypoints(img, kp, None, color=[0, 0, 255])

    cv.imshow("Simple Features", simple_img)
    cv.waitKey(0)
    cv.imwrite("data/simple_features.png", simple_img)

    json_data.update( \
    {"Simple":
        {
            "detected_kepoints": len(kp),
            "time_to_create_detect": elapsed,
            "NOTE": "only a feature detector."
        }
     })

    # json.dump(json_data, data)

#     # SIFT

#     start = time.time()

#     sift = cv.xfeatures2d.SIFT_create()
#     kp = sift.detect(img, None)
#     kp, des = sift.compute(img, kp)

#     elapsed = time.time() - start

#     # , flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#     sift_img = cv.drawKeypoints(img, kp, None, color=[0, 0, 255])

#     cv.imshow("SIFT Features", sift_img)
#     cv.waitKey(0)
#     cv.imwrite("sift_features.png", sift_img)

#     json_data.update( \
#     { "SIFT" :
#         {
#             "detected_kepoints": len(kp),
#             "time_to_create_detect_compute": elapsed
#         }
#     })

#     # json.dump(json_data, data)

#     # SURF

#     start = time.time()

#     surf = cv.xfeatures2d.SURF_create()
#     kp = surf.detect(img, None)
#     kp, des = surf.compute(img, kp)

#     elapsed = time.time() - start

#     # , flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#     surf_img = cv.drawKeypoints(img, kp, None, color=[0, 0, 255])

#     cv.imshow("SURF Features", surf_img)
#     cv.waitKey(0)
#     cv.imwrite("surf_features.png", surf_img)

#     json_data.update( \
#     { "SURF" :
#         {
#             "detected_kepoints": len(kp),
#             "time_to_create_detect_compute": elapsed
#         }
#     })

#     # json.dump(json_data, data)

#    # STAR

#     start = time.time()

#     star = cv.xfeatures2d.StarDetector_create()
#     kp = star.detect(img, None)
#     # kp, des = star.compute(img, kp)

#     elapsed = time.time() - start

#     star_img = cv.drawKeypoints(img, kp, None, color=[0, 0, 255])

#     cv.imshow("STAR Features", star_img)
#     cv.waitKey(0)
#     cv.imwrite("star_features.png", star_img)

#     json_data.update( \
#     {"STAR":
#         {
#             "detected_kepoints": len(kp),
#             "time_to_create_detect": elapsed,
#             "NOTE": "only a feature detector."
#         }
#      })

    json.dump(json_data, data)

    cv.destroyAllWindows()

    data.close()

    return
  

if __name__ == "__main__":

    main()
