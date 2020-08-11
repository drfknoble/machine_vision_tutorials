#ifndef OPENCV_ALGORITHM_H
#define OPENCV_ALGORITHM_H

#include <opencv2/opencv.hpp>

#include <QDebug>
#include <QObject>
#include <QVector>

class opencv_algorithm : public QObject
{
    Q_OBJECT
public:
    explicit opencv_algorithm(QObject *parent = nullptr);

signals:
    void sig_updateCameras(const QVector<int> &devices);
    void sig_cameraOpened();
    void sig_updateFrame();

public slots:
    void slot_getCameras();
    void slot_openCamera(const int &device);
    void slot_getFrame();

private:
    cv::VideoCapture *camera;

};

#endif // OPENCV_ALGORITHM_H
