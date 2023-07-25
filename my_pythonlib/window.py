import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget,QComboBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QPalette, QColor, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSocketNotifier

class janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("tecnology selector")# nome da janela
        desktop = QApplication.desktop()# vai buscar o widget do dektop
        screen_geometry = desktop.screenGeometry() #associa as dimensoes do desktop na variavel
        self.setGeometry(screen_geometry)#inicializa a janela com as dimensoes
        
        palette = self.palette()#cria uma classe filho palette
        background_color = palette.color(QPalette.Window)#vai buscar a cor de fundo da janela

       
        
        pixmap = QPixmap("/home/vasco/Desktop/my_pythonlib/IST_-_Instituto_Superior_Tecnico.png")#carrega a imagem na variavel pixmap
        smaller_pixmap = pixmap.scaled(300, 100, Qt.KeepAspectRatio)#reduz o aspeto da imagem
        image = QLabel(self) #cria uma classe chamada atraves de qlabel em funcao da classe pai Qlabel
        image.setPixmap(smaller_pixmap )#faz com que a imagem seja displaeyed na na classe imagem criada
        image.setAlignment(Qt.AlignCenter)#centraliza a imagem
        image.setGeometry(0, 0, 350, 100) #geometria e posiçao (x,y,x_tamanho,t_tamanho)

        font = QFont()#cria uma class do tamanho
        font.setPointSize(40)#da se set para um tamanho de 40


        text_label = QLabel(self)#ccria uma classe textlabel
        text_label.setText("Tecnologias")#texto
        text_label.setFont(font)#tamano da letra
        text_label.setStyleSheet("QLabel { background-color: %s; padding: 10px; }" % background_color.name())  # Set the background color using the retrieved color
        text_label.setAlignment(Qt.AlignCenter)
        text_label.setGeometry(800, 200, 320, 100)

        self.button1 = QPushButton("sky130A", self)#definicao da classe butao em funcao da classe pai QPUshbutton
        self.button2 = QPushButton("sky130B", self)
        self.button3 = QPushButton("gf180mcuA", self)
        self.button4 = QPushButton("gf180mcuB", self)
        self.button5 = QPushButton("gf180mcuC", self)
        self.button6 = QPushButton("exit",self)

        self.button7 = QPushButton("continuar",self)

        self.button1.setFixedSize(150, 50)
        self.button2.setFixedSize(150, 50)#defenicao da posicao
        self.button3.setFixedSize(150, 50)
        self.button4.setFixedSize(150, 50)
        self.button5.setFixedSize(150, 50)
        self.button6.setFixedSize(300, 75)

        self.button7.setFixedSize(200,75)


        self.button1.setGeometry(600, 500, 150, 50)
        self.button2.setGeometry(750, 500, 150, 50)#definicao da posicao, tamanho e 1960*1000
        self.button3.setGeometry(900, 500, 150, 50)
        self.button4.setGeometry(1050, 500, 150, 50)
        self.button5.setGeometry(1200, 500, 150, 50)
        self.button6.setGeometry(1620, 875, 300, 75)

        self.button7.setGeometry(875,700,150,50)
        self.button7.setEnabled(False)#so fica enables quando e clicado

        self.button1.clicked.connect(self.button1_clicked)
        self.button2.clicked.connect(self.button2_clicked)
        self.button3.clicked.connect(self.button3_clicked)
        self.button4.clicked.connect(self.button4_clicked)
        self.button5.clicked.connect(self.button5_clicked)

        self.button6.clicked.connect(self.button6_clicked)

        self.button7.clicked.connect(self.button7_clicked)









    def button1_clicked(self):
        path = "/home/vasco/Desktop/sky130A"#caminho para a custom sky130A folder
        if os.path.isdir(path):#verifica se o caminho existe
            os.chdir(path)#muda para o para a diretoria
            self.button1.setStyleSheet("background-color: green;")
            self.button2.setStyleSheet("")  # Set button2 to default style
            self.button3.setStyleSheet("")  # Set button2 to default style
            self.button4.setStyleSheet("")  # Set button2 to default style
            self.button5.setStyleSheet("")  # Set button2 to default style
            self.button7.setEnabled(True)#ativa o botao
        else:
            sys.exit(1)
    

    def button2_clicked(self):
        path = "/home/vasco/Desktop/sky130B"#caminho para a custom sky130A folder
        if os.path.isdir(path):#verifica se o caminho existe
            os.chdir(path)#muda para o para a diretoria
            self.button2.setStyleSheet("background-color: green;")
            self.button1.setStyleSheet("")  # Set button2 to default style
            self.button3.setStyleSheet("")  # Set button2 to default style
            self.button4.setStyleSheet("")  # Set button2 to default style
            self.button5.setStyleSheet("")  # Set button2 to default style
            self.button7.setEnabled(True)#ativa o botao
           
        else:
            sys.exit(1)


    def button3_clicked(self):
        path = "/home/vasco/Desktop/gf180mcuA"#caminho para a custom sky130A folder
        if os.path.isdir(path):#verifica se o caminho existe
            os.chdir(path)#muda para o para a diretoria
            self.button3.setStyleSheet("background-color: green;")
            self.button2.setStyleSheet("")  # Set button2 to default style
            self.button1.setStyleSheet("")  # Set button2 to default style
            self.button4.setStyleSheet("")  # Set button2 to default style
            self.button5.setStyleSheet("")  # Set button2 to default style
            self.button7.setEnabled(True)#ativa o botao
           
        else:
            sys.exit(1)
    
    def button4_clicked(self):
        path = "/home/vasco/Desktop/gf180mcuB"#caminho para a custom sky130A folder
        if os.path.isdir(path):#verifica se o caminho existe
            os.chdir(path)#muda para o para a diretoria
            self.button4.setStyleSheet("background-color: green;")
            self.button2.setStyleSheet("")  # Set button2 to default style
            self.button3.setStyleSheet("")  # Set button2 to default style
            self.button1.setStyleSheet("")  # Set button2 to default style
            self.button5.setStyleSheet("")  # Set button2 to default style
            self.button7.setEnabled(True)#ativa o botao
           
        else:
            sys.exit(1)


    def button5_clicked(self):
        path = "/home/vasco/Desktop/gf180mcuC"#caminho para a custom sky130A folder
        if os.path.isdir(path):#verifica se o caminho existe
            os.chdir(path)#muda para o para a diretoria
            self.button5.setStyleSheet("background-color: green;")
            self.button2.setStyleSheet("")  # Set button2 to default style
            self.button3.setStyleSheet("")  # Set button2 to default style
            self.button1.setStyleSheet("")  # Set button2 to default style
            self.button4.setStyleSheet("")  # Set button2 to default style
            self.button7.setEnabled(True)#ativa o botao
           
        else:
            sys.exit(1)

    def button6_clicked(self):#butao de saida
        sys.exit(1)


    def button7_clicked(self):#butao de saida
        current_directory = os.getcwd() 
        if current_directory == "/home/vasco/Desktop/sky130A":
            self.new_window = sky130A()  # Create an instance of the new window class
            self.new_window.show()  # Show the new window
            self.close()  # Close the original window

        
