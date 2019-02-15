#include "gui.hpp"

gui::gui(QWidget *parent)
	: QMainWindow(parent)
{

	this->setGeometry(QRect(100, 100, 640, 560));
	this->setWindowTitle("Qt GUI");

	graphicsPixmap = new QGraphicsPixmapItem();

	graphicsScene = new QGraphicsScene(this);
	graphicsScene->addItem(graphicsPixmap);
	
	graphicsView = new QGraphicsView(this);
	graphicsView->setGeometry(QRect(0, 0, 640, 480));
	graphicsView->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
	graphicsView->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
	graphicsView->setScene(graphicsScene);

	debugLine = new QLineEdit(this);
	debugLine->setGeometry(10, 500, 620, 20);
	debugLine->setText("");

	quitButton = new QPushButton(this);
	quitButton->setGeometry(10, 530, 75, 23);
	quitButton->setText("Quit");
	
	QObject::connect(quitButton, SIGNAL(clicked()), this, SLOT(slot_quit()));

	return;
	
}

void gui::slot_updateView(const QImage &image) {

	QPixmap pixmap = QPixmap::fromImage(image);

	graphicsPixmap->setPixmap(pixmap);

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