from http.client import responses

from aiohttp import ClientSession
import requests
import pyautogui
import tkinter as tk
from threading import Thread
import time


class FunctionRunner:
    def __init__(self):
        self.is_running = False
        self.thread = None

    def checker(self, gift_name, gift_number):
            while self.is_running:
                url = f'https://t.me/nft/{gift_name}-{gift_number - 1}'
                response = requests.get(url)
                if f'{response}' != f'https://t.me/nft/{gift_name}-{gift_number - 1}':
                    print(1)
                else:
                    print('gg')
                    pyautogui.click()
                    break

    def start(self, param1, param2):
        if not self.is_running:
            self.is_running = True
            self.thread = Thread(target=self.checker, args=(param1, param2))
            self.thread.start()
            print("Gift catcher запущен")

    def stop(self):
        if self.is_running:
            self.is_running = False
            if self.thread is not None:
                self.thread.join()
            print("Gift catcher остановлен")


def on_start():
    param1 = entry_param1.get()
    param2 = int(entry_param2.get())

    if not param1 or not param2:
        status_label.config(text="Ошибка: введите оба параметра!", fg="red")
        return

    status_label.config(text="Gift catcher запущен", fg="green")
    function_runner.start(param1, param2)


def on_stop():
    function_runner.stop()
    status_label.config(text="Gift catcher остановлен", fg="black")



function_runner = FunctionRunner()


root = tk.Tk()
root.title("Gift catcher")
root.geometry("400x250")


tk.Label(root, text="Название подарка").pack(pady=(10, 0))
entry_param1 = tk.Entry(root, width=30)
entry_param1.pack()

tk.Label(root, text="Желаемый номер").pack(pady=(10, 0))
entry_param2 = tk.Entry(root, width=30)
entry_param2.pack()


button_frame = tk.Frame(root)
button_frame.pack(pady=20)

start_button = tk.Button(button_frame, text="Старт", command=on_start, width=10, bg="#000000", fg="white")
start_button.pack(side=tk.LEFT, padx=10)

stop_button = tk.Button(button_frame, text="Стоп", command=on_stop, width=10, bg="#000000", fg="white")
stop_button.pack(side=tk.LEFT, padx=10)


status_label = tk.Label(root, text="Готов к работе", fg="black")
status_label.pack(pady=10)

root.mainloop()