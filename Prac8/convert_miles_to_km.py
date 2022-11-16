from kivy.app import App
from kivy.lang import Builder

m_to_km = 1.6


class MilesConverterApp(App):

    def build(self):
        """ creates Kivy app from kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root

    def handle_calculations(self):
        """ Converts from miles to kilometres """
        value = float(self.root.ids.input_miles.text)
        result = value * m_to_km
        self.root.ids.output_label.text = str(result)

    def handle_increments(self, change):
        value = float(self.root.ids.input_miles.text)
        self.root.ids.input_miles.text = str(value)
        self.handle_calculations()


MilesConverterApp().run()
