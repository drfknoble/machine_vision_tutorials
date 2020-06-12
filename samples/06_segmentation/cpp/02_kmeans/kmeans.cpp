#include <iostream>
#include <opencv2/opencv.hpp>
#include <vector>

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

	// k-means

	for (int K = 2; K < 14; K += 2)
	{

		cv::Mat data;

		img.convertTo(data, CV_32F);

		data = data.reshape(1, static_cast<int>(data.total()));

		cv::TermCriteria criteria = cv::TermCriteria(cv::TermCriteria::EPS | cv::TermCriteria::MAX_ITER, 10, 1.0);

		cv::Mat labels, centers;

		cv::kmeans(data, K, labels, criteria, 3, cv::KMEANS_PP_CENTERS, centers);

		centers = centers.reshape(3, centers.rows);
		
		data = data.reshape(3, data.rows);

		cv::Vec3f *p = data.ptr<cv::Vec3f>();

		for (int i = 0; i < data.rows; i++)
		{
			int center_id = labels.at<int>(i);
			p[i] = centers.at<cv::Vec3f>(center_id);
		}

		data = data.reshape(3, img.rows);
		data.convertTo(data, CV_8U);

		std::stringstream ss;

		ss << "Quantized image, K = " << K;

		cv::imshow(ss.str(), data);
		cv::waitKey(0);

		ss = std::stringstream();

		ss << "data/quantized_img_" << K << ".png";

		cv::imwrite(ss.str(), data);
	}

	cv::destroyAllWindows();

	return 0;
}