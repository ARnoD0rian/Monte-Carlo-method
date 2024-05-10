import tkinter as tk
from tkinter.messagebox import showerror, showinfo
from tkinter.simpledialog import askstring
from method.method import MonteCarlo
from method.figure.point.point import Point
from method.figure.figure import Figure
import re

class GUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Метод Монта-Карло")

        # Кнопка для расчета площади
        self.area_button = tk.Button(self.root, text="Расчитать площадь", command=self.toggle_area_fields, width=30)
        self.area_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # Кнопка для расчета интеграла
        self.integral_button = tk.Button(self.root, text="Расчитать интеграл", command=self.toggle_integral_fields, width=30)
        self.integral_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        
        self.menu.add_command(label="Запустить", command=self._start_algorithm)

        
        self.menu_entry = {
            "area": {
                "text": {
                    "figure": None,
                    "limits": None 
                },
                "entry": {
                    "area": None,
                    "limits": None
                }
            },
            "integral": {
                "text": {
                    "figure": None,
                    "limits": None 
                },
                "entry": {
                    "func": None,
                    "limits": None
                }
            }
        }

    def toggle_area_fields(self) -> None:
        if self.menu_entry["integral"]["text"]["figure"] is not None:
            self._delete("integral")
            
        self.menu_entry["area"]["text"]["figure"] = tk.Label(self.root, text="Введите фигуру:")
        self.menu_entry["area"]["text"]["figure"].grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.menu_entry["area"]["entry"]["figure"] = tk.Text(self.root, height=5, width=30)
        self.menu_entry["area"]["entry"]["figure"].grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        
        self.menu_entry["area"]["text"]["limits"] = tk.Label(self.root, text="Введите ограничения на x и y:")
        self.menu_entry["area"]["text"]["limits"].grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.menu_entry["area"]["entry"]["limits"] = tk.Text(self.root, height=5, width=30)
        self.menu_entry["area"]["entry"]["limits"].grid(row=2, column=1, padx=10, pady=10, sticky="ew")

    def toggle_integral_fields(self):
        if self.menu_entry["area"]["text"]["figure"] is not None:
            self._delete("area")
            
        self.menu_entry["integral"]["text"]["figure"] = tk.Label(self.root, text="Введите функцию")
        self.menu_entry["integral"]["text"]["figure"].grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.menu_entry["integral"]["entry"]["figure"] = tk.Text(self.root, height=5, width=30)
        self.menu_entry["integral"]["entry"]["figure"].grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        
        self.menu_entry["integral"]["text"]["limits"] = tk.Label(self.root, text="Введите пределы интегрирования")
        self.menu_entry["integral"]["text"]["limits"].grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        self.menu_entry["integral"]["entry"]["limits"] = tk.Text(self.root, height=5, width=30)
        self.menu_entry["integral"]["entry"]["limits"].grid(row=2, column=1, padx=10, pady=10, sticky="ew")
        
    def _delete(self, name: str) -> None:
        self.menu_entry[name]["text"]["figure"].destroy()
        self.menu_entry[name]["text"]["limits"].destroy()
        self.menu_entry[name]["entry"]["figure"].destroy()
        self.menu_entry[name]["entry"]["limits"].destroy()
        
        self.menu_entry[name]["text"]["figure"] = None
        self.menu_entry[name]["text"]["limits"] = None
        self.menu_entry[name]["entry"]["figure"] = None
        self.menu_entry[name]["entry"]["limits"] = None
        
    def _start_algorithm(self) -> None:
        N = int(askstring(title="N", prompt="Ввведите N"))
        if self.menu_entry["integral"]["text"]["figure"] is not None:
            limits = self.menu_entry["integral"]["entry"]["limits"].get('1.0', 'end-1c')
            limits = [float(limit) for limit in limits.split(' ')]
            
            func = self.menu_entry["integral"]["entry"]["figure"].get('1.0', 'end-1c')
            I = MonteCarlo.integrate(func, limits, N=N)
            showinfo(title="успешно", message=f"I = {I}")
            
        elif self.menu_entry["area"]["text"]["figure"] is not None:
            limits = self.menu_entry["area"]["entry"]["limits"].get('1.0', 'end-1c')
            limits = limits.split('\n')
            
            figure = self.menu_entry["area"]["entry"]["figure"].get('1.0', 'end-1c')
            figure = figure.split('\n')
            
            x = [float(k) for k in re.findall(r'-?\d+\.\d+|-?\d+', limits[0])]
            y = [float(l) for l in re.findall(r'-?\d+\.\d+|-?\d+', limits[1])]
            points = [Point(k, l) for k, l in zip(x, y)]
            figure = Figure(figure)
            S = MonteCarlo.calculating_area(figure, points, N=N)
            showinfo(title="успешно", message=f"S = {S}")
            
    def start(self) -> None:
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()