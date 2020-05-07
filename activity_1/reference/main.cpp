#include "main.hpp"

int main(int argc, char* argv[])
{

    try
    {

    // Get executable path

    std::filesystem::path executable_path = std::filesystem::path(argv[0]).parent_path();

    std::cout << "Parent path:" << std::endl <<  executable_path.string() << std::endl;

    // Check if a file exists

    std::filesystem::path input_file = executable_path / "data/input_image.png";

    std::cout << "Input file:" << std::endl <<  input_file.string() << std::endl;

    if(!std::filesystem::exists(input_file))
    {
        return 1;
    } 

    // Read an image

    cv::Mat image = cv::imread(input_file.string(), cv::IMREAD_COLOR);

    // Check if image has been read

    if (image.empty())
    {
        return 2;
    }

    // Display an image

    cv::imshow("image", image);
    cv::waitKey(1);

    // Get user input

    while(true)
    {
        char c = cv::waitKey(0);

        if (c == 27)
        {
            break;
        }
    }

    // Close a window

    cv::destroyWindow("image");
       
    // Write an image

    std::filesystem::path output_file = executable_path / "data/output_image.png";

    std::cout << "Output file:" << std::endl <<  output_file.string() << std::endl;

    cv::imwrite(output_file.string(), image);

    return 0;

    }
    catch(std::exception &e)
    {

        std::cout << e.what() << std::endl;

    }
}