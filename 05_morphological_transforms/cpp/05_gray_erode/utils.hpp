#ifndef __UTILS_HPP__
#define __UTILS_HPP__

#include <cmath>
#include <opencv2/opencv.hpp>
#include <random>
#include <vector>

void add_gaussian_noise(const cv::Mat& in, cv::Mat* out);

void add_salt_pepper_noise(const cv::Mat& in, cv::Mat* out);

#endif //!__UTILS_HPP