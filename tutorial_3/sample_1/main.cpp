#include <filesystem>
#include <iostream>

#include "main.hpp"

namespace fs = std::filesystem;

int main(int argc, char* argv[]) {

	cv::Mat image = cv::Mat(cv::Size(400, 400), CV_8UC3, cv::Scalar(255, 255, 255));

	cv::line(image, cv::Point(100, 50), cv::Point(300, 50), cv::Scalar(0, 0, 0), 10);
	cv::line(image, cv::Point(350, 100), cv::Point(350, 300), cv::Scalar(0, 0, 0), 10);
	cv::line(image, cv::Point(300, 350), cv::Point(100, 350), cv::Scalar(0, 0, 0), 10);
	cv::line(image, cv::Point(50, 300), cv::Point(50, 100), cv::Scalar(0, 0, 0), 10);

	cv::ellipse(image, cv::Point(100, 100), cv::Size(50, 50), 0, 180, 270, cv::Scalar(0, 0, 0), 10);
	cv::ellipse(image, cv::Point(300, 100), cv::Size(50, 50), 0, 270, 360, cv::Scalar(0, 0, 0), 10);
	cv::ellipse(image, cv::Point(100, 300), cv::Size(50, 50), 0, 90, 180, cv::Scalar(0, 0, 0), 10);
	cv::ellipse(image, cv::Point(300, 300), cv::Size(50, 50), 0, 0, 90, cv::Scalar(0, 0, 0), 10);

	cv::circle(image, cv::Point(200, 200), 75, cv::Scalar(0, 0, 0), 10);
	cv::circle(image, cv::Point(300, 100), 25, cv::Scalar(0, 0, 0), -1);

	cv::imshow("image", image);

	cv::waitKey(0);

	cv::destroyAllWindows();

    return 0;
}