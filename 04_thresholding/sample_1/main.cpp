#include "main.hpp"

int main(int argc, char* argv[]) {

	cv::Mat image{ cv::Mat(cv::Size(640, 480), CV_8UC1, cv::Scalar(0)) };

	cv::circle(image, cv::Point(320, 240), 50, cv::Scalar(125), -1);

	cv::imshow("image", image);

	cv::waitKey(1);

	cv::Mat imageThreshold;

	cv::threshold(image, imageThreshold, 124, 255, cv::THRESH_BINARY);

	cv::imshow("imageThreshold", imageThreshold);

	cv::waitKey(0);

	cv::destroyAllWindows();

    return 0;
    
}