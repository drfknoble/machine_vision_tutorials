#include "gui.hpp"

gui::gui(QWidget *parent)
	: QMainWindow(parent)
{

	this->setGeometry(QRect(100, 100, 640, 560));
	this->setWindowTitle("Qt OpenCV");

	graphicsPixmap = new QGraphicsPixmapItem();

	graphicsScene = new QGraphicsScene(this);
	graphicsScene->addItem(graphicsPixmap);
	
	graphicsView = new QGraphicsView(this);
	graphicsView->setScene(graphicsScene);
	graphicsView->setGeometry(QRect(0, 0, 640, 480));

	debugLine = new QLineEdit(this);
	debugLine->setText("");
	debugLine->setGeometry(10, 500, 640, 20);

	quitButton = new QPushButton(this);
	quitButton->setText("Quit");
	quitButton->setGeometry(10, 530, 75, 23);
	
	QObject::connect(quitButton, SIGNAL(clicked()), this, SLOT(slot_quit()));

	return;
	
}

void gui::slot_updateView(const QImage &image) {

	QPixmap pixmap = QPixmap::fromImage(image);

	graphicsPixmap->setPixmap(pixmap);

	emit sig_getFrame();

	return;
}

void gui::slot_updateMessage(const QString &message) {

	debugLine->setText(message);

	emit sig_messageUpdated();

	return;
}

void gui::slot_quit() {

	emit sig_quit();

	return;
}