#include "utils.hpp"

void add_gaussian_noise(const cv::Mat& in, cv::Mat* out)
{

	int rows = in.rows;
	int cols = in.cols;

	double mean = 0.0;
	double var = 1.0;
	double sigma = std::pow(var, 0.5);

	std::default_random_engine generator;
	std::normal_distribution<float> distribution(mean, sigma);

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

	return;

}
