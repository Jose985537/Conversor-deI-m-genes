# Conversor de Imágenes By J_Gabriel

## Descripción
**Conversor de Imágenes** es una aplicación de escritorio desarrollada en Python que permite convertir imágenes entre diferentes formatos de manera rápida y sencilla. Diseñada con una interfaz gráfica intuitiva, esta herramienta facilita la conversión por lotes de múltiples archivos de imagen.

## Características
- Interfaz gráfica de usuario limpia e intuitiva
- Conversión entre formatos populares: JPG, PNG, BMP, TIFF
- Detección automática de formatos existentes en el directorio seleccionado
- Posibilidad de actualizar la lista de formatos detectados en tiempo real
- Opción para eliminar archivos originales después de la conversión
- Preservación de transparencia al convertir a formatos que la soportan (PNG, TIFF)
- Diseño visual acorde a estándares modernos

## Requisitos del sistema
- Python 3.6 o superior
- Bibliotecas requeridas:
  - tkinter (incluido en la mayoría de las instalaciones de Python)
  - Pillow (PIL Fork)

## Instalación

### 1. Clonar o descargar este repositorio

### 2. Instalar dependencias
```bash
pip install Pillow
```

### 3. Ejecutar la aplicación
```bash
python conversor_imagenes.py
```

## Guía de uso

1. **Selección de directorio**: 
   - Haga clic en "Buscar Directorio" para seleccionar la carpeta donde se encuentran las imágenes que desea convertir.
   - La aplicación analizará automáticamente los formatos de imagen existentes.

2. **Selección de formatos**: 
   - En la sección "Formatos Detectados" aparecerán todos los formatos de imagen encontrados.
   - Marque o desmarque las casillas para seleccionar qué formatos desea convertir.
   - Utilice el botón de actualización (↻) para refrescar la lista de formatos si ha añadido o eliminado archivos.

3. **Selección de formato destino**: 
   - Elija el formato al que desea convertir las imágenes utilizando el menú desplegable.

4. **Opciones adicionales**:
   - Marque "Eliminar archivos originales tras conversión" si desea que solo queden los archivos convertidos.

5. **Iniciar conversión**:
   - Haga clic en "Convertir Imágenes" para comenzar el proceso.
   - Una vez completado, se mostrará un mensaje con los resultados.
   - La lista de formatos se actualizará automáticamente para reflejar los cambios.

## Formatos soportados
- JPG/JPEG
- PNG
- BMP
- TIFF

## Notas técnicas
- Al convertir a formatos que soportan transparencia (PNG, TIFF), se preservará el canal alfa si existe.
- Al convertir a formatos sin soporte para transparencia (JPG), las imágenes se convertirán al modo RGB.
- La aplicación utiliza una interfaz acorde con estándares de diseño modernos, con colores institucionales para una experiencia visual coherente.

## Resolución de problemas

### La aplicación no inicia
- Verifique que tiene instalado Python 3.6 o superior
- Confirme que las dependencias están correctamente instaladas con `pip list`

### No se detectan imágenes
- Asegúrese de que las imágenes tengan las extensiones correctas (.jpg, .jpeg, .png, .bmp, .tiff)
- Utilice el botón de actualizar para refrescar la lista de formatos

### Error durante la conversión
- Verifique que las imágenes no estén corruptas o dañadas
- Asegúrese de tener permisos de escritura en el directorio seleccionado

## Licencia
Este proyecto está disponible como software de código abierto bajo la licencia MIT.

## Autor
Desarrollado por J_Gabriel

---

© 2025 Conversor de Imágenes. Todos los derechos reservados.
