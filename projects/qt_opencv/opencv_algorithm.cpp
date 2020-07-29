#include "opencv_algorithm.h"

opencv_algorithm::opencv_algorithm(QObject *parent) : QObject(parent)
{
    qDebug() << "opencv_algorithm";

    camera = new cv::VideoCapture();
}

void opencv_algorithm::slot_getCameras()
{
    qDebug() << "slot_getCameras";

    QVector<int> devices {};

    for(int i {0}; ;i++)
    {
        if(camera->open(i))
        {
            qDebug() << i;

            devices.push_back(i);

            camera->release();
        }
        else
        {
            break;
        }
    }

    emit sig_updateCameras(devices);
}

void opencv_algorithm::slot_openCamera(const int &device)
{
    qDebug() << "slot_openCamera";

    camera->open(device);

}

void opencv_algorithm::slot_getFrame()
{
    qDebug() << "slot_getFrame";

    emit sig_updateFrame();
}
