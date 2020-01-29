#include <QApplication>

#include "Game.h"

Game* game;

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    game = new Game(0);
    game->show();
    game->start();

    return a.exec();
}
