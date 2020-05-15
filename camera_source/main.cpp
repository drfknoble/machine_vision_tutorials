#include "main.hpp"

int main(int argc, char* argv[])
{
    
    cv::VideoCapture camera(0);

    if(!camera.isOpened())
    {
        return 1;
    }

    while(true)
    {

        cv::Mat frame;

        camera >> frame;

        cv::imshow("frame", frame);

        int i = cv::waitKey(30);

        if(i == 27)
        {
            break;
        }
    }

    cv::destroyAllWindows();

    camera.release();

    return 0;
}