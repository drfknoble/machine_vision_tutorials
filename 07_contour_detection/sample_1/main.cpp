#include "main.hpp"

int main(int argc, char* argv[]) {

	cv::Mat image{ cv::Mat(cv::Size(640, 480), CV_8UC3, cv::Scalar(0, 0, 0)) };

	cv::circle(image, cv::Point(320, 240), 50, cv::Scalar(255, 0, 0), -1);
	cv::circle(image, cv::Point(320, 240), 20, cv::Scalar(0, 0, 0), -1);

	cv::imshow("image", image);

	cv::waitKey(1);

	cv::Mat imageHSV;

	cv::cvtColor(image, imageHSV, cv::COLOR_BGR2HSV);

	cv::Mat thresholdedImage;

	cv::inRange(imageHSV, cv::Scalar(115, 0, 0), cv::Scalar(125, 255, 255), thresholdedImage);
	   
	std::vector<std::vector<cv::Point>> contours;
	std::vector<cv::Vec4i> hierarchy;

	cv::findContours(thresholdedImage, contours, hierarchy, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);

	for (int i = 0; i < contours.size(); i++) {
		cv::drawContours(image, contours, i, cv::Scalar(0, 0, 255), 2, 8, hierarchy);
	}

	cv::imshow("image", image);

	cv::waitKey(0);

	cv::destroyAllWindows();

    return 0;
    
}