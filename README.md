# 🔐 Verificador de Política de Acesso

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Segurança da Informação](https://img.shields.io/badge/Segurança_da_Informação-GRC-E74C3C?style=flat)
![Controle de Acesso](https://img.shields.io/badge/Controle_de_Acesso-Privilégio_Mínimo-2ECC71?style=flat)

Script em Python que compara os acessos reais dos usuários com a política definida por cargo — e aponta automaticamente quem está com permissão incompatível.

---

## 🎯 O problema que resolve

Em GRC, uma das falhas mais comuns de controle de acesso é o **desvio silencioso da política**: a política existe no papel, mas o que está configurado no sistema é diferente. Esse gap raramente aparece sozinho — alguém precisa ir atrás.

O script automatiza esse cruzamento: em vez de comparar linha por linha em uma planilha, ele lê os dados, aplica a regra e sinaliza as inconsistências.

---

## 🚨 O que ele detecta

Usuários com acesso **diferente** do permitido para o cargo. Exemplos:

- Estagiário com acesso de **administrador**
- Suporte com acesso de **escrita**
- Qualquer cargo com permissão acima (ou fora) do definido na política

---

## 📂 Arquivos

- `verificador.py` — lógica principal: lê os CSVs, cruza e gera o relatório
- `politica.csv` — mapeamento cargo → acesso permitido
- `usuarios.csv` — base de usuários com cargo e acesso atual

---

## 🚀 Como executar

```bash
git clone https://github.com/cah-menezes/verificador-politica-python.git
cd verificador-politica-python
python3 verificador.py
```

O relatório com as inconsistências encontradas é exibido direto no terminal.

---

*Projeto desenvolvido como parte de uma trilha de automação aplicada à segurança da informação e GRC.*