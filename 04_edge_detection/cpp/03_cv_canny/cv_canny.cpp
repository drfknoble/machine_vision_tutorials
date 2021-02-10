#include <iostream>
#include <opencv2/opencv.hpp>

int main(int argc, char* argv[])
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

    // Convert image form BGR to grayscale

    cv::cvtColor(img,img, cv::COLOR_BGR2GRAY);
   
    // OpenCV canny

    cv::Mat canny;

    cv::Canny(img, canny, 25, 255);

    cv::imshow("OpenCV Canny()", canny);
	cv::waitKey(0);
    cv::imwrite("data/01_cv_canny.png", canny);

    cv::destroyAllWindows();

	return 0;
}