from label import Label


class ButtonConfigurator:
    def on_click_number(self, label: Label, number: str):
        current_text = label.text
        label.update_text(new_text=current_text + number)

    def configure_background(self, button_text: str):
        if button_text == 'C':
            return '#ff6666'

        elif button_text == '=':
            return '#9ACDB1'

        elif button_text in list('0123456789'):
            return '#9ABFCD'

        else:
            return '#99CCCC'

    def configure_command(self, button_text: str, label: Label):
        if button_text == 'C':
            return lambda: label.update_text('0')

        elif button_text == 'del':
            return lambda: label.update_text(label.label_text.cget(key='text')[0:-1])

        elif button_text == 'X^2':
            return lambda: label.update_text(str((eval(label.label_text.cget(key='text')) ** 2)))

        elif button_text == '=':
            return lambda: label.update_text(str(eval(label.label_text.cget(key='text'))))

        elif button_text == '+/-':
            return lambda: label.update_text(str((eval((label.label_text.cget(key='text'))) * -1)))

        else:
            if label.label_text.cget(key='text') == '0':
                return lambda: label.update_text(new_text=button_text)

            return lambda: on_click_number(label=label, number=button_text)
            # return lambda: label.update_text(label.label_text.cget(key='text') + button_text)
