#include <iostream>
#include <opencv2/opencv.hpp>
#include <cmath>

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

	// Kernel, K = [0, 0, 0; 0, 1, 0; 0, 0, 0]

	float data_1[]{ 0, 0, 0,
					0, 1, 0,
					0, 0, 0 };
	cv::Mat kernel_1 = cv::Mat(3, 3, CV_32F, data_1);

	cv::Mat I_img;
	cv::filter2D(img, I_img, CV_8UC3, kernel_1);

	cv::imshow("Identity Image", I_img);
	cv::waitKey(0);
	cv::imwrite("data/I_img.png", I_img);

	// Kernel, K = [0, -1, 0; -1, 5, -1; 0, -1, 0]

	float data_2[]{ 0, -1, 0,
					-1, 5, -1,
					0, -1, 0 };
	cv::Mat kernel_2 = cv::Mat(3, 3, CV_32F, data_2);

	cv::Mat sharp_img;
	cv::filter2D(img, sharp_img, CV_8UC3, kernel_2);

	cv::imshow("Sharpened Image", sharp_img);
	cv::waitKey(0);
	cv::imwrite("data/sharp_img.png", sharp_img);

	// Kernel, K = 1 / 9 * [1, 1, 1; 1, 1, 1; 1, 1, 1]

	float data_3[]{ 1, 1, 1,
					1, 1, 1,
					1, 1, 1 };
	cv::Mat kernel_3 = (1.0 / 9.0) * cv::Mat(3, 3, CV_32F, data_3);

	cv::Mat box_img;
	cv::filter2D(img, box_img, CV_8UC3, kernel_3);

	cv::imshow("Box Blurred Image", box_img);
	cv::waitKey(0);
	cv::imwrite("data/box_img.png", box_img);

	// Kernel, K = 1 / 16 * [1, 2, 1; 2, 4, 2; 1, 2, 1]

	float data_4[]{ 1, 2, 1,
				    2, 4, 2,
				    1, 2, 1 };
	cv::Mat kernel_4 = (1.0 / 16.0) * cv::Mat(3, 3, CV_32F, data_4);

	cv::Mat gaussian_img;
	cv::filter2D(img, gaussian_img, CV_8UC3, kernel_4);

	cv::imshow("Gaussian Blurred Image", gaussian_img);
	cv::waitKey(0);
	cv::imwrite("data/gaussian_img.png", gaussian_img);

	// Kernel, K = [1, 0, 0; 0, 1, 0; 0, 0, 1]

	float data_5[]{ 1, 0, 0,
					0, 1, 0,
					0, 0, 1 };
	cv::Mat kernel_5 = cv::Mat(3, 3, CV_32F, data_5);

	cv::Mat eye_img;
	cv::filter2D(img, eye_img, CV_8UC3, kernel_5);

	cv::imshow("Eye(3) Image", eye_img);
	cv::waitKey(0);
	cv::imwrite("data/eye_img.png", eye_img);

	// Kernel, K = [0, 1, 0; 1, -4, 1; 0, 1, 0]

	float data_6[]{ -1, -1, -1,
					-1, 8, -1,
					-1, -1, -1 };
	cv::Mat kernel_6 = cv::Mat(3, 3, CV_32F, data_6);

	cv::Mat edge_img;
	cv::filter2D(img, edge_img, CV_8UC3, kernel_6);

	cv::imshow("Edge Image", edge_img);
	cv::waitKey(0);
	cv::imwrite("data/edge_img.png", edge_img);

	cv::destroyAllWindows();

	return 0;
}