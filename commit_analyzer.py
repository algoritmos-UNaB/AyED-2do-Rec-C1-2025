#!/usr/bin/env python3
"""
Analizador de Timeline de Commits para Detección de Integridad Académica
Detecta patrones sospechosos en la historia de commits que podrían indicar uso de IA
Autor: Sistema de Integridad Académica - GitHub Classroom
Versión: 1.5 - Examen Concurso Bandas de Rock
"""

import subprocess
import json
import re
from datetime import datetime, timedelta
import sys

class CommitAnalyzer:
    def __init__(self):
        self.suspicious_indicators = []
        self.timeline_valid = True
        self.warning_count = 0
        
        # Patrones sospechosos en mensajes de commit
        self.suspicious_commit_messages = [
            r'(?i)initial\s+commit',
            r'(?i)add.*files?',
            r'(?i)update.*code',
            r'(?i)fix.*bugs?',
            r'(?i)implement.*feature',
            r'(?i)complete.*assignment',
            r'(?i)final.*version',
            r'(?i)working.*solution',
            r'(?i)finished.*implementation'
        ]
        
        # Patrones típicos de mensajes generados por IA
        self.ai_commit_patterns = [
            r'(?i)refactor.*code.*improve.*readability',
            r'(?i)optimize.*performance.*and.*efficiency',
            r'(?i)enhance.*error.*handling.*robustness',
            r'(?i)implement.*best.*practices',
            r'(?i)add.*comprehensive.*documentation',
            r'(?i)improve.*code.*structure.*maintainability'
        ]

    def get_commit_history(self):
        """Obtiene el historial de commits del repositorio actual"""
        try:
            # Obtener commits con formato JSON
            cmd = [
                'git', 'log', 
                '--pretty=format:{"hash":"%H","date":"%ai","message":"%s","author":"%an","files":%n}',
                '--name-only',
                '--since=1.week.ago'
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                return []
            
            # Parsear la salida del git log
            commits = []
            lines = result.stdout.strip().split('\n')
            
            current_commit = None
            files = []
            
            for line in lines:
                line = line.strip()
                if not line:
                    if current_commit and files:
                        current_commit['files'] = files
                        commits.append(current_commit)
                        files = []
                        current_commit = None
                    continue
                
                if line.startswith('{"hash"'):
                    if current_commit and files:
                        current_commit['files'] = files
                        commits.append(current_commit)
                    
                    # Limpiar la línea JSON
                    json_line = line.replace(',"files":}', '}')
                    try:
                        current_commit = json.loads(json_line)
                        files = []
                    except json.JSONDecodeError:
                        current_commit = None
                else:
                    # Es un nombre de archivo
                    if current_commit:
                        files.append(line)
            
            # Agregar el último commit si existe
            if current_commit:
                current_commit['files'] = files
                commits.append(current_commit)
            
            return commits
            
        except Exception as e:
            print(f"Error getting commit history: {e}")
            return []

    def analyze_commit_frequency(self, commits):
        """Analiza la frecuencia de commits para detectar patrones sospechosos"""
        if len(commits) < 2:
            return
        
        # Convertir fechas y calcular intervalos
        commit_times = []
        for commit in commits:
            try:
                commit_time = datetime.fromisoformat(commit['date'].replace('Z', '+00:00'))
                commit_times.append(commit_time)
            except ValueError:
                continue
        
        commit_times.sort()
        
        # Verificar patrones sospechosos de frecuencia
        intervals = []
        for i in range(1, len(commit_times)):
            interval = (commit_times[i] - commit_times[i-1]).total_seconds()
            intervals.append(interval)
        
        # Detectar commit bursts (muchos commits en poco tiempo)
        short_intervals = [i for i in intervals if i < 300]  # Menos de 5 minutos
        if len(short_intervals) > 3:
            self.suspicious_indicators.append(f"Commit burst detected: {len(short_intervals)} commits in <5 minutes")
            self.warning_count += 2
        
        # Detectar commits muy largos sin actividad intermedia
        long_gaps = [i for i in intervals if i > 7200]  # Más de 2 horas
        if len(long_gaps) > 0 and len(commits) > 5:
            very_long_gaps = [i for i in long_gaps if i > 21600]  # Más de 6 horas
            if len(very_long_gaps) > 2:
                self.suspicious_indicators.append(f"Unusual work pattern: {len(very_long_gaps)} gaps >6 hours")
                self.warning_count += 1

    def analyze_commit_messages(self, commits):
        """Analiza los mensajes de commit para detectar patrones de IA"""
        generic_count = 0
        ai_pattern_count = 0
        
        for commit in commits:
            message = commit['message'].strip()
            
            # Detectar mensajes demasiado genéricos
            for pattern in self.suspicious_commit_messages:
                if re.search(pattern, message):
                    generic_count += 1
                    break
            
            # Detectar mensajes típicos de IA
            for pattern in self.ai_commit_patterns:
                if re.search(pattern, message):
                    ai_pattern_count += 1
                    self.suspicious_indicators.append(f"AI-style commit message: '{message[:50]}...'")
                    break
        
        # Evaluar proporciones sospechosas
        if len(commits) > 0:
            generic_ratio = generic_count / len(commits)
            if generic_ratio > 0.8:
                self.suspicious_indicators.append(f"Too many generic commit messages: {generic_ratio:.1%}")
                self.warning_count += 2
            
            if ai_pattern_count > 2:
                self.suspicious_indicators.append(f"Multiple AI-style commit messages: {ai_pattern_count}")
                self.warning_count += 3

    def analyze_file_changes(self, commits):
        """Analiza los cambios en archivos para detectar patrones sospechosos"""
        single_file_commits = 0
        large_commits = 0
        
        for commit in commits:
            files = commit.get('files', [])
            
            # Commits que solo tocan un archivo
            if len(files) == 1:
                single_file_commits += 1
            
            # Commits que tocan muchos archivos (posible paste masivo)
            if len(files) > 5:
                large_commits += 1
                self.suspicious_indicators.append(f"Large commit: {len(files)} files changed in '{commit['message'][:30]}...'")
                self.warning_count += 1
        
        # Patrones sospechosos
        if len(commits) > 0:
            single_file_ratio = single_file_commits / len(commits)
            if single_file_ratio > 0.9 and len(commits) > 3:
                self.suspicious_indicators.append(f"Almost all commits touch single file: {single_file_ratio:.1%}")
                self.warning_count += 1

    def analyze_working_hours(self, commits):
        """Analiza las horas de trabajo para detectar patrones inusuales"""
        night_commits = 0  # 12 AM - 6 AM
        early_morning = 0  # 6 AM - 9 AM
        
        for commit in commits:
            try:
                commit_time = datetime.fromisoformat(commit['date'].replace('Z', '+00:00'))
                hour = commit_time.hour
                
                if 0 <= hour < 6:
                    night_commits += 1
                elif 6 <= hour < 9:
                    early_morning += 1
                    
            except ValueError:
                continue
        
        # Demasiados commits nocturnos pueden indicar uso de IA
        if len(commits) > 0:
            night_ratio = night_commits / len(commits)
            if night_ratio > 0.6 and len(commits) > 4:
                self.suspicious_indicators.append(f"High proportion of night commits: {night_ratio:.1%}")
                self.warning_count += 1

    def calculate_timeline_validity(self):
        """Calcula si el timeline de commits es válido"""
        # Timeline es inválido si hay demasiadas advertencias
        if self.warning_count >= 5:
            self.timeline_valid = False
            self.suspicious_indicators.append("Timeline marked as INVALID due to multiple suspicious patterns")
        elif self.warning_count >= 3:
            self.suspicious_indicators.append("Timeline marked as SUSPICIOUS but still valid")

    def analyze(self):
        """Ejecuta el análisis completo del timeline de commits"""
        commits = self.get_commit_history()
        
        if not commits:
            # Si no hay commits recientes, asumir que es válido pero con advertencia
            self.suspicious_indicators.append("No recent commits found - analysis limited")
            return {
                "timeline_valid": True,
                "warning_count": 0,
                "suspicious_indicators": self.suspicious_indicators,
                "commit_count": 0
            }
        
        # Ejecutar todos los análisis
        self.analyze_commit_frequency(commits)
        self.analyze_commit_messages(commits)
        self.analyze_file_changes(commits)
        self.analyze_working_hours(commits)
        
        # Determinar validez final
        self.calculate_timeline_validity()
        
        return {
            "timeline_valid": self.timeline_valid,
            "warning_count": self.warning_count,
            "suspicious_indicators": self.suspicious_indicators,
            "commit_count": len(commits)
        }

def main():
    analyzer = CommitAnalyzer()
    result = analyzer.analyze()
    
    # Output requerido por el test de GitHub Classroom
    print(f"TIMELINE_VALID: {result['timeline_valid']}")
    
    # Información adicional para el profesor
    if result['warning_count'] > 0:
        print(f"# WARNING_COUNT: {result['warning_count']}")
        print(f"# COMMIT_COUNT: {result['commit_count']}")
        
        for indicator in result['suspicious_indicators'][:3]:  # Mostrar solo los primeros 3
            print(f"# {indicator}")

if __name__ == "__main__":
    main()