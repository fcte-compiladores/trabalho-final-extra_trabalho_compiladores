"""
DeadCodeDetector - Um analisador de código morto para Python
"""

__version__ = "1.0.0"
__author__ = "Seu Nome"

from .analyzer import DeadCodeAnalyzer
from .reporter import Reporter

__all__ = ["DeadCodeAnalyzer", "Reporter"] 