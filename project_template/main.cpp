#include "main.hpp"

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);

	gui w;

	QThread *visionThread = new QThread();

	vision *visionTasks = new vision();

	visionTasks->moveToThread(visionThread);

	QObject::connect(visionThread, SIGNAL(started()), visionTasks, SLOT(slot_runAlgorithm()));

	QObject::connect(visionTasks, SIGNAL(sig_updateView(const QImage&)), &w, SLOT(slot_updateView(const QImage&)));

	QObject::connect(visionTasks, SIGNAL(sig_updateMessage(const QString&)), &w, SLOT(slot_updateMessage(const QString&)));

	QObject::connect(&w, SIGNAL(sig_quit()), &a, SLOT(quit()));

	visionThread->start();

	w.show();

	return a.exec();
}
