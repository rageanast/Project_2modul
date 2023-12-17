from tkinter import *

window = Tk()
window.title('Химический калькулятор')
window.geometry('900x400+100+100')


def input_into_entry(symbol): # Новые символы пишутся не слева, а справа
    """returns 'abcd' instead of 'dcba'"""
    entry.insert(END, symbol)


def clear(): # Стирание всей строки
    """returns '' """
    entry.delete(0, END)


def count_result(): # Вводится 2 элмента, выводится сумма и ответ
    """returns A + B (after reaction)

    :param A: element_1
    :type A: str
    :param B: elemet_2
    :type B: str
    :returns: A sum B
    :rtype: str
    :raises '': if A+B not reaction

    """
    equation = entry.get()
    result = ''





    clear()
    entry.insert(0, result)


entry = Entry(window, width=35, font=('', 30))
entry.place(x=100, y=50)

btn1 = Button(window, bg = 'white', fg = 'red', text = '1',
              command = lambda: input_into_entry('1'))
btn1.place(x = 100, y = 100, width = 50, height = 50)
btn2 = Button(window, bg = 'white', fg = 'red', text = '2',
              command = lambda: input_into_entry('2'))
btn2.place(x = 150, y = 100, width = 50, height = 50)
btn3 = Button(window, bg = 'white', fg = 'red', text = '3',
              command = lambda: input_into_entry('3'))
btn3.place(x = 200, y = 100, width = 50, height = 50)
btn4 = Button(window, bg = 'white', fg = 'red', text = '4',
              command = lambda: input_into_entry('4'))
btn4.place(x = 250, y = 100, width = 50, height = 50)
btn5 = Button(window, bg = 'white', fg = 'red', text = '5',
              command = lambda: input_into_entry('5'))
btn5.place(x = 300, y = 100, width = 50, height = 50)
btn6 = Button(window, bg = 'white', fg = 'red', text = '6',
              command = lambda: input_into_entry('6'))
btn6.place(x = 350, y = 100, width = 50, height = 50)
btn7 = Button(window, bg = 'white', fg = 'red', text = '7',
              command = lambda: input_into_entry('7'))
btn7.place(x = 400, y = 100, width = 50, height = 50)
btn8 = Button(window, bg = 'white', fg = 'red', text = '8',
              command = lambda: input_into_entry('8'))
btn8.place(x = 450, y = 100, width = 50, height = 50)
btn9 = Button(window, bg = 'white', fg = 'red', text = '9',
              command = lambda: input_into_entry('9'))
btn9.place(x = 500, y = 100, width = 50, height = 50)
btn10 = Button(window, bg = 'white', fg = 'red', text = 'A',
               command = lambda: input_into_entry('A'))
btn10.place(x = 100, y = 150, width = 50, height = 50)
btn11 = Button(window, bg = 'white', fg = 'red', text = 'B',
               command = lambda: input_into_entry('B'))
btn11.place(x = 150, y = 150, width = 50, height = 50)
btn12 = Button(window, bg = 'white', fg = 'red', text = 'C',
               command = lambda: input_into_entry('C'))
btn12.place(x = 200, y = 150, width = 50, height = 50)
btn13 = Button(window, bg = 'white', fg = 'red', text = 'D',
               command = lambda: input_into_entry('D'))
btn13.place(x = 250, y = 150, width = 50, height = 50)
btn14 = Button(window, bg = 'white', fg = 'red', text = 'E',
               command = lambda: input_into_entry('E'))
btn14.place(x = 300, y = 150, width = 50, height = 50)
btn15 = Button(window, bg = 'white', fg = 'red', text = 'F',
               command = lambda: input_into_entry('F'))
btn15.place(x = 350, y = 150, width = 50, height = 50)
btn16 = Button(window, bg = 'white', fg = 'red', text = 'G',
               command = lambda: input_into_entry('G'))
btn16.place(x = 400, y = 150, width = 50, height = 50)
btn17 = Button(window, bg = 'white', fg = 'red', text = 'H',
               command = lambda: input_into_entry('H'))
btn17.place(x = 450, y = 150, width = 50, height = 50)
btn18 = Button(window, bg = 'white', fg = 'red', text = 'I',
               command = lambda: input_into_entry('I'))
btn18.place(x = 500, y = 150, width = 50, height = 50)
btn19 = Button(window, bg = 'white', fg = 'red', text = 'J',
               command = lambda: input_into_entry('G'))
btn19.place(x = 550, y = 150, width = 50, height = 50)
btn20 = Button(window, bg = 'white', fg = 'red', text = 'K',
               command = lambda: input_into_entry('K'))
