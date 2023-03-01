
# наш новый класс, который представляет графику и способ взаимодействия с пользователем
class ConsoleGameGui:
    # инициализация точно такая же, как с pygame, только теперь он нам не нужен
    def __init__(self, w, h, logic) -> None:
        self.main_w = w
        self.main_h = h
        self.logic = logic

    # тут будет цикл обработки сообщений и взаимодействия с пользователем
    def run(self):
        running = True
        while running:
            # сначала посылаем сообщение Event_Tick, чтобы была сгенерирована цель
            self.processEvent(GameEvent(GameEvent.Event_Tick, None))

            # отрисовываем то, что сейчас должно быть на доске
            self.draw()

            # запрашиваем команды у пользователя
            print('------------------')
            print('0. exit')
            print('1. hit target')
            cmd = int(input())

            # значение пустого события по умолчанию
            event = GameEvent(GameEvent.Event_None, None)
            # если команда 0 - идем на выход
            if cmd == 0:
                running = False
                continue
            # если команда 1 запрашиваем координаты
            if cmd == 1:
                x = int(input('input X: '))
                y = int(input('input Y: '))
                event = GameEvent(GameEvent.Event_Hit, Pos(x, y))

            # отрабатываем событие
            self.processEvent(event)

    # в отличие от варианта с pygame тут никакой логики нет, но мы все равно оставили этот метод, чтобы повторять ту же структуру класса
    def processEvent(self, event):
        self.logic.processEvent(event)

    # метод отображения содержимого доски
    def draw(self):
        # выводим текущий счет
        score = self.logic.getScore()
        print('------------------')
        print(f'Your score: {score}')

        # выводим текущие цели
        print('Aims:')
        marks = self.logic.getBoard()
        for index, mark in enumerate(marks):
            print(
                f'aim{index}[x = {mark.getPos().x},y={mark.getPos().y}, w = {mark.getWidth()}, h = {mark.getHeight()}]: {mark.getCost()}')


# --------------------------------------------
if __name__ == "__main__":
    width = 800
    height = 600
    gui = ConsoleGameGui(width, height, GameLogic(width, height))
    gui.run()