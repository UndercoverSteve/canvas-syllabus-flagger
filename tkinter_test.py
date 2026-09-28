#tkinter import for GUI
import tkinter as tk
from tkinter import ttk

#Direct import for text scan script
import txt_scan

def scan_syllabus():
    #Clear any possible remaining results from prior run
    results_box.delete("1.0", tk.END)

    #retrieve results from txt_scan
    results = txt_scan.main_task()

    #Display results
    for result in results:
        results_box.insert(tk.END, result + "\n")

#Main setup for app, set 600x400 for testing, can be set
#to a different size later if needed
root = tk.Tk()
root.geometry("600x400")
root.title("Syllabus Scanner")

#Setup container for GUI widgets
frm = ttk.Frame(
    root,
    padding=10
)
frm.pack(
    fill="both",
    expand=True
)

#Main label for GUI
ttk.Label(
    frm,
    text="Syllabus Scanner"
).pack(pady=10)

#Button to execute scan
ttk.Button(
    frm,
    text = "Scan Syllabus",
    command=scan_syllabus
).pack(pady=5)

#Format results area
results_box = tk.Text(
    frm,
    height=15,
    width=70
)
results_box.pack(
    fill="both",
    expand=True,
    pady=10
)

#Quit button
ttk.Button(
    frm,
    text="Quit",
    command=root.destroy
).pack(pady=5)

root.mainloop()

#TODO:
    #Add code to provide more context in results, i.e. which sections
        #were found and which ones were not
    #Additional button for choosing syllabus file to scan
    #Window resizing?
