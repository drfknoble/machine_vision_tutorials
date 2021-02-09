#include <cmath>
#include <iostream>

#include "utils.hpp"

int main(int argc, char* argv[])
{

    // Load image

    cv::Mat img = cv::imread("data/apples.png");

    if(img.empty())
    {
        std::cout << "ERROR::CV::Could not read image." << std::endl;
        return 1;
    }

    int rows = img.rows;
    int cols = img.cols;
    int type = img.type();

    rows = static_cast<int>(std::floor(rows / 2));
    cols = static_cast<int>(std::floor(cols / 2));

    cv::resize(img, img, cv::Size(cols, rows));

    cv::imshow("img", img);
    cv::waitKey(0);

    // Convert image from BGR to grayscale

    cv::cvtColor(img, img, cv::COLOR_BGR2GRAY);

    // Apply salt and pepper noise to img

    cv::Mat noisy_img;

    add_salt_pepper_noise(img, &noisy_img);

    cv::imshow("noisy_img", noisy_img);
    cv::waitKey(0);
    cv::imwrite("data/salt_noise_apples.png", noisy_img);

    // Use a median filter to remove noise

    cv::Mat filtered_img;

    cv::medianBlur(noisy_img, filtered_img, 3);

    cv::imshow("filtered_img", filtered_img);
    cv::waitKey(0);
    cv::imwrite("data/median_filtered_apples.png", filtered_img);

    cv::destroyAllWindows();

    return 0;
}