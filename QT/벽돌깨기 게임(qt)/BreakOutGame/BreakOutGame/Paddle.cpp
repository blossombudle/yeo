#include "Paddle.h"
#include <QBrush>

Paddle::Paddle(QGraphicsItem *parent) {
    // draw rect
    setRect(0, 0, 85, 18);
    QBrush brush;
    brush.setStyle(Qt::SolidPattern);
    brush.setColor(Qt::gray);
    setBrush(brush);
}

double Paddle::getCenterX() {
    return x()+rect().width()/2;
}

void Paddle::mouseMoveEvent(QGraphicsSceneMouseEvent *event) {
    // follow mouse's x pos
    double mouseX = mapToScene(event->pos()).x();
    setPos(mouseX,y());
}
