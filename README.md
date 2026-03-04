# TP Cryptographie - AES avec PyCryptodome

Implémentation du chiffrement AES en modes **CBC** et **CFB** en Python.

## Arborescence

```
aes-crypto-tp/
├── venv/               ← environnement virtuel (ignoré par Git)
├── aes_cbc.py          ← chiffrement AES mode CBC
├── aes_cfb.py          ← chiffrement AES mode CFB
├── main.py             ← point d'entrée, lance les deux démos
├── .gitignore          ← fichiers à exclure de Git
└── README.md           ← ce fichier
```

## Installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/Azeflow10 aes-crypto-tp.git
cd aes-crypto-tp

# 2. Créer et activer le venv
python -m venv venv       
venv\Scripts\activate     

# 3. Installer les dépendances
pip install -r requirements.txt
```

## Utilisation

```bash
# Lancer les deux démonstrations
python main.py

# Ou séparément
python aes_cbc.py
python aes_cfb.py
```

## Modes expliqués

| Mode | Padding requis | Usage typique |
|------|---------------|---------------|
| **CBC** | Oui (PKCS7) | Fichiers, données fixes |
| **CFB** | Non | Flux, données variables |