btn20.place(x = 600, y = 150, width = 50, height = 50)
btn21 = Button(window, bg = 'white', fg = 'red', text = 'L',
               command = lambda: input_into_entry('L'))
btn21.place(x = 650, y = 150, width = 50, height = 50)
btn22 = Button(window, bg = 'white', fg = 'red', text = 'M',
               command = lambda: input_into_entry('M'))
btn22.place(x = 700, y = 150, width = 50, height = 50)
btn23 = Button(window, bg = 'white', fg = 'red', text = 'N',
               command = lambda: input_into_entry('N'))
btn23.place(x = 100, y = 200, width = 50, height = 50)
btn24 = Button(window, bg = 'white', fg = 'red', text = 'O',
               command = lambda: input_into_entry('O'))
btn24.place(x = 150, y = 200, width = 50, height = 50)
btn25 = Button(window, bg = 'white', fg = 'red', text = 'P',
               command = lambda: input_into_entry('P'))
btn25.place(x = 200, y = 200, width = 50, height = 50)
btn26 = Button(window, bg = 'white', fg = 'red', text = 'Q',
               command = lambda: input_into_entry('Q'))
btn26.place(x = 250, y = 200, width = 50, height = 50)
btn27 = Button(window, bg = 'white', fg = 'red', text = 'R',
               command = lambda: input_into_entry('R'))
btn27.place(x = 300, y = 200, width = 50, height = 50)
btn28 = Button(window, bg = 'white', fg = 'red', text = 'S',
               command = lambda: input_into_entry('S'))
btn28.place(x = 350, y = 200, width = 50, height = 50)
btn29 = Button(window, bg = 'white', fg = 'red', text = 'T',
               command = lambda: input_into_entry('T'))
btn29.place(x = 400, y = 200, width = 50, height = 50)
btn30 = Button(window, bg = 'white', fg = 'red', text = 'U',
               command = lambda: input_into_entry('U'))
btn30.place(x = 450, y = 200, width = 50, height = 50)
btn31 = Button(window, bg = 'white', fg = 'red', text = 'V',
               command = lambda: input_into_entry('V'))
btn31.place(x = 500, y = 200, width = 50, height = 50)
btn32 = Button(window, bg = 'white', fg = 'red', text = 'W',
               command = lambda: input_into_entry('W'))
btn32.place(x = 550, y = 200, width = 50, height = 50)
btn33 = Button(window, bg = 'white', fg = 'red', text = 'X',
               command = lambda: input_into_entry('X'))
btn33.place(x = 600, y = 200, width = 50, height = 50)
btn34 = Button(window, bg = 'white', fg = 'red', text = 'Y',
               command = lambda: input_into_entry('Y'))
btn34.place(x = 650, y = 200, width = 50, height = 50)
btn35 = Button(window, bg = 'white', fg = 'red', text = 'Z',
               command = lambda: input_into_entry('Z'))
btn35.place(x = 700, y = 200, width = 50, height = 50)
btn36 = Button(window, bg = 'white', fg = 'red', text = 'a',
               command = lambda: input_into_entry('a'))
btn36.place(x = 100, y = 250, width = 50, height = 50)
btn37 = Button(window, bg = 'white', fg = 'red', text = 'b',
               command = lambda: input_into_entry('b'))
btn37.place(x = 150, y = 250, width = 50, height = 50)
btn38 = Button(window, bg = 'white', fg = 'red', text = 'c',
               command = lambda: input_into_entry('c'))
btn38.place(x = 200, y = 250, width = 50, height = 50)
btn39 = Button(window, bg = 'white', fg = 'red', text = 'd',
               command = lambda: input_into_entry('d'))
btn39.place(x = 250, y= 250, width = 50, height = 50)
btn40 = Button(window, bg = 'white', fg = 'red', text = 'e',
               command = lambda: input_into_entry('e'))
btn40.place(x = 300, y = 250, width = 50, height = 50)
btn41 = Button(window, bg = 'white', fg = 'red', text = 'f',
               command = lambda: input_into_entry('f'))
btn41.place(x = 350, y = 250, width = 50, height = 50)
btn42 = Button(window, bg = 'white', fg = 'red', text = 'g',
               command = lambda: input_into_entry('g'))
btn42.place(x = 400, y = 250, width = 50, height = 50)
btn43 = Button(window, bg = 'white', fg = 'red', text = 'h',
               command = lambda: input_into_entry('h'))
