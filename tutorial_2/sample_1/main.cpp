#include <filesystem>
#include <iostream>

#include "main.hpp"

namespace fs = std::experimental::filesystem;

int main(int argc, char* argv[]) {

    fs::path executablePath{ fs::path(argv[0]) };

    fs::path dataPath{ fs::path("/data/image.jpg") };

    fs::path inputFile { executablePath.parent_path().append(dataPath) };

    std::cout << inputFile.string() << std::endl;

    cv::Mat image = cv::imread(inputFile.string(), cv::IMREAD_COLOR);

    if(image.empty()) {

        std::cout << "Error: `image` is empty" << std::endl;

        return 1;

    }

	cv::Vec3b intensity = image.at<cv::Vec3b>(cv::Point(100, 100));

	uchar blue = intensity.val[0];
	uchar green = intensity.val[1];
	uchar red = intensity.val[2];

	std::cout << intensity << ", " << static_cast<int>(blue) << ", " << static_cast<int>(green) << ", " << static_cast<int>(red) << std::endl;
	
	cv::imshow("image", image);

	cv::waitKey(0);

	image.at<cv::Vec3b>(cv::Point(100, 100)) = cv::Vec3b(100, 0, 0);

	intensity = image.at<cv::Vec3b>(cv::Point(100, 100));

	blue = intensity.val[0];
	green = intensity.val[1];
	red = intensity.val[2];

	std::cout << intensity << ", " << static_cast<int>(blue) << ", " << static_cast<int>(green) << ", " << static_cast<int>(red) << std::endl;

	cv::imshow("image", image);

	cv::waitKey(0);

    cv::destroyAllWindows();

    return 0;
}