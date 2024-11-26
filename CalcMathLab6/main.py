import tkinter as tk
from tkinter import messagebox
from SolverClass import Solver

def calculate():
    global entries,results_frame,root
    try:
        matrix = [[0] * (len(entries) + 1) for _ in range(len(entries))]#считываем матрицу и точность
        for i in range(len(entries)):
            for j in range(len(entries) + 1):
                matrix[i][j] = float(entries[i][j].get())
        precision = int(entry_precision.get())
        print(precision)
    except ValueError as ve:
        messagebox.showerror("Unnaceptable value", str(ve))
        return

    equationsSystem = Solver(matrix,precision)#создаём обьект решателя СЛАУ
    isApplicable = equationsSystem.applicabilityCheck()

    if results_frame is not None:
        results_frame.destroy()
    results_frame = tk.Frame(root)
    results_frame.grid(row = 4,column = 0,columnspan=3,padx=10,pady=10)

    if isApplicable == 'assymetrical matrix':#проверка на симметричность матрицы
        result_label = tk.Label(results_frame,text='the matrix is not symmetrical')
        result_label.grid(row=0,column=0)
        return
    if isApplicable == "no diagonal dominance":#проверка на наличие диагонального пребладания
        result_label = tk.Label(results_frame,text="matrix has no diagonal dominance")
        result_label.grid(row=0,column=0)
        return

    roots = equationsSystem.solve()

    if roots == "no definite single solution":#проверка на наличие определённого единственного решения
        result_label = tk.Label(results_frame, text='no definite single solution')
        result_label.grid(row=0, column=0)
    else:
        for i in range(len(entries)):
            result_label = tk.Label(results_frame, text="X" + str(i + 1) + " = ")
            result_label.grid(row=i, column=0, padx=(10, 2), pady=(5, 2), sticky="e")

            result_value = tk.Entry(results_frame, width=10, state='normal')
            result_value.insert(0, str(roots[i]))
            result_value.config(state='readonly')
            result_value.grid(row=i, column=1, padx=(2, 10), pady=(5, 2), sticky="w")
        diff_check = equationsSystem.correctnessCheck()
        diff_label = tk.Label(root, text="max root incorrectness")
        diff_label.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

        diff_value = tk.Entry(root, width=10, state='normal')
        diff_value.insert(0, str(max(diff_check)))
        diff_value.config(state="readonly")
        diff_value.grid(row=5, column=1, columnspan=3, padx=10, pady=10)


def create_grid():
    global entries,grid_frame,results_frame

    if grid_frame is not None:
        grid_frame.destroy()
    if results_frame is not None:
        results_frame.destroy()

    try:
        n = int(entry_n.get())
        if n <= 0:
            raise ValueError("n must be a positive integer.")

        grid_frame = tk.Frame(root)
        grid_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        entries = [[None for _ in range(n+1)] for _ in range(n)]
        for i in range(n):
            for j in range(n+1):
                entry = tk.Entry(grid_frame, width=5)
                entry.grid(row=i, column=j, padx=5, pady=5)
                entries[i][j] = entry

        button_calculate = tk.Button(root, text="Calculate", command=calculate)
        button_calculate.grid(row=3, column=0, columnspan=3, pady=(10, 0))

    except ValueError as ve:
        messagebox.showerror("Unnacetpable value as n(or precision)", str(ve))


root = tk.Tk()
root.title("Linear equations systems solver")

entries = []
result_fields = []
grid_frame = None
results_frame = None

label_n = tk.Label(root, text="Enter amount of equations/variables:")
label_n.grid(row=0, column=0, padx=10, pady=10)

entry_n = tk.Entry(root)
entry_n.grid(row=0, column=1, padx=10, pady=10)

button_create = tk.Button(root, text="Enter", command=create_grid)
button_create.grid(row=0, column=2, padx=10, pady=10)

label_b = tk.Label(root,text="Precision:")
label_b.grid(row=1,column=0,padx=10,pady=10)

entry_precision = tk.Entry(root)
entry_precision.insert(0,5)
entry_precision.grid(row=1,column=1,padx=10,pady=10)

root.mainloop()