class sky130A(QWidget):
    def __init__(self):
         super().__init__()
         self.setWindowTitle("skyA menu")# nome da janela
         desktop = QApplication.desktop()# vai buscar o widget do dektop
         screen_geometry = desktop.screenGeometry() #associa as dimensoes do desktop na variavel
         self.setGeometry(screen_geometry)#inicializa a janela com as dimensoes
         palette = self.palette()#cria uma classe filho palette
         background_color = palette.color(QPalette.Window)#vai buscar a cor de fundo da janela


         pixmap = QPixmap("/home/vasco/Desktop/my_pythonlib/IST_-_Instituto_Superior_Tecnico.png")#carrega a imagem na variavel pixmap
         smaller_pixmap = pixmap.scaled(300, 100, Qt.KeepAspectRatio)#reduz o aspeto da imagem
         image = QLabel(self) #cria uma classe chamada atraves de qlabel em funcao da classe pai Qlabel
         image.setPixmap(smaller_pixmap )#faz com que a imagem seja displaeyed na na classe imagem criada
         image.setAlignment(Qt.AlignCenter)#centraliza a imagem
         image.setGeometry(0, 0, 350, 100) #geometria e posiçao (x,y,x_tamanho,t_tamanho)


         self.button1 = QPushButton("exit",self)
         self.button1.setFixedSize(300, 75)
         self.button1.setGeometry(1620, 875, 300, 75)
         self.button1.clicked.connect(self.button1_clicked)


         self.button2 = QPushButton("back",self)
         self.button2.setFixedSize(300, 75)
         self.button2.setGeometry(0, 875, 300, 75)
         self.button2.clicked.connect(self.button2_clicked)


         self.button3 = QPushButton("caracteristicas Mos",self)
         self.button3.setFixedSize(200, 75)
         self.button3.setGeometry(650, 400, 300, 75)
         self.button3.clicked.connect(self.button3_clicked)



         # Add widgets or customize the new window as needed...

    def button1_clicked(self):#butao de saida
        sys.exit(1)
    

    def button2_clicked(self):#butao de saida
        self.new_window = janela()  # Create an instance of the new window class
        self.new_window.show()  # Show the new window
        self.close()  # Close the original window


    def button3_clicked(self):
        current_directory = os.getcwd() 
        path = os.path.join(current_directory, "sim_data")
        if os.path.isdir(path):#verifica se o caminho existe
            os.chdir(path)#muda para o para a diretoria
            print(os.getcwd())

        self.new_window = sky130A_caracteristicas()  # Create an instance of the new window class
        self.new_window.show()  # Show the new window
        self.close()  # Close the original window
        
            
