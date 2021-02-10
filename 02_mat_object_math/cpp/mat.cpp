#include <opencv2/opencv.hpp>

int main(int argc, char* argv[])
{

    cv::Mat img = cv::Mat(480, 640, CV_8U, cv::Scalar(0));

    cv::rectangle(img, cv::Rect(cv::Point(100, 100), cv::Point(400, 400)), cv::Scalar(255), -1);

    cv::imshow("img", img);
    cv::waitKey(0);

    cv::Mat background_img_1 = cv::Mat(480, 640, CV_8U, cv::Scalar(0));
    cv::Mat background_img_2 = cv::Mat(480, 640, CV_8U, cv::Scalar(0));

    cv::rectangle(background_img_1, cv::Rect(cv::Point(150, 150), cv::Point(350, 350)), cv::Scalar(255), -1);
    cv::rectangle(background_img_2, cv::Rect(cv::Point(200, 200), cv::Point(450, 450)), cv::Scalar(255), -1);

    cv::Mat background_img = background_img_1 + background_img_2;

    cv::imshow("background_img", background_img);
    cv::waitKey(0);

    cv::Mat sub_img = img - background_img;

    cv::imshow("sub_img", sub_img);
    cv::waitKey(0);

    cv::destroyAllWindows();    

    return 0;
}