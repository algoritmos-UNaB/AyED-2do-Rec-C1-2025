#!/usr/bin/env python3
"""
Test para verificar eliminación completa de competencias
"""

import sys
import traceback

def test_eliminar_competencia():
    """Verifica que eliminar_competencia elimine todas las instancias"""
    try:
        from ejercicio1 import Banda, PresentacionMusical
        
        # Crear múltiples bandas
        banda1 = Banda("Eliminators", ["Ana"], "Metal", "Rosario")
        banda2 = Banda("Removers", ["Carlos"], "Punk", "Mendoza")
        banda3 = Banda("Deleters", ["Luis"], "Rock", "Tucumán")
        
        # Crear presentaciones compartidas
        presentacion1 = PresentacionMusical(100, "Shared Event", "Big Arena", 600)
        presentacion2 = PresentacionMusical(200, "Another Event", "Small Club", 400)
        presentacion3 = PresentacionMusical(100, "Duplicate ID Event", "Stadium", 800)  # Mismo ID
        
        # Agregar presentaciones a las bandas
        banda1.presentaciones = [presentacion1, presentacion2, presentacion3]
        banda2.presentaciones = [presentacion1, presentacion3]
        banda3.presentaciones = [presentacion2]
        
        # Simular que todas las bandas están en las presentaciones
        presentacion1.bandas = [banda1, banda2]
        presentacion3.bandas = [banda1, banda2]
        
        # Contar presentaciones antes de eliminar
        total_before = len(banda1.presentaciones) + len(banda2.presentaciones) + len(banda3.presentaciones)
        
        # Eliminar todas las instancias con ID 100
        # Esto debería eliminar presentacion1 y presentacion3 de todas las bandas
        banda1.eliminar_competencia(100)
        
        # Contar después de eliminar
        total_after = len(banda1.presentaciones) + len(banda2.presentaciones) + len(banda3.presentaciones)
        
        # Verificar que se eliminaron las correctas
        # banda1: solo debería tener presentacion2
        # banda2: no debería tener ninguna (tenía solo ID 100)
        # banda3: debería seguir teniendo presentacion2
        
        expected_after = 2  # banda1(1) + banda2(0) + banda3(1)
        
        if total_after == expected_after and len(banda1.presentaciones) == 1 and len(banda2.presentaciones) == 0:
            print("Test passed: competition removal complete")
            return True
        else:
            print(f"Test failed: expected {expected_after} total presentations, got {total_after}")
            return False
            
    except Exception as e:
        print(f"Test failed with exception: {str(e)}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_eliminar_competencia()
    sys.exit(0 if success else 1)