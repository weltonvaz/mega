# -*- coding: utf-8 -*-
import sqlite3
from loteria_caixa import *

concurso = MegaSena(1)
dados = concurso.todosDados()
print(dados)