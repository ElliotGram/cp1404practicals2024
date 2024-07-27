from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class DynamicLabels(App):
    def build(self):
        return Builder.load_file('dynamic_labels.kv')

    def on_start(self):
        main_box = self.root.ids.dynamic_labels
        names = ["Tik", "Tol", "Tod", "Tom", "Elliot"]
        for name in names:
            label = Label(text=name, font_size=24)
            main_box.add_widget(label)


if __name__ == "__main__":
    DynamicLabels().run()
