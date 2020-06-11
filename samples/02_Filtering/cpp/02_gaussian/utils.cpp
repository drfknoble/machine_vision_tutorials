#include "utils.hpp"

void add_gaussian_noise(const cv::Mat& in, cv::Mat* out)
{

	int rows = in.rows;
	int cols = in.cols;

	double mean = 0.0;
	double var = 1.0;
	double sigma = std::pow(var, 0.5);

	std::default_random_engine generator;
	std::normal_distribution<double> distribution(mean, sigma);

	std::vector<uint> vec_data;
	for (int i = 0; i < (rows * cols); i++)
	{
		vec_data.push_back(static_cast<uint>(255.0 * distribution(generator)));
	}

	cv::Mat noisy_img = cv::Mat(rows, cols, CV_8U, vec_data.data());

	cv::addWeighted(in, 1.0, noisy_img, 0.2, 0.0, *out);

	return;

}

void add_salt_pepper_noise(const cv::Mat& in, cv::Mat* out)
{

	int rows = in.rows;
	int cols = in.cols;

	double ratio = 0.5;
	double volume = 0.01;

	std::default_random_engine generator;
	std::uniform_int_distribution<int> row_distribution(1, rows-1);
	std::uniform_int_distribution<int> col_distribution(1, cols-1);

	auto row = std::bind(row_distribution, generator);
	auto col = std::bind(col_distribution, generator);

	int salt = static_cast<int>(std::ceil(volume * rows * cols * ratio));
	int pepper = static_cast<int>(std::ceil(volume * rows * cols * (1 - ratio)));

	*out = in.clone();

	for(int i = 0; i < salt; i++)
	{
		out->at<uint8_t>(cv::Point(col(), row())) = 255;
	}

	for(int i = 0; i < pepper; i++)
	{
		out->at<uint8_t>(cv::Point(col(), row())) = 0;
	}

	return;

}
