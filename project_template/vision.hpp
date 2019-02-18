#ifndef __VISION_HPP__
#define __VISION_HPP__

#include <QDebug>

#include <QImage>

#include <QObject>

#include <QPixmap>

#include <opencv2/opencv.hpp>

class vision : public QObject
{
	Q_OBJECT

public:
	vision();
	~vision();

public slots:

	void slot_runAlgorithm();

private:

signals:

	void sig_updateView(const QImage&);
	void sig_updateMessage(const QString&);
	
};


#endif // !__VISION_HPP__
