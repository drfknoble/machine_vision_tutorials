#include <filesystem>
#include <iostream>

#include "main.hpp"

namespace fs = std::experimental::filesystem;

int main(int argc, char* argv[]) {

	fs::path executablePath{ fs::path(argv[0]) };

	fs::path dataPath{ fs::path("/data/image.png") };

	fs::path inputFile{ executablePath.parent_path().append(dataPath) };

	std::cout << inputFile.string() << std::endl;

	cv::Mat image = cv::imread(inputFile.string(), cv::IMREAD_COLOR);

	if (image.empty()) {

		std::cout << "Error: 'image' is empty" << std::endl;

		return 1;
	}

	cv::imshow("image", image);

	cv::waitKey(0);

	cv::destroyAllWindows();

    return 0;
}