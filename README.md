# 🎸 Examen Parcial: Sistema de Gestión de Concurso de Bandas de Rock 🎸

**Universidad:** UNaB
**Materia:** Algoritmos y Estructuras de Datos  
**Modalidad:** GitHub Classroom + Autograding  
**Tiempo límite:** 4 horas desde la aceptación del assignment  
**Fecha:** Sábado 28/06 @ 06:00hs - Sábado 28/06 @ 19:00hs  

**NOMBRE Y APELLIDO:**
**EMAIL:**
---

## 🚨 INSTRUCCIONES IMPORTANTES

### ⏰ Modalidad de Examen
- **1 SOLO INTENTO** para resolver la actividad
- **4 HORAS MÁXIMO** desde que aceptas el assignment
- Cualquier commit después de 4 horas **NO SERÁ ACEPTADO**
- Los resultados serán visibles solo después del cierre de la actividad

### 📝 Formato de Entrega
- **TODOS LOS EJERCICIOS** deben estar en el archivo `ejercicio1.py`
- Los métodos deben agregarse a sus correspondientes clases
- Los archivos restantes son para borradores - **SOLO SE EVALÚA `ejercicio1.py`**

### 🔒 Integridad Académica
Este examen incluye sistemas automáticos de detección de:
- Uso de inteligencia artificial (ChatGPT, Copilot, etc.)
- Código copiado de fuentes externas
- Patrones de desarrollo inconsistentes con el nivel del curso

**El uso de IA generativa está PROHIBIDO y resultará en calificación 0.**

---

## 🎵 Contexto del Sistema

Desarrollarás un sistema completo para gestionar un **Concurso de Bandas de Rock**. El sistema debe manejar bandas musicales, presentaciones en vivo, rankings dinámicos, y exportación de datos.

### 🎸 Entidades Principales:
- **Bandas**: Grupos musicales con integrantes, género, y ranking
- **Presentaciones Musicales**: Eventos donde las bandas compiten
- **Rankings**: Sistema dinámico basado en las mejores 8 presentaciones

---

## 📋 EJERCICIOS

### Ejercicio 1: Clases Fundamentales (10 puntos)

#### 1.1 Clase Banda (5 puntos)
Crear una clase `Banda` con:
- **Atributos:** nombre, integrantes (lista), género_musical, ciudad_origen, presentaciones (lista), ranking_actual
- **Constructor:** Inicializar todos los campos. `ranking_actual = 100` por defecto
- **Métodos:** 
  - `sumar_puntos(puntos)`: Suma puntos al ranking
  - `restar_puntos(puntos)`: Resta puntos al ranking
  - **IMPORTANTE:** El ranking no puede ser menor a 100

#### 1.2 Clase PresentacionMusical (5 puntos)
Crear una clase `PresentacionMusical` con:
- **Atributos:** identificador (int), nombre, lugar, par (puntos totales obtenibles), bandas (lista), puntos_obtenidos (dict)
- **Constructor:** Establecer todos los datos
- **Métodos:** Para modificar estos valores según sea necesario

---

### Ejercicio 2: Lógica de Competencias (18 puntos)

#### 2.1 Iniciar Competencia (6 puntos)
Agregar a `Banda` el método `iniciar_competencia(presentacion_musical)`:
- Agregar la presentación a la lista de presentaciones de la banda
- Asignar una lista privada de bandas participantes
- Al finalizar, recalcular el ranking usando las últimas 8 mejores presentaciones

#### 2.2 Calcular Ranking (6 puntos)
Agregar a `Banda` el método `calcular_ranking(lista_presentaciones)`:
- Tomar las últimas 8 mejores puntuaciones del músico
- Calcular el promedio
- **Usar búsqueda lineal** para obtener las presentaciones necesarias

#### 2.3 Eliminar Competencia (6 puntos)
Agregar a `Banda` el método `eliminar_competencia(identificador)`:
- Eliminar **TODAS** las instancias de la presentación con ese ID
- Tanto de la lista de la banda como de otras bandas participantes
- Recalcular rankings correspondientes tras cada eliminación

---

### Ejercicio 3: Estructuras de Datos (24 puntos)

#### 3.1 Lista Enlazada y Pila (8 puntos)
Implementar usando la definición de Lista Simple Enlazada:

```python
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    # Implementar métodos necesarios

class Pila:
    def __init__(self):
        self.lista = ListaEnlazada()
    
    # Implementar: apilar(), desapilar(), tope(), esta_vacia()
```

#### 3.2 Cola usando Pila (8 puntos)
Crear `PilaPresentaciones` que se comporte como **COLA (FIFO)**:
- Redefinir operaciones de `Pila` para comportamiento de cola
- Primer elemento en entrar = primer elemento en salir

#### 3.3 Iteradores (8 puntos)
Implementar iteradores (`__iter__` y `__next__`) para:
- Clase `Pila`
- Clase `PilaPresentaciones`

