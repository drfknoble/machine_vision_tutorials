#include <iostream>
#include <opencv2/opencv.hpp>
#include <random>
#include <vector>

int main(int argc, char *argv[])
{

	// Create shapes

	int rows = 480;
	int cols = 640;

	cv::Mat img = cv::Mat(rows, cols, CV_8U, cv::Scalar(0));

	std::default_random_engine pos_generator;
	std::uniform_int_distribution row_distribution(1, rows - 1);
	std::uniform_int_distribution col_distribution(1, cols - 1);

	auto row = std::bind(row_distribution, pos_generator);
	auto col = std::bind(col_distribution, pos_generator);

	std::vector<cv::Point> coordinates;

	for (int i = 0; i < 40; i++)
	{
		coordinates.push_back(cv::Point(col(), row()));
	}

	for (auto c : coordinates)
	{	
		cv::circle(img, c, 10, cv::Scalar(255), -1);
	}

	cv::imshow("img", img);
	cv::waitKey(0);
	cv::imwrite("data/img.png", img);

	// Find contours

	std::vector<std::vector<cv::Point>> contours;
	std::vector<cv::Vec4i> hierarchy;

	cv::findContours(img, contours, hierarchy, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);
	
	std::default_random_engine color_generator;
	std::uniform_int_distribution color_distribution(0, 255);

	auto color = std::bind(color_distribution, color_generator);

	cv::Mat labelled_img = cv::Mat(480, 640, CV_8UC3, cv::Scalar(0, 0, 0));

	for (int i = 0; i < contours.size(); i++)
	{

		cv::Scalar rgb = cv::Scalar(color(), color(), color());

		cv::drawContours(labelled_img, contours, i, rgb, -1);

	}

	cv::imshow("labelled_img", labelled_img);
	cv::waitKey(0);
	cv::imwrite("data/labelled_img.png", labelled_img);

	cv::destroyAllWindows();

	return 0;
}