#include <cmath>
#include <iostream>
#include <opencv2/opencv.hpp>

int main(int argc, char *argv[])
{

	// load image

	cv::Mat img = cv::imread("data/line.png");

	if (img.empty())
	{
		std::cout << "ERROR::CV::Could not read image." << std::endl;
		return 1;
	}

	int rows = img.rows;
	int cols = img.cols;
	int channels = img.type();

	cv::imshow("img", img);
	cv::waitKey(0);

    // Destect lines' edges

    cv::Mat edges;

    cv::Canny(img, edges, 127, 255);

    std::vector<cv::Vec2f> lines;

    constexpr double pi = 3.14159265358979323846;

    cv::HoughLines(edges, lines, 1, pi / 180, 255);

    cv::Mat draw = cv::Mat(rows, cols, CV_8U, cv::Scalar(0));

    if( lines.size() != 0) 
    {
        for (int i = 0; i < lines.size(); i++)
        {
            double rho = lines[i][0];
            double theta = lines[i][1];
            double a = std::cos(theta);
            double b = std::sin(theta);
            double x0 = a * rho;
            double y0 = b * rho;
            cv::Point p1 = cv::Point(int(x0 + 1000*(-b)), int(y0 + 1000*(a)));
            cv::Point p2 = cv::Point(int(x0 - 1000*(-b)), int(y0 - 1000*(a)));

            cv::line(draw, p1, p2, cv::Scalar(255), 1, cv::LINE_AA);

        }
    }

    cv::imshow("hough_lines", draw);
    cv::waitKey(0);
    cv::imwrite("data/hough_lines.png", draw);

    cv::destroyAllWindows();

    return 0;
}