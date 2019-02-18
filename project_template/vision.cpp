#include "vision.hpp"

vision::vision()
{

	
}

vision::~vision()
{

	cv::destroyAllWindows();

}

void vision::slot_runAlgorithm() {

	cv::Mat blank = 255 * cv::Mat::ones(cv::Size(640, 480), CV_8UC3);

	QImage *qBlank = new QImage(static_cast<uchar*>(blank.data), blank.cols, blank.rows, blank.step, QImage::Format_RGB888);

	emit sig_updateView(qBlank->rgbSwapped());

	return;
}
