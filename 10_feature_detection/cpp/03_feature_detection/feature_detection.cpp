#include <cmath>
#include <fstream>
#include <iostream>
#include <opencv2/opencv.hpp>
#include <rapidjson/document.h>
#include <rapidjson/writer.h>
#include <rapidjson/stringbuffer.h>
#include <sstream>
#include <chrono>

int main(int argc, char *argv[])
{

	// Load image

	cv::Mat img = cv::imread("data/apples.png");

	int rows = img.rows;
	int cols = img.cols;
	int channels = img.type();

	rows = static_cast<int>(std::floor(rows / 2));
	cols = static_cast<int>(std::floor(cols / 2));

	cv::resize(img, img, cv::Size(cols, rows));

	cv::imshow("img", img);
	cv::waitKey(0);

	rapidjson::Document d;

	std::stringstream ss;

	// ss << "{";
	// ss << "\"KAZE\" : { \"detected_keypoints\" : " << 1.0 << ", \"time_to_create_detect_compute\" : "<< 1.0 << " }";
	// ss << ",";
	// ss << "\"KAZE\" : { \"detected_keypoints\" : " << 1.0 << ", \"time_to_create_detect_compute\" : "<< 1.0 << " }";
	// ss << "}";

	ss << "{";

	// KAZE

	std::vector<cv::KeyPoint> kaze_kp;
	cv::Mat kaze_des;

	auto start = std::chrono::steady_clock::now();

	cv::Ptr<cv::KAZE> kaze = cv::KAZE::create();
	kaze->detect(img, kaze_kp);
	kaze->compute(img, kaze_kp, kaze_des);	

	auto stop = std::chrono::steady_clock::now();
	auto elapsed = std::chrono::duration_cast<std::chrono::seconds>(stop - start).count();

	cv::Mat kaze_img;

	cv::drawKeypoints(img, kaze_kp, kaze_img, cv::Scalar(0, 0, 255));

	cv::imshow("KAZE Features", kaze_img);
	cv::waitKey(0);
	cv::imwrite("data/kaze_features.png", kaze_img);

	ss << "\"KAZE\" : { \"detected_keypoints\" : " << kaze_kp.size() << ", \"time_to_create_detect_compute\" : " << elapsed << " }";

	//

	ss << "}";

	d.Parse((ss.str()).c_str());

	rapidjson::StringBuffer buffer;
	rapidjson::Writer<rapidjson::StringBuffer> writer(buffer);

	d.Accept(writer);

	std::ofstream file;
	file.open("data/features.json", std::ios::out);
	file << buffer.GetString() << std::endl;
	file.close();

    cv::destroyAllWindows();

    return 0;
}