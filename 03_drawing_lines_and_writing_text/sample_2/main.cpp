#include <filesystem>
#include <iostream>

#include "main.hpp"

int main(int argc, char* argv[]) {

	cv::Mat image = cv::Mat(cv::Size(600, 200), CV_8UC3, cv::Scalar(255, 255, 255));

	cv::putText(image, "OpenCV is Great!", cv::Point(50,100), cv::FONT_HERSHEY_PLAIN, 3, cv::Scalar(0, 0, 0), 3);

	cv::imshow("image", image);

	cv::waitKey(0);

	cv::destroyAllWindows();

    return 0;
}