from flask import Flask, request, jsonify, make_response
import json

alunos = [
    {
        "id": 1,
        "aluno": "João Ayrton",
        "RA": "2101236"
    },
    {
        "id": 2,
        "aluno": "Julio Cesar",
        "RA": "2101214"
    },
    {
        "id": 3,
        "aluno": "Diego Veríssimo",
        "RA": "2101350"
    },
    {
        "id": 4,
        "aluno": "Lívia Alves",
        "RA": "2101325"
    },
    {
        "id": 5,
        "aluno": "Victor Souza",
        "RA": "2100774"
    },
    {
        "id": 6,
        "aluno": "Claudio Simões",
        "RA": "2101274"
    }
]

class Model():

    def jsonReturn():
        aluno = alunos[5]["id"]

        if aluno > 0 and aluno < 2:
            return "Registrado na tabela X"

        elif aluno > 2:
            return "Registrado na tabela Y"