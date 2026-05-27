import tkinter as tk
from tkinter import ttk, scrolledtext
import subprocess
import threading
import sys
import os

class CollatzResearchHub:
    def __init__(self, root):
        self.root = root
        self.root.title("Collatz Desktop Research Hub")
        self.root.geometry("850x700")
        self.root.configure(bg="#1e1e1e")

        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background="#1e1e1e")
        style.configure("TLabel", background="#1e1e1e", foreground="#ffffff", font=("Courier", 10))
        style.configure("TButton", background="#333333", foreground="#ffffff", font=("Courier", 10, "bold"))
        style.map("TButton", background=[("active", "#4af6c3")], foreground=[("active", "#000000")])

        main_frame = ttk.Frame(root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- Parameters Section ---
        param_frame = ttk.LabelFrame(main_frame, text=" Global Parameters ", style="TFrame")
        param_frame.pack(fill=tk.X, pady=5)

        ttk.Label(param_frame, text="Target Number (n):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_n = ttk.Entry(param_frame, width=15)
        self.entry_n.insert(0, "27")
        self.entry_n.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(param_frame, text="Range Limit (Max n):").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_range = ttk.Entry(param_frame, width=15)
        self.entry_range.insert(0, "50")
        self.entry_range.grid(row=0, column=3, padx=5, pady=5)

        # --- Tools Matrix ---
        tools_frame = ttk.LabelFrame(main_frame, text=" Mathematical Execution Matrix ", style="TFrame")
        tools_frame.pack(fill=tk.X, pady=10)

        ttk.Button(tools_frame, text="1. Console Trajectory", command=lambda: self.run_script("collatz conjecture.py", use_n=True)).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        ttk.Button(tools_frame, text="2. Quantitative Metrics", command=lambda: self.run_script("length & trends.py", use_range=True)).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        ttk.Button(tools_frame, text="3. Modulo Analysis", command=lambda: self.run_script("modulo analyzer.py", use_range=True)).grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        ttk.Button(tools_frame, text="4. Parity Map (Image)", command=lambda: self.run_script("parity tracker.py", use_range=True)).grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        ttk.Button(tools_frame, text="5. Confluence Grid (Image)", command=lambda: self.run_script("confluence grid[rows link].py", use_range=True)).grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        ttk.Button(tools_frame, text="6. 3D Landscape (Image)", command=lambda: self.run_script("3d confluence mapping.py", use_range=True)).grid(row=1, column=2, padx=5, pady=5, sticky="ew")
        ttk.Button(tools_frame, text="7. Directed Graph Tree", command=lambda: self.run_script("directed graph tree.py", use_range=True)).grid(row=2, column=0, padx=5, pady=5, sticky="ew")
        ttk.Button(tools_frame, text="8. Inverse Topology (Heavy)", command=lambda: self.run_script("inverse_collatz.py", use_range=True)).grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        
        for i in range(3):
            tools_frame.columnconfigure(i, weight=1)

        # --- Asset Management ---
        asset_frame = ttk.Frame(main_frame, style="TFrame")
        asset_frame.pack(fill=tk.X, pady=5)
        ttk.Button(asset_frame, text="Open Local Image Assets Folder", command=self.open_workspace).pack(fill=tk.X)

        # --- Terminal Output ---
        ttk.Label(main_frame, text="Console Output Integration:").pack(anchor="w")
        self.terminal = scrolledtext.ScrolledText(main_frame, bg="#000000", fg="#00ff00", font=("Consolas", 10))
        self.terminal.pack(fill=tk.BOTH, expand=True, pady=5)

    def log(self, message):
        self.terminal.insert(tk.END, message + "\n")
        self.terminal.see(tk.END)

    def open_workspace(self):
        # Opens the current directory in Windows File Explorer
        try:
            os.startfile(os.getcwd())
            self.log("[+] Opened local workspace directory.")
        except Exception as e:
            self.log(f"[!] Could not open directory: {e}")

    def run_script(self, script_name, use_n=False, use_range=False):
        self.log(f"\n[+] Executing: {script_name}...")
        args = [sys.executable, script_name]
        if use_n:
            args.append(self.entry_n.get())
        if use_range:
            args.append(self.entry_range.get())

        thread = threading.Thread(target=self.execute_subprocess, args=(args,))
        thread.start()

    def execute_subprocess(self, args):
        try:
            process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                self.root.after(0, self.log, line.strip())
            process.wait()
            self.root.after(0, self.log, f"[-] {args[1]} Execution Terminated.")
        except Exception as e:
            self.root.after(0, self.log, f"[!] Error launching script: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CollatzResearchHub(root)
    root.mainloop()