#include <iostream>
#include <opencv2/opencv.hpp>

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

	// Covert from BGR color space to RGB color space

    cv::Mat rgb_img;
	
	cv::cvtColor(img, rgb_img, cv::COLOR_BGR2RGB);

	// Red channel
	
	cv::Mat red;

	cv::extractChannel(rgb_img, red, 0);

	cv::imshow("red", red);
	cv::waitKey(0);
	cv::imwrite("data/red.png", red);

	// Green channel

	cv::Mat green;

	cv::extractChannel(rgb_img, green, 1);

	cv::imshow("green", green);
	cv::waitKey(0);
	cv::imwrite("data/green.png", green);

	// Blue channel

	cv::Mat blue;

	cv::extractChannel(rgb_img, blue, 2);

	cv::imshow("blue", blue);
	cv::waitKey(0);
	cv::imwrite("data/blue.png", blue);

    cv::destroyAllWindows();

    return 0;
}