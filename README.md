[![Category](https://img.shields.io/badge/Category-Productivity-blue.svg?style=flat-square)](https://github.com/topics/productivity)
[![Type](https://img.shields.io/badge/Type-Utility-green.svg?style=flat-square)](https://github.com/topics/utility)
[![Function](https://img.shields.io/badge/Function-Desktop_Organizer-orange.svg?style=flat-square)](https://github.com/topics/desktop-organizer)
[![Automation](https://img.shields.io/badge/Feature-Automation-red.svg?style=flat-square)](https://github.com/topics/automation)
[![Language](https://img.shields.io/badge/Language-Python-informational.svg?style=flat-square)](https://github.com/topics/python)
[![OS](https://img.shields.io/badge/OS-Windows%20%7C%20Linux-lightgrey.svg?style=flat-square)](https://github.com/topics/windows)
[![Project](https://img.shields.io/badge/Project-DeskMate-7D26CD.svg?style=flat-square)](https://github.com/D4rkh45h/DeskMate)
[![Developer](https://img.shields.io/badge/Developer-d4rkh45h-brightgreen.svg?style=flat-square)](https://github.com/d4rkh45h)

<div align="center">
  <div style="display: inline-flex; align-items: center; gap: 8px; margin-bottom: 25px; padding-top: 10px;">
    <a href="README.md" style="text-decoration: none; display: inline-flex; align-items: center; gap: 8px; margin-right: 8px;" title="Español">
      <img src="https://flagpedia.net/data/flags/w1600/es.png" alt="Español" width="36" style="vertical-align: middle;">
      <span style="color: white; font-size: 18px; font-weight: 600; font-family: sans-serif;">  Español</span>
    </a>
    <span style="color: grey; font-size: 18px; font-family: sans-serif; margin-right: 8px;">|</span>
    <a href="README.en.md" style="text-decoration: none; display: inline-flex; align-items: center; gap: 8px;" title="English">
      <img src="https://flagpedia.net/data/flags/w1600/us.png" alt="English" width="36" style="vertical-align: middle;">
      <span style="color: deepskyblue; font-size: 18px; font-family: sans-serif; text-decoration: underline;">  English</span>
    </a>
  </div>
</div>

# DeskMate 🚀

DeskMate es una herramienta diseñada para mantener tu escritorio organizado automáticamente. Clasifica y mueve archivos a carpetas predefinidas según su tipo, y registra todas estas acciones en un archivo de texto (log) para que siempre tengas un historial detallado de la organización de tu espacio de trabajo.

![Logo de la Herramienta](/Logo_DeskMate.png) 
<!-- Si no tienes un logo, puedes eliminar la línea anterior o usar un icono genérico. -->

<h2 align="center">Demostración</h2>

<p align="center">
  Aquí puedes ver la herramienta en acción a través de GIFs y capturas de pantalla.
</p>

### GIF de la Herramienta en Funcionamiento

<p align="center">
  <img src="gif1.gif" alt="Demostración en GIF" style="max-width: 100%; height: auto; display: block; margin: 0 auto;">
  <em>Una rápida demostración del flujo de trabajo principal de DeskMate, mostrando sus características clave.</em>
</p>

### Capturas de Pantalla Clave

<p align="center">
  <img src="foto1.png" alt="Captura de pantalla 1" style="max-width: 100%; height: auto; display: block; margin: 0 auto;">
  <em>Escritorio desordenado.</em>
</p>

<p align="center">
  <img src="foto2.png" alt="Captura de pantalla 2" style="max-width: 100%; height: auto; display: block; margin: 0 auto;">
  <em>Ejecutamos la herramienta para ordenar el escritorio.</em>
</p>

<p align="center">
  <img src="foto3.png" alt="Captura de pantalla 3" style="max-width: 100%; height: auto; display: block; margin: 0 auto;">
  <em>Una vez confirmada la ejecución de la herramienta veremos el escritorio ordenado.</em>
</p>

<p align="center">
  <img src="foto4.png" alt="Captura de pantalla 4" style="max-width: 100%; height: auto; display: block; margin: 0 auto;">
  <em>Logs generados por la herramienta.</em>
</p>

---
## 📝 Funcionamiento de DeskMate

El uso de DeskMate es directo y se centra en la interacción inicial para comenzar la organización de tu espacio digital.

1.  **Iniciar la Aplicación:**
    Ejecuta `DeskMate.py` (o `DeskMate.exe` si has generado el ejecutable) desde tu terminal o haciendo doble clic, según tu sistema.
    ```bash
    # Para ejecutar desde script Python
    python3 DeskMate.py
    ```

2.  **Confirmar Operación:**
    Al iniciar, la herramienta te solicitará **confirmación para proceder con los cambios**. Es crucial que aceptes para que DeskMate pueda comenzar su tarea de organización.

3.  **Resultado de la Organización:**
    Una vez confirmada la ejecución, DeskMate procederá a:
    *   **Clasificar tu Escritorio:** Moverá los archivos a sus respectivas carpetas predefinidas.
    *   **Generar Archivos de Registro:** Creará y actualizará los archivos de texto (`log`) que detallan todas las acciones realizadas, proporcionando un historial completo de la limpieza de tu escritorio.

De esta manera, tu escritorio quedará ordenado y tendrás un registro accesible de cada acción de organización.
---

## Características

*   **Organización Automática:** Clasifica y mueve archivos del escritorio a carpetas designadas según su tipo (ej., documentos, imágenes, ejecutables).
*   **Registro Detallado (Log):** Genera un archivo de texto (`log`) con el historial completo de todos los movimientos y acciones realizadas, permitiendo un seguimiento preciso.
*   **Compatibilidad:** Optimizada para entornos Windows x64.

## Estructura del Proyecto

Este repositorio contiene la herramienta **DeskMate** y sus archivos asociados.
```bash
DeskMate/
├── DeskMate.py
├── DeskMate.spec
├── README.md
└── README.en.md
```
---

## Documentación Adicional

Aquí encontrarás información más detallada sobre el proyecto:

*   🤝 [**Código de Conducta**](.github/CODIGO_DE_CONDUCTA.md) - Normas para una comunidad respetuosa.
*   📬 [**Cómo Contribuir**](.github/COMO_CONTRIBUIR.md) - Pasos para colaborar con el proyecto.
*   🔐 [**Seguridad**](.github/SEGURIDAD.md) - Información sobre cómo reportar vulnerabilidades.
*   ⚠️ [**Aviso Legal**](.github/AVISO_LEGAL.md) - Cláusulas y advertencias legales importantes.
*   📢 [**Soporte**](.github/SOPORTE.md) - Dónde obtener ayuda o hacer preguntas.

---

## 🚀 Guía Rápida de Uso e Instalación

```bash
# PASOS GENERALES PARA OBTENER EL PROYECTO
git clone https://github.com/D4rkh45h/DeskMate.git
cd DeskMate

# CONFIGURACIÓN DEL ENTORNO VIRTUAL (OPCIONAL, PERO RECOMENDADO)
# Para Windows:
# python -m venv venv
# .\venv\Scripts\activate
#
# Para Linux:
# python3 -m venv venv
# source venv/bin/activate

# --- OPCIONES DE EJECUCIÓN ---

# 🪟 PARA USUARIOS DE WINDOWS (x64):
# Instalación de PyInstaller y Generación del Ejecutable .exe
pip install pyinstaller
pyinstaller --clean --onefile --noconsole --version-file=version.txt --icon=deskmate.ico DeskMate.py
# El ejecutable compilado estará disponible en: DeskMate/dist/DeskMate/DeskMate.exe

# 🐧 PARA USUARIOS DE LINUX:
# Instalación de Dependencias y Ejecución del Script
pip install -r requirements.txt
python3 DeskMate.py
