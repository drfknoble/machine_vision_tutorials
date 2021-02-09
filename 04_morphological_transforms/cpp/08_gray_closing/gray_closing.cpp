#include <iostream>
#include <opencv2/opencv.hpp>

#include "utils.hpp"

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

    // Convert image from BGR 2 grayscale

    cv::cvtColor(img, img, cv::COLOR_BGR2GRAY);

    // Apply salt and pepper noise to image

    cv::Mat noisy_img;

    add_salt_pepper_noise(img, &noisy_img);

    cv::imshow("noisy_img", noisy_img);
	cv::waitKey(0);
    cv::imwrite("data/noisy_img.png", noisy_img);

    // Erode image using different shapes

    std::vector<int> shapes {cv::MORPH_RECT, cv::MORPH_CROSS, cv::MORPH_ELLIPSE};
    std::vector<std::string> labels {"MORPH_RECT", "MORPH_CROSS", "MORPH_ELLIPSE"};

    for (int i = 0; i < shapes.size(); i++)
    {
        cv::Mat kernel = cv::getStructuringElement(shapes[i], cv::Size(5, 5));
        
        std::cout << labels[i] << std::endl;
        std::cout << kernel << std::endl;

        cv::Mat closed;

        cv::morphologyEx(img, closed, cv::MORPH_CLOSE, kernel);

        std::stringstream ss;
        
        ss << "closed + " << labels[i];

        cv::imshow(ss.str(), closed);
        cv::waitKey(0);
        
        ss = std::stringstream();

        ss << "data/closed_" << labels[i] << ".png";

        cv::imwrite(ss.str(), closed);        

    }

    cv::destroyAllWindows();

    return 0;
}