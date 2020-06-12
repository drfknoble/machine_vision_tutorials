#include <iostream>
#include <opencv2/opencv.hpp>
#include <vector>

int main(int argc, char *argv[])
{

	// load image

	cv::Mat img = cv::imread("data/apples.png");

	if (img.empty())
	{
		std::cout << "ERROR::CV::Could not read image." << std::endl;
		return 1;
	}

	int rows = img.rows;
	int cols = img.cols;
	int channels = img.type();

    rows = static_cast<int>(floor(rows / 2));
	cols = static_cast<int>(floor(cols / 2));

	cv::resize(img, img, cv::Size(cols, rows));
		
	cv::imshow("img", img);
	cv::waitKey(0);

	// Blue channel

	cv::Mat blue;

	// extract a desired channel
	cv::extractChannel(img, blue, 0);

	cv::imshow("blue", blue);
	cv::waitKey(0);
	cv::imwrite("data/blue.png", blue);

	// modify single channel
	cv::Mat blue_colorized = cv::Mat(rows, cols, CV_8UC3, cv::Scalar(0, 0, 0));

	std::vector<cv::Mat> blue_channels;

	cv::split(blue_colorized, blue_channels);

	blue_channels[0] = blue;

	cv::merge(blue_channels, blue_colorized);

	cv::imshow("blue_colorized", blue_colorized);
	cv::waitKey(0);
	cv::imwrite("data/blue_colorized.png", blue_colorized);

	// Green channel

	cv::Mat green;

	// extract a desired channel
	cv::extractChannel(img, green, 1);

	cv::imshow("green", green);
	cv::waitKey(0);
	cv::imwrite("data/green.png", green);

	// modify single channel
	cv::Mat green_colorized = cv::Mat(rows, cols, CV_8UC3, cv::Scalar(0, 0, 0));

	std::vector<cv::Mat> green_channels;

	cv::split(green_colorized, green_channels);

	green_channels[1] = green;

	cv::merge(green_channels, green_colorized);

	cv::imshow("green_colorized", green_colorized);
	cv::waitKey(0);
	cv::imwrite("data/green_colorized.png", green_colorized);

	// Red channel
	
	cv::Mat red;

	// extract a desired channel
	cv::extractChannel(img, red, 2);

	cv::imshow("red", red);
	cv::waitKey(0);
	cv::imwrite("data/red.png", red);

	// modify single channel
	cv::Mat red_colorized = cv::Mat(rows, cols, CV_8UC3, cv::Scalar(0, 0, 0));

	std::vector<cv::Mat> red_channels;

	cv::split(red_colorized, red_channels);

	red_channels[2] = red;

	cv::merge(red_channels, red_colorized);

	cv::imshow("red_colorized", red_colorized);
	cv::waitKey(0);
	cv::imwrite("data/red_colorized.png", red_colorized);

    cv::destroyAllWindows();

    return 0;
}