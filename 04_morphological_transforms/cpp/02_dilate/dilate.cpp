#include <iostream>
#include <opencv2/opencv.hpp>
#include <random>
#include <vector>

int main(int argc, char *argv[])
{

    // Create image

    int rows = 480;
    int cols = 640;

    cv::Mat img = cv::Mat(rows, cols, CV_8U, cv::Scalar(0));

    // Draw circles at centre

    cv::circle(img, cv::Point(320, 240), 150, cv::Scalar(255), 40);
    cv::circle(img, cv::Point(320, 240), 100, cv::Scalar(0), 40);

    // Generate random noise

    std::default_random_engine generator;
    std::uniform_int_distribution<int> row_distribution(1, rows - 1);
    std::uniform_int_distribution<int> col_distribution(1, cols - 1);

    auto row = std::bind(row_distribution, generator);
    auto col = std::bind(col_distribution, generator);

    std::vector<cv::Point> coordinates;

    for (int i = 0; i < 100; i++)
    {
        coordinates.push_back(cv::Point(col(), row()));
    }

    for (auto c : coordinates)
    {
        cv::circle(img, c, 2, cv::Scalar(255), -1);
    }

    cv::imshow("img", img);
    cv::waitKey(0);
    cv::imwrite("data/img.png", img);

    // Dilate image using different shapes

    std::vector<int> shapes {cv::MORPH_RECT, cv::MORPH_CROSS, cv::MORPH_ELLIPSE};
    std::vector<std::string> labels {"MORPH_RECT", "MORPH_CROSS", "MORPH_ELLIPSE"};

    for (int i = 0; i < shapes.size(); i++)
    {
        cv::Mat kernel = cv::getStructuringElement(shapes[i], cv::Size(20, 20));
        
        std::cout << labels[i] << std::endl;
        std::cout << kernel << std::endl;

        cv::Mat dilated;

        cv::erode(img, dilated, kernel);

        std::stringstream ss;
        
        ss << "dilated + " << labels[i];

        cv::imshow(ss.str(), dilated);
        cv::waitKey(0);
        
        ss = std::stringstream();

        ss << "data/dilated_" << labels[i] << ".png";

        cv::imwrite(ss.str(), dilated);        

    }

    cv::destroyAllWindows();

    return 0;
}