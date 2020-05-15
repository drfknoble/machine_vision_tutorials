#include "main.hpp"

int main(int argc, char* argv[]) {

	cv::Mat image{ cv::Mat(cv::Size(640, 480), CV_8UC1, cv::Scalar(0)) };

	cv::circle(image, cv::Point(320, 240), 50, cv::Scalar(125), -1);

	cv::Mat thresholdedImage;

	cv::threshold(image, thresholdedImage, 124, 255, cv::THRESH_BINARY);

	cv::imshow("thresholdedImage", thresholdedImage);

	cv::waitKey(1);

	int elementSize = 10;
	cv::Mat element = cv::getStructuringElement(cv::MORPH_ELLIPSE, cv::Size(2 * elementSize + 1, 2 * elementSize + 1), cv::Point(elementSize, elementSize));

	std::cout << element << std::endl;

	cv::Mat erodedImage;

	cv::erode(thresholdedImage, erodedImage, element);

	cv::imshow("erodedImage", erodedImage);
	cv::waitKey(1);

	cv::Mat dilatedImage;

	cv::dilate(thresholdedImage, dilatedImage, element);

	cv::imshow("dilatedImage", dilatedImage);
	cv::waitKey(1);

	cv::waitKey(0);

	cv::destroyAllWindows();

    return 0;
    
}