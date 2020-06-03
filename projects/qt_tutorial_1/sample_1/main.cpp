#include "main.hpp"

int main(int argc, char *argv[])
{
	QApplication a(argc, argv);

	gui w;

	QObject::connect(&w, SIGNAL(sig_quit()), &a, SLOT(quit()));

	w.show();

	return a.exec();
}
