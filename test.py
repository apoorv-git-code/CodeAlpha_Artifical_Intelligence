import tkinter as tk
from tkinter import ttk, messagebox
import threading
import requests

class LanguageTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator Tool")
        self.root.geometry("750x450")
        self.root.configure(bg="#f1f5f9")
        
        # Language mapping (Display Name: API Code)
        self.languages = {
            "English": "en-GB",
            "Spanish": "es-ES",
            "French": "fr-FR",
            "German": "de-DE",
            "Italian": "it-IT"
        }

        self.setup_styles()
        self.create_widgets()

    def setup_styles(self):
        """Configures modern styling for the Tkinter elements."""
        self.style = ttk.Style()
        self.style.theme_use("clam")
        
        # Configure ComboBox dropdowns
        self.style.configure("TCombobox", fieldbackground="#f8fafc", background="#e2e8f0")
        
        # Configure custom button styles
        self.style.configure("Action.TButton", font=("Arial", 11, "bold"), background="#4f46e5", foreground="white")
        self.style.map("Action.TButton", background=[("active", "#4338ca"), ("disabled", "#94a3b8")])
        
        self.style.configure("Util.TButton", font=("Arial", 9), background="#e2e8f0", foreground="#334155")

    def create_widgets(self):
        """Constructs the application layout."""
        # --- Header ---
        header = tk.Label(self.root, text="🌐 Language Translator", font=("Arial", 18, "bold"), bg="#f1f5f9", fg="#1e293b")
        header.pack(pady=15)

        # --- Action Trigger Button (Packed bottom first to ensure visibility) ---
        self.translate_btn = ttk.Button(self.root, text="Translate Text →", style="Action.TButton", command=self.start_translation_thread)
        self.translate_btn.pack(side=tk.BOTTOM, fill=tk.X, padx=30, pady=20)

        # --- Main Workspace Grid ---
        main_frame = tk.Frame(self.root, bg="#f1f5f9")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20)

        # Left Column: Source Text
        left_frame = tk.Frame(main_frame, bg="#f1f5f9")
        left_frame.grid(row=0, column=0, sticky="nsew", padx=10)

        self.src_lang_var = tk.StringVar(value="English")
        self.src_lang_combo = ttk.Combobox(left_frame, textvariable=self.src_lang_var, values=list(self.languages.keys()), state="readonly", width=18, font=("Arial", 10))
        self.src_lang_combo.pack(anchor="w", pady=(0, 5))

        # Pack character count label first at the bottom to prevent it from getting hidden
        self.char_count_label = tk.Label(left_frame, text="0 / 500", font=("Arial", 9), bg="#f1f5f9", fg="#94a3b8")
        self.char_count_label.pack(side=tk.BOTTOM, anchor="e", pady=2)

        self.src_text = tk.Text(left_frame, wrap=tk.WORD, font=("Arial", 11), bg="#f8fafc", fg="#334155", bd=1, relief="solid", highlightthickness=0, height=8)
        self.src_text.pack(fill=tk.BOTH, expand=True)
        self.src_text.bind("<KeyRelease>", self.update_char_count)

        # Right Column: Target Text
        right_frame = tk.Frame(main_frame, bg="#f1f5f9")
        right_frame.grid(row=0, column=1, sticky="nsew", padx=10)

        self.tgt_lang_var = tk.StringVar(value="Spanish")
        self.tgt_lang_combo = ttk.Combobox(right_frame, textvariable=self.tgt_lang_var, values=list(self.languages.keys()), state="readonly", width=18, font=("Arial", 10))
        self.tgt_lang_combo.pack(anchor="w", pady=(0, 5))

        # Pack bottom utility bar FIRST to prevent it from getting hidden on window resize
        util_bar = tk.Frame(right_frame, bg="#f1f5f9")
        util_bar.pack(side=tk.BOTTOM, fill=tk.X, pady=2)

        self.copy_btn = ttk.Button(util_bar, text="📋 Copy", style="Util.TButton", command=self.copy_to_clipboard)
        self.copy_btn.pack(side=tk.LEFT)

        # Pack target text to fill remaining space
        self.tgt_text = tk.Text(right_frame, wrap=tk.WORD, font=("Arial", 11), bg="#f8fafc", fg="#334155", bd=1, relief="solid", highlightthickness=0, height=8)
        self.tgt_text.pack(fill=tk.BOTH, expand=True)

        # Equalize columns inside the grid layout
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)

    def update_char_count(self, event=None):
        """Updates the live counter monitoring input character limits."""
        length = len(self.src_text.get("1.0", "end-1c"))
        self.char_count_label.config(text=f"{length} / 500")

    def copy_to_clipboard(self):
        """Copies the generated translation to the system clipboard."""
        translated_text = self.tgt_text.get("1.0", "end-1c").strip()
        if translated_text and translated_text != "Translating...":
            try:
                self.root.clipboard_clear()
                self.root.clipboard_append(translated_text)
                self.copy_btn.config(text="✅ Copied!")
                self.root.after(2000, lambda: self.copy_btn.config(text="📋 Copy"))
            except Exception as e:
                messagebox.showerror("Error", f"Failed to copy to clipboard: {e}")

    def start_translation_thread(self):
        """Prevents the application window from freezing by processing the network request on a separate thread."""
        text_to_translate = self.src_text.get("1.0", "end-1c").strip()
        if not text_to_translate:
            return

        # Enforce API character limit before requesting
        if len(text_to_translate) > 500:
            messagebox.showwarning("Character Limit Exceeded", "Please limit your text to 500 characters for the free API tier.")
            return

        # Visual feedback during the request lifecycle
        self.translate_btn.config(state="disabled", text="Translating...")
        self.tgt_text.delete("1.0", tk.END)
        self.tgt_text.insert(tk.END, "Translating...")

        # Fire off network thread
        threading.Thread(target=self.execute_translation, args=(text_to_translate,), daemon=True).start()

    def execute_translation(self, text):
        """Handles HTTP Communication with the public translation API endpoint."""
        from_code = self.languages[self.src_lang_var.get()]
        to_code = self.languages[self.tgt_lang_var.get()]
        
        api_url = "https://api.mymemory.translated.net/get"
        params = {
            "q": text,
            "langpair": f"{from_code}|{to_code}"
        }

        try:
            response = requests.get(api_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            result = data["responseData"]["translatedText"]
        except Exception as e:
            result = f"Error: Unable to fetch translation.\n({str(e)})"

        # Safely pass data back to the primary UI thread
        self.root.after(0, self.finalize_ui, result)

    def finalize_ui(self, result_text):
        """Restores control hooks back to the main UI once API results land."""
        self.tgt_text.delete("1.0", tk.END)
        self.tgt_text.insert(tk.END, result_text)
        self.translate_btn.config(state="normal", text="Translate Text →")


if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslatorApp(root)
    root.mainloop()

