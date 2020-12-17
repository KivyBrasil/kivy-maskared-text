from kivy.uix.textinput import TextInput

class MaskaredText(TextInput):
    symbol = "0123456789/"
    use_symbol = True

    mask = "##/##/####"
    use_mask = True

    def insert_text(self, string, from_undo=False):
        text_size = len(self.text)
        mask_size = len(self.mask)

        if self.use_symbol:
            """Used to filter the text by the symbol that you specify."""
            if string in self.symbol:
                pass
            else:
                return super(MaskaredText, self).insert_text("", from_undo=from_undo)

        if self.use_mask:
            """Used to filter the text by the mask that you specify."""
            if text_size == mask_size:
                return super(MaskaredText, self).insert_text("", from_undo=from_undo)

            try:
                if self.mask[text_size] == "#":
                    int(string)
                else:
                    if string != self.mask[text_size]:
                        string = self.mask[text_size] + string
                return super(MaskaredText, self).insert_text(string, from_undo=from_undo)
            except Exception as e:
                print("except", str(e))

            return super(MaskaredText, self).insert_text("", from_undo=from_undo)

        return super(MaskaredText, self).insert_text(string, from_undo=from_undo)

if __name__ == "__main__":
    from kivy.app import App
    from kivy.lang import Builder

    class MainApp(App):
        def build(self):
            return Builder.load_string("""
BoxLayout:
    orientation: "vertical"
    MaskaredText:
        font_size: sp(50)
        multiline: True
        mask: mask.text
        symbol: symbol.text
        use_symbol: use_symbol.active
        use_mask: use_mask.active
    BoxLayout:
        Label:
            text: "Symbol"
            size_hint_x: .3
        CheckBox:
            id: use_symbol
            active: True
            size_hint_x: .2
        TextInput:
            id: symbol
            size_hint_x: .5
            text: "0123456789/"
            hint_text: "Your Symbol"
    BoxLayout:
        Label:
            text: "Mask"
            size_hint_x: .3
        CheckBox:
            id: use_mask
            active: True
            size_hint_x: .2
        TextInput:
            id: mask
            size_hint_x: .5
            text: "##/##/####"
            hint_text: "Your Mask"
    """)

    MainApp().run()