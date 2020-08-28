from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+","%","^"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        #label
        main_layout.add_widget(Label(text="Calvy - Kivy Calculator",
        size_hint = (.4, .4),
        pos_hint={"center_x": 0.5, "center_y": 0.5}))
        #display
        self.calculation = TextInput(
            multiline=True, readonly=True, halign="right", font_size=250)
        main_layout.add_widget(self.calculation)
        buttons = [
            ["%", "^", "Del", "+"],
            ["7", "8", "9", "-"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "/"],
            [".", "0", "C", "="],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:	 
                if label == "=":
                	button = Button(
                    text=label,
                    background_color = (1, 0, 1, 1),
                    pos_hint={"center_x": 0.5, "center_y": 0.5})
                	button.bind(on_press=self.calculate)
                	h_layout.add_widget(button)
                	continue
                button = Button(
                    text=label,
                    size_hint = (.9, .9),
                    pos_hint={"center_x": 0.4, "center_y": 0.4})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
        return main_layout

    def on_button_press(self, instance):
        current = self.calculation.text
        button_text = instance.text

        if button_text == "C":
            # Clear the calculation widget
            self.calculation.text = ""
        elif button_text == "Del":
        	self.calculation.text = self.calculation.text[:-1]
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                # Don't add two operators right after each other
                return
            elif current == "" and ( button_text in self.operators or button_text == "0"):
                # First character cannot be an operator or zero
                return
            else:
                new_text = current + button_text
                self.calculation.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def calculate(self, instance):
        text = self.calculation.text
        if text:
            try:
            	self.calculation.text = self.calculation.text.replace("^", "**")
            	calculation = str(eval(self.calculation.text))
            	self.calculation.text = calculation
            except Exception:
            	self.calculation.text = "Error"


if __name__ == "__main__":
    app = MainApp()
    app.run()
