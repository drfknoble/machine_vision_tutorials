#ifndef OPENCV_ALGORITHM_H
#define OPENCV_ALGORITHM_H

#include <QObject>

class opencv_algorithm : public QObject
{
    Q_OBJECT
public:
    explicit opencv_algorithm(QObject *parent = nullptr);

signals:

};

#endif // OPENCV_ALGORITHM_H
