# score_db.py
# Sistema simples para salvar e carregar scores usando JSON

import json
import os

SCORE_FILE = os.path.join("scores", "pontuacoes.json")


def carregar_scores():
    if not os.path.exists(SCORE_FILE):
        return []  # Se o arquivo não existir ainda, retorna lista vazia
    with open(SCORE_FILE, "r") as arquivo:
        return json.load(arquivo)


def salvar_score(nome, pontuacao):
    os.makedirs("scores", exist_ok=True)  # ← Cria a pasta se não existir
    scores = carregar_scores()
    scores.append({"nome": nome, "pontuacao": pontuacao})
    with open(SCORE_FILE, "w") as arquivo:
        json.dump(scores, arquivo, indent=4)
