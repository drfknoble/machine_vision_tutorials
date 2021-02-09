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

    cv::Mat yuv_img;
	
	cv::cvtColor(img, yuv_img, cv::COLOR_BGR2YUV);

	// y channel
	
	cv::Mat y;

	cv::extractChannel(yuv_img, y, 0);

	cv::imshow("y", y);
	cv::waitKey(0);
	cv::imwrite("data/y.png", y);

	// u channel

	cv::Mat u;

	cv::extractChannel(yuv_img, u, 1);

	cv::imshow("u", u);
	cv::waitKey(0);
	cv::imwrite("data/u.png", u);

	// v channel

	cv::Mat v;

	cv::extractChannel(yuv_img, v, 2);

	cv::imshow("v", v);
	cv::waitKey(0);
	cv::imwrite("data/v.png", v);

    cv::destroyAllWindows();

    return 0;
}