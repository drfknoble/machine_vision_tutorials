#include <iostream>

#include "utils.hpp"

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

	// Convert image from BGR to grayscale

	cv::cvtColor(img, img, cv::COLOR_BGR2GRAY);

	// Apply gaussian noise to img

	cv::Mat noisy_img;
	add_gaussian_noise(img, &noisy_img);

	cv::imshow("noisy_img", noisy_img);
	cv::waitKey(0);
	cv::imwrite("data/gaussian_noise_apples.png", noisy_img);

	// Use a gaussian filter to remove noise

	cv::Mat filtered_img;
	cv::GaussianBlur(noisy_img, filtered_img, cv::Size(3, 3), 0);

	cv::imshow("gaussian_filtered_img", filtered_img);
	cv::waitKey(0);
	cv::imwrite("data/gaussian_filtered_apples.png", filtered_img);

	cv::destroyAllWindows();

    return 0;
}