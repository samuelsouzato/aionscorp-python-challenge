import sys
import os

# Esse código força o Python a adicionar a raiz do projeto ao sys.path, permitindo que ele encontre app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