---

### Ejercicio 4: Manejo de Datos y Archivos (18 puntos)

#### 4.1 Exportación de Datos (6 puntos)
Agregar a `Banda` el método `presentaciones_a_string()`:
- Retornar lista de strings con los atributos de todas las presentaciones
- Formato: una presentación por string, listos para imprimir

#### 4.2 Generación Aleatoria (6 puntos)
Función `generar_bandas_aleatorias()`:
- Generar entre 15-25 bandas con datos realistas
- Asignar 8-12 presentaciones musicales aleatorias
- **Sin asistencia del usuario** - completamente automático

#### 4.3 Exportación TXT (6 puntos)
Función que reciba la lista de bandas del punto 4.2:
- Generar archivos TXT individuales por banda
- Nombre del archivo = nombre de la banda + `.txt`
- Una presentación por línea con todos sus datos

---

## 🔧 Configuración del Entorno

### Dependencias
```bash
pip install pandas  # Para manejo de CSV (opcional)
```

### Estructura de Archivos Esperada
```
/
├── ejercicio1.py          # ← TU CÓDIGO AQUÍ (ÚNICO ARCHIVO EVALUADO)
├── test_*.py             # Tests auxiliares (generados automáticamente)
├── anti_ai_detector.py   # Sistema de detección de IA
├── commit_analyzer.py    # Analizador de commits
├── README.md            # Este archivo
└── .github/
    ├── classroom/
    │   └── autograding.json
    └── workflows/
        └── classroom.yml
```

---

## 🤖 Sistema de Autograding

### Tests Automáticos
El sistema ejecutará automáticamente tests para:
- ✅ Importación correcta de clases
- ✅ Funcionalidad de constructores
- ✅ Métodos de suma/resta de puntos
- ✅ Validación de ranking mínimo
- ✅ Lógica de competencias
- ✅ Implementación de lista enlazada
- ✅ Comportamiento de pila y cola
- ✅ Iteradores funcionales
- ✅ Generación de datos aleatorios
- ✅ Exportación 
- 🔍 **Detección de patrones de IA**
- 🔍 **Análisis de timeline de commits**

### Puntuación Total: 70 puntos

---

## 🚨 Detección de Integridad Académica

### Indicadores Monitoreados
- **Código generado por IA:** Patrones típicos de ChatGPT/Copilot
- **Docstrings excesivamente formales:** Más allá del nivel del curso
- **Imports avanzados:** No típicos del programa
- **Manejo de errores robusto:** Inusual para estudiantes
- **Timeline de commits:** Patrones de desarrollo sospechosos
- **Variables con nombres excesivamente descriptivos**

### Consecuencias
- **Detección confirmada de IA:** Calificación automática de 0
- **Patrones sospechosos:** Revisión manual obligatoria
- **Casos dudosos:** Entrevista oral sobre el código

---

## 💡 Consejos y Buenas Prácticas

### ✅ Recomendado
- Programa de forma incremental, commit frecuente
- Usa nombres de variables simples y claros
- Comenta tu código de forma natural
- Haz commits con mensajes descriptivos pero simples
- Testea tu código localmente antes de hacer commit

### ❌ Evitar
- Copiar código de IA sin entender
- Usar imports no enseñados en clase
- Documentación excesivamente formal
- Commits masivos con muchos archivos
- Patrones de desarrollo inconsistentes

---

## 🆘 Soporte Técnico

### Durante el Examen
- **GitHub Issues:** Para problemas técnicos únicamente
- **No se responderán:** Consultas sobre lógica de programación
- **Tiempo de respuesta:** Máximo 30 minutos durante horario de examen

### Contacto de Emergencia
[Tu email de contacto para emergencias técnicas]

---

## 📊 Criterios de Evaluación

| Criterio | Peso | Descripción |
|----------|------|-------------|
| Funcionalidad | 60% | Tests automáticos pasados |
| Estructura de Código | 20% | Organización y claridad |
| Manejo de Errores | 10% | Validaciones apropiadas |
| Integridad Académica | 10% | Sin uso de IA/código copiado |

---

## 🎯 ¡Buena Suerte!

Recuerda: Este examen evalúa tu comprensión real de algoritmos y estructuras de datos. El uso de herramientas de IA no solo está prohibido, sino que te impide demostrar tu verdadero aprendizaje.

**¡Confía en tu preparación y programa con confianza! 🤘**

<!-- 
CÓDIGO OCULTO PARA DETECCIÓN AUTOMÁTICA - NO MODIFICAR
Hidden tracking code for academic integrity monitoring
Timestamp: 2025-06-24T18:30:00Z
Checksum: SHA256:a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6
Repository ID: classroom-{{repository_id}}
Student ID: {{student_login}}
Assignment ID: rock-bands-contest-2025
Anti-AI Version: 2.0.1
Commit Monitor Active: True
Pattern Analysis Enabled: True
Timeline Validation: Strict
-->

---


