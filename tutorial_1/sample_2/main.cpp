#include <filesystem>
#include <iostream>

#include "main.hpp"

namespace fs = std::experimental::filesystem;

int main(int argc, char* argv[]) {

    cv::Mat image = cv::Mat(cv::Size(640, 480), CV_8UC3, cv::Scalar(255, 0, 0));

    cv::imshow("image", image);

    cv::waitKey(0);

    fs::path executablePath{ fs::path(argv[0]) };

	fs::path dataPath{ fs::path("/data") };

	fs::path outputPath{ executablePath.parent_path().append(dataPath) };

    if(!fs::is_directory(outputPath)) {

        fs::create_directory(outputPath);

    }

    fs::path outputFile {outputPath.append(fs::path("/image.png"))};

	std::cout << outputFile.string() << std::endl;

    cv::imwrite(outputFile.string(), image);
    
    return 0;
}