btn43.place(x = 450, y = 250, width = 50, height = 50)
btn44 = Button(window, bg = 'white', fg = 'red', text = 'i',
               command = lambda: input_into_entry('i'))
btn44.place(x = 500, y = 250, width = 50, height = 50)
btn45 = Button(window, bg = 'white', fg = 'red', text = 'j',
               command = lambda: input_into_entry('j'))
btn45.place(x = 550, y = 250, width = 50, height = 50)
btn46 = Button(window, bg = 'white', fg = 'red', text = 'k',
               command = lambda: input_into_entry('k'))
btn46.place(x = 600, y = 250, width = 50, height = 50)
btn47 = Button(window, bg = 'white', fg = 'red', text = 'l',
               command = lambda: input_into_entry('l'))
btn47.place(x = 650, y = 250, width = 50, height = 50)
btn48 = Button(window, bg = 'white', fg = 'red', text = 'm',
               command = lambda: input_into_entry('m'))
btn48.place(x = 700, y = 250, width = 50, height = 50)
btn49 = Button(window, bg = 'white', fg = 'red', text = 'n',
               command = lambda: input_into_entry('n'))
btn49.place(x = 100, y = 300, width = 50, height = 50)
btn50 = Button(window, bg = 'white', fg = 'red', text = 'o',
               command = lambda: input_into_entry('o'))
btn50.place(x = 150, y = 300, width = 50, height = 50)
btn51 = Button(window, bg = 'white', fg = 'red', text = 'p',
               command = lambda: input_into_entry('p'))
btn51.place(x = 200, y = 300, width = 50, height = 50)
btn52 = Button(window, bg = 'white', fg = 'red', text = 'q',
               command = lambda: input_into_entry('q'))
btn52.place(x = 250, y = 300, width = 50, height = 50)
btn53 = Button(window, bg = 'white', fg = 'red', text = 'r',
               command = lambda: input_into_entry('r'))
btn53.place(x = 300, y = 300, width = 50, height = 50)
btn54 = Button(window, bg = 'white', fg = 'red', text = 's',
               command = lambda: input_into_entry('s'))
btn54.place(x = 350, y = 300, width = 50, height = 50)
btn55 = Button(window, bg = 'white', fg = 'red', text = 't',
               command = lambda: input_into_entry('t'))
btn55.place(x = 400, y = 300, width = 50, height = 50)
btn56 = Button(window, bg = 'white', fg = 'red', text = 'u',
               command = lambda: input_into_entry('u'))
btn56.place(x = 450, y = 300, width = 50, height = 50)
btn57 = Button(window, bg = 'white', fg = 'red', text = 'v',
               command = lambda: input_into_entry('v'))
btn57.place(x = 500, y = 300, width = 50, height = 50)
btn58 = Button(window, bg = 'white', fg = 'red', text = 'w',
               command = lambda: input_into_entry('w'))
btn58.place(x=550, y=300, width=50, height=50)
btn59 = Button(window, bg = 'white', fg = 'red', text = 'x',
               command = lambda: input_into_entry('x'))
btn59.place(x = 600, y = 300, width = 50, height = 50)
btn60 = Button(window, bg = 'white', fg = 'red', text = 'y',
               command = lambda: input_into_entry('y'))
btn60.place(x = 650, y = 300, width = 50, height = 50)
btn61 = Button(window, bg = 'white', fg = 'red', text = 'z',
               command = lambda: input_into_entry('z'))
btn61.place(x = 700, y = 300, width = 50, height=50)
btn62 = Button(window, bg = 'white', fg = 'red', text = '+',
               command = lambda: input_into_entry('+'))
btn62.place(x = 600, y = 100, width = 50, height = 50)
btn63 = Button(window, bg = 'white', fg = 'red', text = ' ',
               command = lambda: input_into_entry(' '))
btn63.place(x = 650, y = 100, width = 50, height = 50)
btn64 = Button(window, bg = 'white', fg = 'red', text = 'CE',
               command = clear)
btn64.place(x = 700, y = 100, width = 50, height = 50)
btn65 = Button(window, bg = 'white', fg = 'red', text = '-->',
               command = count_result)
btn65.place(x = 550, y = 100, width = 50, height = 50)
btn66 = Button(window, bg = 'white', fg = 'red', text = '(',
              command = lambda: input_into_entry('('))
btn66.place(x = 650, y = 350, width = 50, height = 50)
btn67 = Button(window, bg = 'white', fg = 'red', text = ')',
              command = lambda: input_into_entry(')'))
btn67.place(x = 700, y = 350, width = 50, height = 50)



window.mainloop()
