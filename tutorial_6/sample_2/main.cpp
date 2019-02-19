#include "main.hpp"

int main(int argc, char* argv[]) {

	cv::Mat image{ cv::Mat(cv::Size(640, 480), CV_8UC3, cv::Scalar(0, 0, 0)) };

	cv::circle(image, cv::Point(320, 240), 50, cv::Scalar(125, 0, 0), -1);

	cv::imshow("originalImage", image);
	cv::waitKey(1);

	cv::Mat imageHSV;

	cv::cvtColor(image, imageHSV, cv::COLOR_BGR2HSV);

	cv::Mat thresholdedImage;

	cv::inRange(imageHSV, cv::Scalar(115, 0, 0), cv::Scalar(125, 255, 255), thresholdedImage);

	cv::imshow("thresholdedImage", thresholdedImage);

	cv::waitKey(0);

	cv::destroyAllWindows();

    return 0;
    
}