class sky130A_caracteristicas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("skyA menu")# nome da janela
        desktop = QApplication.desktop()# vai buscar o widget do dektop
        screen_geometry = desktop.screenGeometry() #associa as dimensoes do desktop na variavel
        self.setGeometry(screen_geometry)#inicializa a janela com as dimensoes
        palette = self.palette()#cria uma classe filho palette
        background_color = palette.color(QPalette.Window)#vai buscar a cor de fundo da janela


        pixmap = QPixmap("/home/vasco/Desktop/my_pythonlib/IST_-_Instituto_Superior_Tecnico.png")#carrega a imagem na variavel pixmap
        smaller_pixmap = pixmap.scaled(300, 100, Qt.KeepAspectRatio)#reduz o aspeto da imagem
        image = QLabel(self) #cria uma classe chamada atraves de qlabel em funcao da classe pai Qlabel
        image.setPixmap(smaller_pixmap )#faz com que a imagem seja displaeyed na na classe imagem criada
        image.setAlignment(Qt.AlignCenter)#centraliza a imagem
        image.setGeometry(0, 0, 350, 100) #geometria e posiçao (x,y,x_tamanho,t_tamanho)

        self.button1 = QPushButton("exit",self)
        self.button1.setFixedSize(300, 75)
        self.button1.setGeometry(1620, 875, 300, 75)
        self.button1.clicked.connect(self.button1_clicked)

        self.button2 = QPushButton("back",self)
        self.button2.setFixedSize(300, 75)
        self.button2.setGeometry(0, 875, 300, 75)
        self.button2.clicked.connect(self.button2_clicked)
        
        current_directory = os.getcwd() 
        folder_names = os.listdir(current_directory)
        self.combo_box = QComboBox(self)
        self.combo_box.clear()
        self.combo_box.addItem("")
        self.combo_box.addItems(folder_names)
        self.combo_box.setGeometry(150, 300, 150, 50)
        self.combo_box.currentIndexChanged.connect(self.selection_changed)

        
        self.combo_box2 = QComboBox(self)
        self.combo_box2.setGeometry(350, 300, 150, 50)
        self.combo_box2.currentIndexChanged.connect(self.selection_changed2)
        self.combo_box2.setEnabled(False)#so fica enables quando e clicado



        self.combo_box3 = QComboBox(self)
        self.combo_box3.setGeometry(550, 300, 150, 50)
        self.combo_box3.currentIndexChanged.connect(self.selection_changed3)
        self.combo_box3.setEnabled(False)#so fica enables quando e clicado




        self.combo_box4 = QComboBox(self)
        self.combo_box4.setGeometry(750, 300, 150, 50)
        self.combo_box4.currentIndexChanged.connect(self.selection_changed2)
        self.combo_box4.setEnabled(False)#so fica enables quando e clicado









        
        font = QFont()#cria uma class do tamanho
        font.setPointSize(16)#da se set para um tamanho de 40

        text_label = QLabel(self)#ccria uma classe textlabel
        text_label.setText("cells")#texto
        text_label.setFont(font)#tamano da letra
        text_label.setStyleSheet("QLabel { background-color: %s; padding: 10px; }" % background_color.name())  # Set the background color using the retrieved color
        text_label.setAlignment(Qt.AlignCenter)
        text_label.setGeometry(150, 250, 150, 50)



        text_label2 = QLabel(self)#ccria uma classe textlabel
        text_label2.setText("simulacoes")#texto
        text_label2.setFont(font)#tamano da letra
        text_label2.setStyleSheet("QLabel { background-color: %s; padding: 10px; }" % background_color.name())  # Set the background color using the retrieved color
        text_label2.setAlignment(Qt.AlignCenter)
        text_label2.setGeometry(350, 250, 150, 50)



        text_label3 = QLabel(self)#ccria uma classe textlabel
        text_label3.setText("visualização")#texto
        text_label3.setFont(font)#tamano da letra
        text_label3.setStyleSheet("QLabel { background-color: %s; padding: 10px; }" % background_color.name())  # Set the background color using the retrieved color
        text_label3.setAlignment(Qt.AlignCenter)
        text_label3.setGeometry(550, 250, 150, 50)

        self.button3 = QPushButton("proseguir",self)
        self.button3.setFixedSize(300, 75)
        self.button3.setGeometry(800, 600, 300, 75)
        #self.button3.clicked.connect(self.button3_clicked)
        self.button3.setEnabled(False)#so fica enables quando e clicado

    def button1_clicked(self):#butao de saida
        sys.exit(1)
    
    def button2_clicked(self):#butao de saida
        path = "/home/vasco/Desktop/sky130A"
        if os.path.isdir(path):#verifica se o caminho existe
            os.chdir(path)#muda para o para a diretoria
        self.new_window = sky130A()  # Create an instance of the new window class
        self.new_window.show()  # Show the new window
        self.close()  # Close the original window

    def selection_changed(self, index):
        selected_option = self.combo_box.currentText()
        current_directory = os.getcwd()
        path = os.path.join(current_directory, selected_option)
        if os.path.isdir(path):#verifica se o caminho existe
            self.combo_box2.setEnabled(True)#so fica enables quando e clicado
            os.chdir(path)#muda para o para a diretoria
            self.combo_box2.clear()
            folder_names = os.listdir(path)
            self.combo_box2.addItem("")
            self.combo_box2.addItems(folder_names)
        if selected_option == "":
            path = "/home/vasco/Desktop/sky130A/sim_data"
            if os.path.isdir(path):#verifica se o caminho existe
                os.chdir(path)#muda para o para a diretoria
                self.combo_box2.setEnabled(False)#so fica enables quando e clicado
                self.combo_box3.setEnabled(False)#so fica enables quando e clicado
                self.combo_box2.clear()
                self.button3.setEnabled(False)#so fica enables quando e clicado
                self.combo_box4.setEnabled(False)#so fica enables quando e clicado
                self.combo_box4.clear()
                self.combo_box3.clear()
                
    def selection_changed2(self, index):
        selected_option = self.combo_box2.currentText()
        current_directory = os.getcwd()
        path = os.path.join(current_directory, selected_option)
        if os.path.isdir(path):#verifica se o caminho existe
            os.chdir(path)#muda para o para a diretoria
            print(path)
            self.combo_box3.setEnabled(True)#so fica enables quando e clicado
            self.combo_box3.addItem("")
            self.combo_box3.addItem("plot_3d_var")
            self.combo_box3.addItem("with temp variation")
        if selected_option == "":
            selected_option = self.combo_box.currentText()
            path = "/home/vasco/Desktop/sky130A/sim_data"
            path = os.path.join(path, selected_option)
            print(path)
            print(selected_option)
            if os.path.isdir(path):#verifica se o caminho existe
                os.chdir(path)#muda para o para a diretoria
                self.combo_box3.setEnabled(False)#so fica enables quando e clicado
                self.combo_box4.setEnabled(False)#so fica enables quando e clicado
                self.button3.setEnabled(False)#so fica enables quando e clicado
                self.combo_box3.clear()
                self.combo_box3.clear()

    def selection_changed3(self, index):
        selected_option = self.combo_box3.currentText()
        if selected_option == "plot_3d_var":
            self.combo_box4.setEnabled(True)#so fica enables quando e clicado
            current_directory = os.getcwd() 
            self.combo_box4.clear()
            self.combo_box4.addItem("")
            folder_names = os.listdir(current_directory)
            csv_files = [file for file in folder_names if file.endswith(".csv")]# so poe na combo box os ficheiros csv
            self.combo_box4.addItems(csv_files)
        else:
            self.combo_box4.setEnabled(False)#so fica enables quando e clicado
            self.combo_box4.clear()
            

