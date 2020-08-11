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

    if (camera->isOpened())
    {
        camera->release();
    }

    camera->open(device);

    emit sig_cameraOpened();

    slot_getFrame();

}

void opencv_algorithm::slot_getFrame()
{
    qDebug() << "slot_getFrame";

    cv::Mat frame {};

    bool ret = camera->read(frame);

    qDebug() << ret;

    if (ret)
    {
        cv::imshow("frame", frame);
        cv::waitKey(1);

        emit sig_updateFrame();
    }
}
