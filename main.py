from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
import mysql.connector

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="she_her",
        password="onlyyouu",
        database="jasa_fotografiii"
    )

# Screens
class HomeScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class ServicesScreen(Screen):
    pass

class JobsScreen(Screen):
    pass

class SignUpScreen(Screen):
    def sign_up_user(self, name, email, password):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, email, password))
            conn.commit()
            cursor.close()
            conn.close()
            self.ids.signup_status.text = "Sign-up successful!"
        except Exception as e:
            self.ids.signup_status.text = f"Error: {e}"

class LoginScreen(Screen):
    def login_user(self, email, password):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE email = %s AND password = %s"
            cursor.execute(query, (email, password))
            user = cursor.fetchone()
            cursor.close()
            conn.close()
            if user:
                self.ids.login_status.text = f"Welcome, {user[1]}!"
                App.get_running_app().root.current = 'home'
            else:
                self.ids.login_status.text = "Invalid email or password."
        except Exception as e:
            self.ids.login_status.text = f"Error: {e}"

class PhotographyApp(App):
    def build(self):
        Window.size = (800, 600)
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(AboutScreen(name='about'))
        sm.add_widget(ServicesScreen(name='services'))
        sm.add_widget(JobsScreen(name='jobs'))
        sm.add_widget(SignUpScreen(name='signup'))
        sm.add_widget(LoginScreen(name='login'))
        return sm

if __name__ == "__main__":
    PhotographyApp().run()
