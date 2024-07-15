import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class RegistrationApp(App):
    def build(self):
        self.title = "Game Registration Form"
        layout = BoxLayout(orientation='vertical', padding=30, spacing=10)

        # Add widgets
        layout.add_widget(Label(text='Username:'))
        self.username = TextInput(multiline=False)
        layout.add_widget(self.username)

        layout.add_widget(Label(text='Age:'))
        self.Age = TextInput(multiline=False)
        layout.add_widget(self.Age)

        layout.add_widget(Label(text='Email:'))
        self.email = TextInput(multiline=False)
        layout.add_widget(self.email)

        layout.add_widget(Label(text='country:'))
        self.country = TextInput(multiline=False)
        layout.add_widget(self.country)

        layout.add_widget(Label(text='Password:'))
        self.password = TextInput(password=True, multiline=False)
        layout.add_widget(self.password)

        layout.add_widget(Label(text='Repassword:'))
        self.Repassword = TextInput(multiline=False)
        layout.add_widget(self.Repassword)

        submit_button = Button(text='Submit')
        submit_button.bind(on_press=self.submit)
        layout.add_widget(submit_button)
        on_press=self.submit

        return layout

    def submit(self, instance):
        print(f'username:{self.username.text}')
        print(f'Age:{self.Age.text}')
        print(f'email:{self.email.text}')
        print(f'country:{self.country.text}')
        print(f'password:{self.password.text}')
        print(f'repassword:{self.repassword.text}')

        if username.strip() == '' or Age.strip() == '' or email.strip() == '' or country.strip() == '' or password.strip() == '' or repassword.strip() == '':
            message ="please fill in all field"


 # Here you can add code to handle the registration logic


if __name__ == '__main__':
    RegistrationApp().run()



