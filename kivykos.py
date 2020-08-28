import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle, Color, Line
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
import pandas as pd
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup


file = open('data.csv', 'a')
class CellLabel(Label):
    pass

class Main(Screen):

    def btn_add_data(self):
        print("Add Data")

    def btn_edit_data(self):
        print("Edit Data")

    def btn_see_data(self):
        print("See Data")



class Show(Screen):
    def __init__(self,**kwargs):
        super(Show,self).__init__(**kwargs)
        Clock.schedule_once(self.fill)

    def fill(self, dt):
            # fill the GridLayout with CellLabels
        df = pd.read_csv('data.csv')
        grid = self.ids.grid
        grid.cols = df.shape[1]
        for row in df.values:
            for col in row:
                txt = str(col).strip()
                if txt == 'nan':
                    txt = ''
                grid.add_widget(CellLabel(text=txt))
        Clock.schedule_once(self.do_centering)

    def do_centering(self, dt):
            # center the text in each CellLabel

            # start by getting the max width of each column
        grid = self.ids.grid
        reversed = grid.children[:]
        reversed.reverse()
        max_col_widths = [0] * grid.cols
        col = 0
        for cell in reversed:
            if cell.width > max_col_widths[col]:
                max_col_widths[col] = cell.width
            col += 1
            col = col % grid.cols

            # use those max widths to center the text in each CellLabel
        col = 0
        for cell in reversed:
            cell.width = max_col_widths[col]
            cell.halign = 'center'
            cell.text_size = cell.size
            col += 1
            col = col % grid.cols

        #with self.canvas:
            #Color(.62,.91,.968,1, mode='rgba')
            #Rectangle(pos=(0, 0), size=(2000, 2000))
            #Color(.83,1,1,1,mode='rgba')
            #Rectangle(pos=(0,140),size=(2000,1000))


        #df = str((pd.read_csv('data.csv')))
        #self.add_widget(Label(text=df, color=(0, 0, 0, 1)))

class Add(Screen):
    nama_lengkap = ObjectProperty(None)
    nomor_kamar = ObjectProperty(None)
    biaya_kos = ObjectProperty(None)
    tanggal_masuk = ObjectProperty(None)
    tanggal_bayar = ObjectProperty(None)


    def submit(self):

        print("Nama:",self.nama_lengkap.text,"\nNomor Kamar:",self.nomor_kamar.text,"\nBiaya Kos:",self.biaya_kos.text,"\nTanggal Masuk:",self.tanggal_masuk.text,"\nTanggal Bayar:",self.tanggal_bayar.text)


        file.write(f"\n{self.nama_lengkap.text},{self.nomor_kamar.text},{self.biaya_kos.text},{self.tanggal_masuk.text},{self.tanggal_bayar.text}")
        print(f"{self.nama_lengkap.text}has been added to the list")
        file.close()

        self.nama_lengkap.text = ""
        self.nomor_kamar.text = ""
        self.biaya_kos.text = ""
        self.tanggal_masuk.text = ""
        self.tanggal_bayar.text = ""

class Delete(Screen):
    hapus_nama = ObjectProperty(None)
    def __init__(self,**kwargs):
        super(Delete,self).__init__(**kwargs)
        Clock.schedule_once(self.fill)

    def fill(self, dt):
            # fill the GridLayout with CellLabels
        df = pd.read_csv('data.csv')
        grid = self.ids.grid
        grid.cols = df.shape[1]
        for row in df.values:
            for col in row:
                txt = str(col).strip()
                if txt == 'nan':
                    txt = ''
                grid.add_widget(CellLabel(text=txt))
        Clock.schedule_once(self.do_centering)

    def do_centering(self, dt):
            # center the text in each CellLabel

            # start by getting the max width of each column
        grid = self.ids.grid
        reversed = grid.children[:]
        reversed.reverse()
        max_col_widths = [0] * grid.cols
        col = 0
        for cell in reversed:
            if cell.width > max_col_widths[col]:
                max_col_widths[col] = cell.width
            col += 1
            col = col % grid.cols

                # use those max widths to center the text in each CellLabel
        col = 0
        for cell in reversed:
            cell.width = max_col_widths[col]
            cell.halign = 'center'
            cell.text_size = cell.size
            col += 1
            col = col % grid.cols

    #with self.canvas:
        #Color(.62,.91,.968,1, mode='rgba')
        #Rectangle(pos=(0, 0), size=(2000, 2000))

    #dx = str((pd.read_csv('data.csv')))
    #self.add_widget(Label(pos_hint={"x":0,"y":0.15},text=dx, color=(0, 0, 0, 1)))

    def btn(self):
        print(self.hapus_nama.text)
        dl = pd.read_csv('data.csv')
        dl = dl.loc[~dl['Name'].str.contains(self.hapus_nama.text)]
        print(dl)
        dl.to_csv('data.csv', index=False)

class WindowManager(ScreenManager):
    pass



class Kosless(App):
    def build(self):
        #return Add()
        return Builder.load_file('kosless.kv')

if __name__ == "__main__":
    Kosless().run()

