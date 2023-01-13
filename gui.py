#!/usr/bin/python3

import tkinter as tk
from formulas import triangle_area, circle_area, \
    triangle_coordinates


def gui():
    """
    Общие параметры окна
    """
    window = tk.Tk()
    window.title("Лабораторная работа №5")
    window.geometry("800x400")

    figure_val = tk.StringVar()

    """
    Фрейм выбора фигуры
    """

    figure_frame = tk.Frame(window)
    figure_frame.grid(row=1, column=1)

    figure = tk.Label(figure_frame, text="Фигура")
    rectangle_b = tk.Radiobutton(
            figure_frame, 
            text="Прямоугольник", 
            variable=figure_val, 
            value="rectangle" 
            )
    triangle_b = tk.Radiobutton(
            figure_frame, 
            text="Треугольник", 
            variable=figure_val, 
            value="triangle" 
            )
    circle_b = tk.Radiobutton(
            figure_frame, 
            text="Круг", 
            variable=figure_val, 
            value="circle" 
            )
    
    figure.pack(side=tk.TOP)
    rectangle_b.pack(anchor="w")
    triangle_b.pack(anchor="w")
    circle_b.pack(anchor="w")

    """
    Фрейм ввода параметров фигуры
    
    сокращения в именах:
    фигура__сторона(буква)__{l-Lablel / e-Entry}
    """
    figure_params_frame = tk.Frame(window)
    figure_params_frame.grid(row=1, column=2)
    
    figure_params_l = tk.Label(figure_params_frame, text="Параметры фигуры")
    fig_params_entry_frame = tk.Frame(figure_params_frame)
    
    fig_params_entry_frame.grid(row=2, column=2)
    rectangle_a_l = tk.Label(fig_params_entry_frame, text="a")
    rectangle_a_e = tk.Entry(fig_params_entry_frame)
    rectangle_b_l = tk.Label(fig_params_entry_frame, text="b")
    rectangle_b_e = tk.Entry(fig_params_entry_frame)
    
    triangle_a_l = tk.Label(fig_params_entry_frame, text="a")
    triangle_a_e = tk.Entry(fig_params_entry_frame)
    triangle_b_l = tk.Label(fig_params_entry_frame, text="b")
    triangle_b_e = tk.Entry(fig_params_entry_frame)
    triangle_c_l = tk.Label(fig_params_entry_frame, text="c")
    triangle_c_e = tk.Entry(fig_params_entry_frame)
    
    circle_r_l = tk.Label(fig_params_entry_frame, text="r")
    circle_r_e = tk.Entry(fig_params_entry_frame)
    
    figure_params_l.grid(row=1, column=2)
    
    rectangle_a_l.grid(row=2, column=1)
    rectangle_a_e.grid(row=2, column=2)
    rectangle_b_l.grid(row=2, column=3)
    rectangle_b_e.grid(row=2, column=4)

    triangle_a_l.grid(row=3, column=1)
    triangle_a_e.grid(row=3, column=2)
    triangle_b_l.grid(row=3, column=3)
    triangle_b_e.grid(row=3, column=4)
    triangle_c_l.grid(row=3, column=5)
    triangle_c_e.grid(row=3, column=6)
    
    circle_r_l.grid(row=4, column=1)
    circle_r_e.grid(row=4, column=2)

    """
    Фрейм для кнопок расчитать и выход
    """
    calculate_frame = tk.Frame(window)
    calculate_frame.grid(row=2, column=1)

    def action():
        draw_shape()

    def exit_butt():
        exit(0)

    calc_area_b = tk.Button(calculate_frame, text="Расчитать площадь", command=action)
    exit_b = tk.Button(calculate_frame, text="Выход", command=exit_butt)
    
    calc_area_b.pack(anchor="w")
    exit_b.pack(anchor="w")
    
    """
    Фрейм для отрисовки фигуры
    """

    show_frame = tk.Frame(window)
    show_frame.grid(row=2, column=2)
    canvas = tk.Canvas(show_frame, width=200, height=200)
    canvas.pack()

    def draw_shape():
        canvas.delete("all")
        area_label.config(text="Площадь: ")
        selected_shape = figure_val.get()

        if selected_shape == "rectangle":
            width = float(rectangle_a_e.get())
            height = float(rectangle_b_e.get())

            area_label.config(text="Площадь: " + str(width * height))
            canvas.create_rectangle(50, 50, 50 + width, 50 + height, fill="blue")

        elif selected_shape == "triangle":
            side1 = float(triangle_a_e.get())
            side2 = float(triangle_b_e.get())
            side3 = float(triangle_c_e.get())

            coords = triangle_coordinates(side1, side2, side3)

            canvas.create_polygon(coords, fill="green")
            area_label.config(text="Площадь: " + str(triangle_area(side1, side2, side3)))
        elif selected_shape == "circle":
            # Get the radius of the circle from the entry widget
            radius = float(circle_r_e.get())

            # Draw the circle
            canvas.create_oval(50, 50, 50 + 2 * radius, 50 + 2 * radius, fill="red")
            area_label.config(text="Площадь: " + str(circle_area(radius)))

    area_label = tk.Label(show_frame, text="")
    area_label.pack()

    window.mainloop()


if __name__ == "__main__":
    gui()
