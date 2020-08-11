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

    cv::destroyAllWindows();

    return 0;
}