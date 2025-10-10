import os
import shutil
import datetime

def organizar_escritorio():
    escritorio_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    
    # Archivo para el registro de acciones
    log_file_path = os.path.join(escritorio_path, "organizacion_escritorio.log")
    
    def log_message(message):
        """Escribe un mensaje en la consola y en el archivo de log."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_message = f"[{timestamp}] {message}"
        print(full_message)
        with open(log_file_path, "a", encoding="utf-8") as f:
            f.write(full_message + "\n")

    log_message(f"Iniciando escaneo del escritorio: {escritorio_path}")

    # --- Configuración de categorías ---
    categorias = {
        "Imágenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
        "Documentos": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".csv", ".xlsx", ".pptx", ".ppt"],
        "Ejecutables": [".exe", ".msi", ".dmg", ".appimage"],
        "Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Audio": [".mp3", ".wav", ".aac", ".flac"],
        "Video": [".mp4", ".mov", ".avi", ".mkv", ".flv"],
        "Programación": [".py", ".html", ".css", ".js", ".java", ".c", ".cpp", ".php", ".json", ".xml"],
    }

    # --- Archivos/Carpetas a excluir del movimiento ---
    # Puedes añadir nombres de archivos o carpetas que no quieras que el script toque.
    # Por ejemplo: ["MiCarpetaImportante", "mi_proyecto.zip"]
    excluir_elementos = ["organizacion_escritorio.log", "organizacion_escritorio.py"] 
    # Aseguramos que el propio script y su log no se muevan.

    # Diccionario para almacenar los archivos que irán a cada categoría, incluyendo "Otros"
    archivos_por_categoria = {cat: [] for cat in categorias}
    archivos_por_categoria["Otros"] = []

    # --- Identificar archivos a mover ---
    archivos_en_escritorio = os.listdir(escritorio_path)
    elementos_a_procesar = []

    for nombre_elemento in archivos_en_escritorio:
        ruta_completa_elemento = os.path.join(escritorio_path, nombre_elemento)

        # Excluir elementos definidos y carpetas de destino existentes
        if nombre_elemento in excluir_elementos:
            log_message(f"Excluyendo '{nombre_elemento}' por lista de exclusión.")
            continue
        if os.path.isdir(ruta_completa_elemento) and nombre_elemento in categorias: # Las carpetas de destino no se mueven
             log_message(f"Excluyendo carpeta de categoría '{nombre_elemento}'.")
             continue
        if os.path.isdir(ruta_completa_elemento) and nombre_elemento == "Otros": # Excluir carpeta "Otros"
            log_message(f"Excluyendo carpeta de 'Otros'.")
            continue
        
        if os.path.isfile(ruta_completa_elemento):
            elementos_a_procesar.append(nombre_elemento)
        else:
            log_message(f"Ignorando carpeta no categorizada: '{nombre_elemento}'")


    for nombre_archivo in elementos_a_procesar:
        _, extension = os.path.splitext(nombre_archivo)
        extension = extension.lower()

        asignado = False
        for categoria, extensiones_asociadas in categorias.items():
            if extension in extensiones_asociadas:
                archivos_por_categoria[categoria].append(nombre_archivo)
                asignado = True
                break
        
        if not asignado:
            archivos_por_categoria["Otros"].append(nombre_archivo)

    # --- Mostrar resumen y pedir confirmación ---
    log_message("\nResumen de la organización propuesta:")
    hay_movimientos = False
    for categoria, lista_archivos in archivos_por_categoria.items():
        if lista_archivos:
            log_message(f"  - '{categoria}': {len(lista_archivos)} archivo(s)")
            hay_movimientos = True
        else:
            log_message(f"  - '{categoria}': No se moverán archivos (la carpeta no se creará).")

    if not hay_movimientos:
        log_message("No hay archivos para organizar en el escritorio. Organización cancelada.")
        return

    confirmacion = input("\n¿Deseas proceder con la organización? (s/n): ").lower()
    if confirmacion != 's':
        log_message("Organización cancelada por el usuario.")
        return

    # --- Crear carpetas y mover archivos ---
    log_message("\nProcediendo con el movimiento de archivos...")
    for categoria, lista_archivos in archivos_por_categoria.items():
        if lista_archivos: # Si hay archivos para esta categoría
            carpeta_destino = os.path.join(escritorio_path, categoria)
            
            try:
                if not os.path.exists(carpeta_destino):
                    os.makedirs(carpeta_destino)
                    log_message(f"Carpeta creada: {carpeta_destino}")
            except OSError as e:
                log_message(f"Error al crear la carpeta '{categoria}': {e}")
                continue # No podemos mover archivos si la carpeta no se crea

            for nombre_archivo in lista_archivos:
                ruta_completa_archivo = os.path.join(escritorio_path, nombre_archivo)
                destino_archivo = os.path.join(carpeta_destino, nombre_archivo)

                # Maneja el caso de que el archivo ya exista en la carpeta de destino
                if os.path.exists(destino_archivo):
                    base, ext = os.path.splitext(nombre_archivo)
                    contador = 1
                    while os.path.exists(os.path.join(carpeta_destino, f"{base}_{contador}{ext}")):
                        contador += 1
                    destino_archivo = os.path.join(carpeta_destino, f"{base}_{contador}{ext}")
                    log_message(f"El archivo '{nombre_archivo}' ya existe en '{categoria}', renombrando a '{os.path.basename(destino_archivo)}'")

                try:
                    shutil.move(ruta_completa_archivo, destino_archivo)
                    log_message(f"Movido: '{nombre_archivo}' a '{categoria}'")
                except PermissionError:
                    log_message(f"Error: Permiso denegado al mover '{nombre_archivo}'. Asegúrate de tener los permisos necesarios.")
                except FileNotFoundError:
                    log_message(f"Error: El archivo '{nombre_archivo}' no se encontró. Pudo haber sido movido o eliminado por otro proceso.")
                except Exception as e:
                    log_message(f"Error inesperado al mover '{nombre_archivo}': {e}")
        else:
            log_message(f"No hay archivos para la categoría '{categoria}', no se crea la carpeta.")

    log_message("\nOrganización completada.")

if __name__ == "__main__":
    organizar_escritorio()