import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image
import os

# Constantes de la identidad corporativa
PRIMARY_COLOR = "#2B579A"      # Azul institucional
SECONDARY_COLOR = "#FFFFFF"    # Fondo blanco puro
BORDER_COLOR = "#E1E1E1"       # Gris neutro para bordes
ACCENT_COLOR = "#D83B01"       # Naranja de alerta
SUCCESS_COLOR = "#00B050"      # Verde para feedback de éxito

TITLE_FONT = ("Segoe UI Semibold", 16)
BODY_FONT = ("Segoe UI", 9)

# Extensiones de imagen consideradas
VALID_EXTENSIONS = [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]

class ImageConverterGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Conversor de Imágenes By J_Gabriel")
        self.configure(bg=SECONDARY_COLOR)
        self.geometry("700x410")
        self.source_formats = {}  # Diccionario para almacenar las extensiones detectadas y su variable asociada
        self.create_widgets()

    def create_widgets(self):
        # Cinta Superior: Barra de título con logo tipográfico
        top_frame = tk.Frame(self, bg=SECONDARY_COLOR)
        top_frame.pack(side="top", fill="x")
        title_label = tk.Label(top_frame, text="Conversor de Imágenes By J_Gabriel", font=TITLE_FONT, fg=PRIMARY_COLOR, bg=SECONDARY_COLOR)
        title_label.pack(pady=8)

        # Zona de Acción Principal
        main_frame = tk.Frame(self, bg=SECONDARY_COLOR)
        main_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Selección del directorio
        dir_label = tk.Label(main_frame, text="Seleccione el directorio de imágenes:", font=BODY_FONT, fg="black", bg=SECONDARY_COLOR)
        dir_label.pack(anchor="w", pady=(0, 5))
        self.dir_entry = tk.Entry(main_frame, font=BODY_FONT, bd=1, relief="solid", highlightthickness=1, highlightbackground=PRIMARY_COLOR)
        self.dir_entry.pack(fill="x", pady=(0, 5))
        browse_button = tk.Button(main_frame, text="Buscar Directorio", font=BODY_FONT, bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, relief="flat", bd=0, command=self.browse_directory)
        browse_button.pack(pady=(0, 10))
        browse_button.bind("<Enter>", lambda e: browse_button.config(relief="raised"))
        browse_button.bind("<Leave>", lambda e: browse_button.config(relief="flat"))

        # Panel para mostrar formatos existentes y selección de formatos a convertir
        formats_header_frame = tk.Frame(main_frame, bg=SECONDARY_COLOR)
        formats_header_frame.pack(fill="x", pady=(10, 0))
        
        formats_title = tk.Label(formats_header_frame, text="Formatos Detectados", font=BODY_FONT, fg=PRIMARY_COLOR, bg=SECONDARY_COLOR)
        formats_title.pack(side="left")
        
        # Creación del icono de actualización (usando Unicode para el símbolo de actualización)
        refresh_button = tk.Button(formats_header_frame, text="↻", font=("Segoe UI", 12, "bold"), 
                                  bg=SECONDARY_COLOR, fg=PRIMARY_COLOR, 
                                  relief="flat", bd=0, width=2, height=1,
                                  command=self.refresh_formats)
        refresh_button.pack(side="right")
        
        # Tooltip para el botón de actualización
        self.create_tooltip(refresh_button, "Actualizar formatos")
        
        # Efecto hover para el botón
        refresh_button.bind("<Enter>", lambda e: refresh_button.config(bg="#F0F0F0"))
        refresh_button.bind("<Leave>", lambda e: refresh_button.config(bg=SECONDARY_COLOR))
        
        # Marco para los formatos detectados
        formats_frame = tk.LabelFrame(main_frame, bd=1, relief="solid", bg=SECONDARY_COLOR)
        formats_frame.pack(fill="x", pady=(0, 10))
        
        self.formats_container = tk.Frame(formats_frame, bg=SECONDARY_COLOR)
        self.formats_container.pack(padx=10, pady=10, fill="x")

        # Opción para seleccionar el formato destino
        target_frame = tk.Frame(main_frame, bg=SECONDARY_COLOR)
        target_frame.pack(fill="x", pady=(10, 10))
        target_label = tk.Label(target_frame, text="Formato destino:", font=BODY_FONT, fg="black", bg=SECONDARY_COLOR)
        target_label.pack(side="left")
        self.target_format = tk.StringVar()
        self.target_format.set("PNG")
        target_options = ["PNG", "JPG", "BMP", "TIFF"]
        self.target_combo = ttk.Combobox(target_frame, textvariable=self.target_format, values=target_options, state="readonly", font=BODY_FONT)
        self.target_combo.pack(side="left", padx=10)

        # Opción para eliminar archivos originales
        self.delete_original = tk.BooleanVar()
        delete_check = tk.Checkbutton(main_frame, text="Eliminar archivos originales tras conversión", font=BODY_FONT, fg="black", bg=SECONDARY_COLOR, variable=self.delete_original)
        delete_check.pack(pady=(5, 10), anchor="w")

        # Botón para iniciar la conversión
        convert_button = tk.Button(main_frame, text="Convertir Imágenes", font=BODY_FONT, bg=PRIMARY_COLOR, fg=SECONDARY_COLOR, relief="flat", bd=0, command=self.convert_images)
        convert_button.pack(pady=(10, 10))
        convert_button.bind("<Enter>", lambda e: convert_button.config(relief="raised"))
        convert_button.bind("<Leave>", lambda e: convert_button.config(relief="flat"))

        # Área de Feedback de Estado
        self.status_label = tk.Label(self, text="", font=BODY_FONT, fg=ACCENT_COLOR, bg=SECONDARY_COLOR)
        self.status_label.pack(side="bottom", fill="x", pady=10)

    def create_tooltip(self, widget, text):
        """Crea un tooltip simple para un widget"""
        def enter(event):
            x, y, _, _ = widget.bbox("insert")
            x += widget.winfo_rootx() + 25
            y += widget.winfo_rooty() + 25
            
            # Crear ventana de tooltip
            self.tooltip = tk.Toplevel(widget)
            self.tooltip.wm_overrideredirect(True)
            self.tooltip.wm_geometry(f"+{x}+{y}")
            
            label = tk.Label(self.tooltip, text=text, font=BODY_FONT, bg="#FFFFCC", relief="solid", borderwidth=1)
            label.pack()
            
        def leave(event):
            if hasattr(self, "tooltip"):
                self.tooltip.destroy()
        
        widget.bind("<Enter>", enter)
        widget.bind("<Leave>", leave)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.dir_entry.delete(0, tk.END)
            self.dir_entry.insert(0, directory)
            # Una vez seleccionado el directorio, se analizan los formatos presentes
            self.analyze_formats(directory)

    def refresh_formats(self):
        directory = self.dir_entry.get()
        if not directory or not os.path.isdir(directory):
            messagebox.showerror("Error", "Seleccione un directorio válido primero.")
            return
        
        self.analyze_formats(directory)
        self.status_label.config(text="Formatos actualizados correctamente.", fg=SUCCESS_COLOR)

    def analyze_formats(self, directory):
        # Limpia el contenedor de formatos
        for widget in self.formats_container.winfo_children():
            widget.destroy()
        self.source_formats.clear()

        # Analiza el directorio y agrupa las extensiones encontradas
        files = os.listdir(directory)
        detected_formats = {}
        
        for filename in files:
            ext = os.path.splitext(filename)[1].lower()
            if ext in VALID_EXTENSIONS:
                if ext not in detected_formats:
                    # Crea una variable para este formato y la guarda en el diccionario
                    var = tk.BooleanVar(value=True)
                    detected_formats[ext] = var
        
        if not detected_formats:
            lbl = tk.Label(self.formats_container, text="No se han detectado formatos válidos.", font=BODY_FONT, fg="black", bg=SECONDARY_COLOR)
            lbl.pack(anchor="w")
            return

        # Crea un checkbox para cada formato detectado
        for ext in sorted(detected_formats.keys()):
            cb = tk.Checkbutton(self.formats_container, text=ext, font=BODY_FONT, fg="black", bg=SECONDARY_COLOR, variable=detected_formats[ext])
            cb.pack(anchor="w")
        
        # Guarda las referencias a las variables
        self.source_formats = detected_formats

    def convert_images(self):
        directory = self.dir_entry.get()
        if not os.path.isdir(directory):
            messagebox.showerror("Error", "El directorio especificado no es válido.")
            return

        # Obtiene las extensiones seleccionadas para la conversión
        selected_formats = [ext for ext, var in self.source_formats.items() if var.get()]
        if not selected_formats:
            messagebox.showinfo("Información", "No se han seleccionado formatos para la conversión.")
            return

        target_format = self.target_format.get().lower()
        target_ext = f".{target_format}"
        files = os.listdir(directory)
        converted_count = 0

        for filename in files:
            file_path = os.path.join(directory, filename)
            base_name, ext = os.path.splitext(filename)
            ext = ext.lower()
            
            # Verifica si este archivo debe procesarse
            if ext not in selected_formats:
                continue
                
            # Si el formato original y destino son iguales, no hay nada que hacer
            if ext == target_ext:
                continue
                
            try:
                new_filepath = os.path.join(directory, f"{base_name}{target_ext}")
                
                # Abre y guarda la imagen con el formato adecuado
                with Image.open(file_path) as img:
                    # Preserva el modo de color según el formato de destino
                    if target_format in ['png', 'tiff'] and img.mode in ['RGBA', 'LA']:
                        # Mantiene la transparencia para PNG y TIFF
                        img.save(new_filepath)
                    else:
                        # Convierte a RGB para JPG y otros formatos sin transparencia
                        img.convert("RGB").save(new_filepath)
                
                # Elimina el archivo original si se solicitó
                if self.delete_original.get():
                    os.remove(file_path)
                    
                converted_count += 1
                
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo convertir {filename}.\nError: {str(e)}")
                return

        # Muestra un mensaje único de éxito
        if converted_count > 0:
            self.status_label.config(text=f"Conversión completada: {converted_count} archivo(s) convertido(s).", fg=SUCCESS_COLOR)
            messagebox.showinfo("Éxito", f"Se han convertido {converted_count} archivo(s) al formato {target_format.upper()} correctamente.")
            
            # Actualiza automáticamente los formatos después de la conversión
            self.analyze_formats(directory)
        else:
            self.status_label.config(text="No se realizaron conversiones.", fg=ACCENT_COLOR)

if __name__ == "__main__":
    app = ImageConverterGUI()
    app.mainloop()
