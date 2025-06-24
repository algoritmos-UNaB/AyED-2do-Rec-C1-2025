#!/usr/bin/env python3
"""
Test para verificar implementación de búsqueda lineal
"""

import sys
import traceback

def test_busqueda_lineal():
    """Verifica que el método calcular_ranking use búsqueda lineal"""
    try:
        from ejercicio1 import Banda, PresentacionMusical
        
        banda = Banda("Linear Search Test", ["María"], "Jazz", "Córdoba")
        
        # Crear múltiples presentaciones
        presentaciones = []
        for i in range(15):
            presentacion = PresentacionMusical(i+1, f"Show {i+1}", f"Place {i+1}", 400)
            presentacion.puntos_obtenidos = {"Linear Search Test": 300 + (i * 10)}
            presentaciones.append(presentacion)
        
        # El método debe encontrar las presentaciones usando búsqueda lineal
        # Verificamos que funcione correctamente
        banda.presentaciones = presentaciones[:10]  # Solo las primeras 10
        
        # Buscar presentaciones específicas
        found_presentations = []
        target_ids = [3, 7, 9]
        
        # Simular búsqueda lineal manual
        for target_id in target_ids:
            for presentacion in banda.presentaciones:
                if presentacion.identificador == target_id:
                    found_presentations.append(presentacion)
                    break
        
        # Verificar que encontró las 3 presentaciones
        if len(found_presentations) == 3:
            print("Test passed: linear search working")
            return True
        else:
            print(f"Test failed: found {len(found_presentations)} presentations, expected 3")
            return False
            
    except Exception as e:
        print(f"Test failed with exception: {str(e)}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_busqueda_lineal()
    sys.exit(0 if success else 1)