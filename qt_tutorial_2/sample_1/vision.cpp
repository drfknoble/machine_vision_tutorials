#include "vision.hpp"

vision::vision()
{


}

vision::~vision()
{


}

void vision::slot_runAlgorithm() {

	fs::path inputImagePath = fs::current_path().append("data/outputImage.png");
	fs::path imageMaskPath = fs::current_path().append("data/imageMask.png");

	cv::Mat inputImage = cv::imread(inputImagePath.string(), cv::IMREAD_GRAYSCALE);
	
	if (inputImage.empty()) {
		emit sig_updateMessage(QString("Error: Could not open 'outputImage.png'"));
	}
	
	cv::Mat imageMask = cv::imread(imageMaskPath.string(), cv::IMREAD_GRAYSCALE);

	if (inputImage.empty()) {
		emit sig_updateMessage(QString("Error: Could not open 'imageMask.png'"));
	}

	int erosionSize = 10;

	cv::Mat element = cv::getStructuringElement(cv::MORPH_ELLIPSE,
		cv::Size(2 * erosionSize + 1, 2 * erosionSize + 1),
		cv::Point(erosionSize, erosionSize));

	cv::erode(inputImage, inputImage, element);

	cv::Mat intersection;

	inputImage.copyTo(intersection, imageMask);

	double percentage = (static_cast<double>(cv::countNonZero(intersection)) / static_cast<double>(cv::countNonZero(imageMask))) * 100;

	emit sig_updateMessage(QString::number(percentage));

	cv::resize(intersection, intersection, cv::Size(640, 480));

	QImage *qIntersection = new QImage(static_cast<uchar*>(intersection.data), intersection.cols, intersection.rows, intersection.step, QImage::Format_Grayscale8);

	emit sig_updateView(qIntersection->rgbSwapped().copy());
		   	   
	return;
}
