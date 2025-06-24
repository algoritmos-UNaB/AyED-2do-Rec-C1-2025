#!/usr/bin/env python3
"""
Test para verificar exportación a archivos txt
"""

import sys
import os
import traceback


def test_txt_export():
    """Verifica que la función de exportación txt funcione correctamente"""
    try:
        from ejercicio1 import generar_bandas_aleatorias, exportar_bandas_a_txt
        
        # Generar bandas aleatorias
        bandas = generar_bandas_aleatorias()
        
        if not bandas or len(bandas) < 15:
            print("Test failed: not enough bands generated")
            return False
        
        # Exportar a txt
        exportar_bandas_a_txt(bandas)
        
        # Verificar que se crearon archivos txt
        archivos_txt_creados = []
        for banda in bandas[:3]:  # Verificar solo las primeras 3
            nombre_archivo = f"{banda.nombre.replace(' ', '_').replace('/', '_')}.txt"
            if os.path.exists(nombre_archivo):
                archivos_txt_creados.append(nombre_archivo)
                
                # Verificar contenido del archivo
                with open(nombre_archivo, 'r', encoding='utf-8') as f:
                    reader = txt.reader(f)
                    lines = list(reader)
                    
                    # Debe tener al menos header + algunas filas de datos
                    if len(lines) < 2:
                        print(f"Test failed: txt file {nombre_archivo} has insufficient data")
                        return False
        
        # Limpiar archivos de test
        for archivo in archivos_txt_creados:
            try:
                os.remove(archivo)
            except:
                pass
        
        # Verificar que se crearon al menos algunos archivos
        if len(archivos_txt_creados) >= 3:
            print("Test passed: txt export working")
            return True
        else:
            print(f"Test failed: only {len(archivos_txt_creados)} txt files created")
            return False
            
    except Exception as e:
        print(f"Test failed with exception: {str(e)}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_txt_export()
    sys.exit(0 if success else 1)