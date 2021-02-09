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

    // Convert image form BGR to grayscale

    cv::cvtColor(img,img, cv::COLOR_BGR2GRAY);
   
    // Vertical edges

    std::vector<float> vertical_data {-1, 0, 1, -2, 0, 2, -1, 0, 1};
    cv::Mat vertical_kernel = cv::Mat(3, 3, CV_32F, vertical_data.data());

    cv::Mat vertical_edges;

    cv::filter2D(img, vertical_edges, CV_32F, vertical_kernel);

    cv::Mat G_x;

    vertical_edges = cv::abs(vertical_edges);
    vertical_edges.convertTo(G_x, CV_8U);

    cv::imshow("Vertical Edges", G_x);
    cv::waitKey(0);
    cv::imwrite("data/01_vertical_edges.png", G_x);

    // Horizontal edges

    std::vector<float> horizontal_data {-1, -2, -1, 0, 0, 0, 1, 2, 1};
    cv::Mat horizontal_kernel = cv::Mat(3, 3, CV_32F, horizontal_data.data());

    cv::Mat horizontal_edges;

    cv::filter2D(img, horizontal_edges, CV_32F, horizontal_kernel);

    cv::Mat G_y;

    horizontal_edges = cv::abs(horizontal_edges);
    horizontal_edges.convertTo(G_y, CV_8U);

    cv::imshow("Horizontal Edges", G_y);
    cv::waitKey(0);
    cv::imwrite("data/02_horizontal_edges.png", G_x);

    // Magnitude edges

    cv::Mat magnitude;

    cv::pow(vertical_edges, 2, vertical_edges);
    cv::pow(horizontal_edges, 2, horizontal_edges);
    cv::sqrt((vertical_edges + horizontal_edges), magnitude);

    cv::Mat G;

    magnitude.convertTo(G, CV_8U);

    cv::imshow("Magnitude", G);
    cv::waitKey(0);
    cv::imwrite("data/03_magnitude.png", G);

    cv::destroyAllWindows();

	return 0;
}