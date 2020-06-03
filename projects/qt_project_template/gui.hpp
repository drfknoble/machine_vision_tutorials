#ifndef __GUI_HPP__
#define __GUI_HPP__

#include <QtWidgets/QMainWindow>

#include <QGraphicsPixmapItem>
#include <QGraphicsScene>
#include <QGraphicsView>
#include <QLineEdit>
#include <QPushButton>

class gui : public QMainWindow
{
	Q_OBJECT

public:
	gui(QWidget *parent = Q_NULLPTR);

private:

	QGraphicsPixmapItem *graphicsPixmap;
	QGraphicsScene *graphicsScene;
	QGraphicsView *graphicsView;

	QLineEdit *debugLine;

	QPushButton *quitButton;
	
public slots:

	void slot_updateView(const QImage&);

	void slot_updateMessage(const QString&);

private slots:

	void slot_quit();

signals:

	void sig_getFrame();

	void sig_messageUpdated();

	void sig_quit();

};


#endif // !__GUI_HPP__