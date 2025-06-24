#!/usr/bin/env python3
"""
Script de Detección Anti-IA para GitHub Classroom
Analiza patrones en código Python que pueden indicar uso de IA generativa
Autor: Sistema de Integridad Académica
Versión: 2.0 - Examen Concurso Bandas de Rock
"""

import sys
import re
import ast
import os
from datetime import datetime

class AntiAIDetector:
    def __init__(self):
        self.suspicious_patterns = 0
        self.ai_indicators = []
        self.confidence_score = 0
        
        # Patrones típicos de código generado por ChatGPT/Copilot
        self.ai_signatures = {
            'docstring_patterns': [
                r'"""[\s\S]*Args:[\s\S]*Returns:[\s\S]*"""',
                r'"""[\s\S]*Parameters:[\s\S]*Returns:[\s\S]*"""',
                r'"""[\s\S]*:param[\s\S]*:return[\s\S]*"""',
                r'"""[\s\S]*Note:[\s\S]*Example:[\s\S]*"""'
            ],
            'comment_patterns': [
                r'# This function does',
                r'# Initialize.*variables?',
                r'# Check if.*is valid',
                r'# Return.*result',
                r'# TODO:.*implement',
                r'# Example usage:',
                r'# Helper function to',
                r'# Note:.*important'
            ],
            'variable_patterns': [
                r'temp_variable_\d+',
                r'temporary_.*_holder',
                r'placeholder_.*',
                r'example_.*_data',
                r'sample_.*_input'
            ],
            'import_patterns': [
                'from typing import',
                'import typing',
                'from dataclasses import dataclass',
                'from abc import ABC, abstractmethod',
                'import logging'
            ],
            'structure_patterns': [
                r'if __name__ == "__main__":',
                r'def main\(\):',
                r'try:[\s\S]*except Exception as e:',
                r'raise NotImplementedError',
                r'pass  # TODO'
            ]
        }
        
        # Nombres extremadamente descriptivos (típicos de IA)
        self.excessive_verbosity = [
            r'calculate_.*_based_on_.*',
            r'get_.*_from_.*_using_.*',
            r'process_.*_and_return_.*',
            r'initialize_.*_with_default_.*',
            r'validate_.*_input_parameters',
            r'convert_.*_to_.*_format',
            r'generate_.*_random_.*_data'
        ]
        
        # Patrones de manejo de errores excesivamente robustos
        self.robust_error_handling = [
            'except (ValueError, TypeError, AttributeError)',
            'except Exception as exc:',
            'logging.error',
            'logging.warning',
            'sys.stderr.write'
        ]

    def analyze_file(self, file_path):
        """Analiza un archivo Python en busca de patrones de IA"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            return self._analyze_content(content, file_path)
        except Exception as e:
            return {"error": f"Error analyzing file: {str(e)}"}

    def _analyze_content(self, content, file_path):
        """Análisis detallado del contenido del archivo"""
        lines = content.split('\n')
        
        # Análisis de patrones sospechosos
        self._check_docstring_patterns(content)
        self._check_comment_patterns(content)
        self._check_variable_naming(content)
        self._check_import_patterns(content)
        self._check_structure_patterns(content)
        self._check_verbosity_patterns(content)
        self._check_error_handling(content)
        self._check_code_quality_indicators(content)
        
        # Análisis específico para el contexto del examen
        self._check_exam_specific_patterns(content)
        
        # Calcular puntuación de confianza
        self._calculate_confidence_score()
        
        return {
            "file": file_path,
            "suspicious_patterns": self.suspicious_patterns,
            "ai_indicators": self.ai_indicators,
            "confidence_score": self.confidence_score,
            "timestamp": datetime.now().isoformat()
        }

    def _check_docstring_patterns(self, content):
        """Detecta docstrings excesivamente formales"""
        for pattern in self.ai_signatures['docstring_patterns']:
            matches = re.findall(pattern, content, re.MULTILINE)
            if matches:
                self.suspicious_patterns += len(matches) * 3
                self.ai_indicators.append(f"Formal docstring pattern detected: {len(matches)} instances")

    def _check_comment_patterns(self, content):
        """Detecta comentarios típicos de IA"""
        for pattern in self.ai_signatures['comment_patterns']:
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                self.suspicious_patterns += len(matches) * 2
                self.ai_indicators.append(f"AI-typical comment: '{pattern}' found {len(matches)} times")

    def _check_variable_naming(self, content):
        """Detecta nombres de variables sospechosos"""
        all_patterns = self.ai_signatures['variable_patterns'] + self.excessive_verbosity
        for pattern in all_patterns:
            matches = re.findall(pattern, content)
            if matches:
                self.suspicious_patterns += len(matches) * 2
                self.ai_indicators.append(f"Suspicious variable naming: {matches}")

    def _check_import_patterns(self, content):
        """Detecta imports no típicos del nivel del curso"""
        for pattern in self.ai_signatures['import_patterns']:
            if pattern in content:
                self.suspicious_patterns += 4
                self.ai_indicators.append(f"Advanced import detected: {pattern}")

    def _check_structure_patterns(self, content):
        """Detecta estructuras de código típicas de IA"""
        for pattern in self.ai_signatures['structure_patterns']:
            matches = re.findall(pattern, content, re.MULTILINE)
            if matches:
                self.suspicious_patterns += len(matches) * 3
                self.ai_indicators.append(f"AI structure pattern: {pattern}")

    def _check_verbosity_patterns(self, content):
        """Detecta verbosidad excesiva en nombres"""
        for pattern in self.excessive_verbosity:
            matches = re.findall(pattern, content)
            if matches:
                self.suspicious_patterns += len(matches) * 3
                self.ai_indicators.append(f"Excessive verbosity: {matches}")

    def _check_error_handling(self, content):
        """Detecta manejo de errores demasiado robusto"""
        for pattern in self.robust_error_handling:
            if pattern in content:
                self.suspicious_patterns += 3
                self.ai_indicators.append(f"Overly robust error handling: {pattern}")

    def _check_code_quality_indicators(self, content):
        """Detecta indicadores de calidad de código inusual para estudiantes"""
        # Type hints excesivos
        type_hints = re.findall(r':\s*[A-Z][a-zA-Z]*\[.*\]', content)
        if len(type_hints) > 5:
            self.suspicious_patterns += len(type_hints)
            self.ai_indicators.append(f"Excessive type hints: {len(type_hints)} found")
        
        # F-strings muy complejos
        complex_fstrings = re.findall(r'f["\'].*\{.*:.*\}.*["\']', content)
        if len(complex_fstrings) > 3:
            self.suspicious_patterns += len(complex_fstrings) * 2
            self.ai_indicators.append(f"Complex f-strings: {len(complex_fstrings)} found")

    def _check_exam_specific_patterns(self, content):
        """Detecta patrones específicos que serían raros en este examen"""
        exam_suspicious = [
            r'@property',
            r'@staticmethod', 
            r'@classmethod',
            r'lambda\s+.*:',
            r'list\(map\(',
            r'list\(filter\(',
            r'\.join\(',
            r'enumerate\(',
            r'zip\(',
            r'collections\.',
            r'itertools\.',
            r'functools\.'
        ]
        
        for pattern in exam_suspicious:
            matches = re.findall(pattern, content)
            if matches:
                self.suspicious_patterns += len(matches) * 4
                self.ai_indicators.append(f"Advanced Python feature: {pattern} ({len(matches)} times)")

    def _calculate_confidence_score(self):
        """Calcula la puntuación de confianza de detección de IA"""
        if self.suspicious_patterns == 0:
            self.confidence_score = 0
        elif self.suspicious_patterns <= 5:
            self.confidence_score = 1
        elif self.suspicious_patterns <= 15:
            self.confidence_score = 2
        elif self.suspicious_patterns <= 30:
            self.confidence_score = 3
        else:
            self.confidence_score = 4

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 anti_ai_detector.py <python_file>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"AI_DETECTION_SCORE: ERROR - File not found: {file_path}")
        sys.exit(1)
    
    detector = AntiAIDetector()
    result = detector.analyze_file(file_path)
    
    if "error" in result:
        print(f"AI_DETECTION_SCORE: ERROR - {result['error']}")
        sys.exit(1)
    
    # Output esperado por el test
    print(f"AI_DETECTION_SCORE: {result['confidence_score']}")
    
    # Log detallado para el profesor (si es necesario)
    if result['confidence_score'] > 0:
        print(f"# SUSPICIOUS_PATTERNS: {result['suspicious_patterns']}")
        for indicator in result['ai_indicators'][:5]:  # Mostrar solo los primeros 5
            print(f"# {indicator}")

if __name__ == "__main__":
    main()