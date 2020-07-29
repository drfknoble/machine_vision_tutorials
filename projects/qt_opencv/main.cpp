#include "mainwindow.h"
#include "opencv_algorithm.h"

#include <QApplication>

#include <QDebug>
#include <QObject>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    MainWindow w;
    opencv_algorithm alg; // = new opencv_algorithm();

    bool con {false};

    // MainWindow signals

    con = QObject::connect(&w, SIGNAL(sig_getCameras()), &alg, SLOT(slot_getCameras()));
    qDebug() << con;

    con = QObject::connect(&w, SIGNAL(sig_getFrame()), &alg, SLOT(slot_getFrame()));
    qDebug() << con;

    // opencv_algorithm signals

    con = QObject::connect(&alg, SIGNAL(sig_updateCameras(const QVector<int>&)), &w, SLOT(slot_updateCameras(const QVector<int>&)));
    qDebug() << con;

    con = QObject::connect(&alg, SIGNAL(sig_updateFrame()), &w, SLOT(slot_updateFrame()));
    qDebug() << con;

    w.init();

    w.show();

    return a.exec();
}
