
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QRadioButton, \
    QGroupBox
from random import choice, randint, shuffle

questions = [
                {'question':'Какой народности не существует?', 
                'answer1':'Буряты',
                'answer2':'Ненцы',
                'answer3':'Нанайцы',
                'answer4':'Смурфы',
                'correct':'Смурфы'
                },
                {'question':'Кaк обозначается медь?', 
                'answer1':'Cu',
                'answer2':'Au',
                'answer3':'Ag',
                'answer4':'O',
                'correct':'Cu'
                },
                {'question':'Кaк обозначается железо?', 
                'answer1':'Fe',
                'answer2':'e',
                'answer3':'F',
                'answer4':'O',
                'correct':'Fe'
                },
                {'question':'Кто ты?', 
                'answer1':'человек',
                'answer2':'железо',
                'answer3':'Cu',
                'answer4':'негритян',
                'correct':'человек'
                },
                {'question':'Какие самые популярные языки в Rust?', 
                'answer1':'русский',
                'answer2':'англиский',
                'answer3':'китайский',
                'answer4':'рсский и англиский',
                'correct':'рсский и англиский'
                },
                {'question':'Как обзначаетс кислород в химии', 
                'answer1':'русский',
                'answer2':'О',
                'answer3':'К',
                'answer4':'Fe',
                'correct':'О'
                },
                {'question':'В школу хочешь?', 
                'answer1':'нет',
                'answer2':'да',
                'answer3':'конечно',
                'answer4':'конечно нет',
                'correct':'конечно нет'
                },
                {'question':'Лучший язык прогромирования?(моё мнение)', 
                'answer1':'русский',
                'answer2':'англиский',
                'answer3':'пайтон',
                'answer4':'джава',
                'correct':'пайтон'
                },
                {'question':'где програмируешь?', 
                'answer1':'ПК',
                'answer2':'Консоль',
                'answer3':'Пайтон',
                'answer4':'Ноут',
                'correct':'Консоль'
                },
                {'question':'играешь в Rust?', 
                'answer1':'да',
                'answer2':'да',
                'answer3':'да',
                'answer4':'да',
                'correct':'да'
                }
]

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.setFixedSize(500, 500)
window.total = 1
window.score = 0

question = QLabel('?')
group_answers = QGroupBox('Выберите ответ')
# Create radio buttons for answers
ans_1 = QRadioButton('')
ans_2 = QRadioButton('')
ans_3 = QRadioButton('')
ans_4 = QRadioButton('')
# Place radio buttons in group box
ans_layout1 = QVBoxLayout()
ans_layout1.setSpacing(20)
ans_layout1.addWidget(ans_1, alignment=Qt.AlignCenter)
ans_layout1.addWidget(ans_2, alignment=Qt.AlignCenter)

ans_layout2 = QVBoxLayout()
ans_layout2.setSpacing(20)
ans_layout2.addWidget(ans_3, alignment=Qt.AlignCenter)
ans_layout2.addWidget(ans_4, alignment=Qt.AlignCenter)
ans_layout = QHBoxLayout()
ans_layout.addLayout(ans_layout1)
ans_layout.addLayout(ans_layout2)
group_answers.setLayout(ans_layout)


def show_result():
    if button.text() == 'Ответить':
        for ans in (ans_1, ans_2, ans_3, ans_4):
            if ans.isChecked():
                button.setText('Следующий вопрос')
                answer_group.show()
                group_answers.hide()
                if ans.text() == window.correct:
                    is_correct.setStyleSheet('color: #339900;')
                    is_correct.setText('Правильно!')
                    window.score += 1
                    print('Статистика:\n - Всего вопросов:',window.total )
                    print('Всего правельных ответов:', window.score)
                    print('Рейтинг', window.score / window.total * 100, '%')
                else:
                    is_correct.setStyleSheet('color: #FF0000;')
                    is_correct.setText('Неправильно... :-(')
                    print('Рейтинг', window.score/window.total * 100, '%')
    else:
        window.total += 1
        set_question()
        answer_group.hide()
        group_answers.show()
        button.setText('Ответить')


button = QPushButton('Ответить')
button.clicked.connect(show_result)

answer_group = QGroupBox('Правильный ответ:')
is_correct = QLabel('Правильно')
answer_line = QVBoxLayout()
answer_line.addWidget(is_correct, alignment=Qt.AlignCenter)
answer_group.setLayout(answer_line)
answer_group.hide()

line = QVBoxLayout()
line.addWidget(question, alignment=Qt.AlignCenter)
line.addWidget(group_answers, alignment=Qt.AlignCenter)
line.addWidget(answer_group, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
line.setSpacing(20)

window.setLayout(line)
window.show()

answers = [ans_1, ans_2, ans_3, ans_4]

def set_question():
    shuffle(answers)
    text_question, a1, a2, a3, a4, correct = choice(questions).values()
    question.setText(text_question)
    answers[0].setText(a1)
    answers[1].setText(a2)
    answers[2].setText(a3)
    answers[3].setText(a4)
    window.correct = correct


def keyPressEvent(self, e):
# отработать символ внутри поля ввода
    Q = e.key()
    super().keyPressEvent(e)
    print("QLineEdit:",Q)


set_question()

app.exec_()