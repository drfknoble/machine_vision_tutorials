#include "mainwindow.h"
#include "./ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::init()
{
    emit sig_getCameras();
}

void MainWindow::slot_updateCameras(const QVector<int> &devices)
{
    qDebug() << "slot_updateCameras";

    for (int i : devices)
    {
        qDebug() << i;

        QString option;
        QTextStream stream(&option);

        stream << "Camera " << i;

        ui->comboBox->addItem(option);
    }

}

void MainWindow::slot_updateFrame()
{
    qDebug() << "slot_updateFrame";
}

void MainWindow::on_pushButton_clicked()
{
    qDebug() << "on_pushButton_clicked";

    int device {0};

    device = ui->comboBox->currentText().toInt();

    emit sig_openCamera(device);

}
