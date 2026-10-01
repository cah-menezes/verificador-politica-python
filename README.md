# 🔐 Verificador de Política de Acesso

Script em Python que lê uma lista de usuários e cruza com a política de acessos da empresa, identificando automaticamente quem está com permissão incompatível com o cargo.

## 🚨 O que ele detecta

Usuários com acesso diferente do permitido para o cargo. Exemplos:
* Estagiário com acesso de administrador
* Suporte com acesso de escrita
* Qualquer cargo com permissão acima do definido na política

## 🛠️ Tecnologias Utilizadas

* Python 3 (`csv`)
* Git & GitHub

## 📂 Arquivos

* `verificador.py` → script principal
* `usuarios.csv` → lista de usuários com cargo e acesso atual
* `politica.csv` → política de acesso permitido por cargo

## 🏁 Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/cah-menezes/verificador-politica-python.git
cd verificador-politica-python
```

2. Execute o verificador:

```bash
python3 verificador.py
```

## 🗺️ Próximos Passos

* Implementar dicionário aninhado para verificar também sistemas permitidos por cargo e horário de acesso
* Exportar relatório para arquivo `.txt`
* Interface gráfica com tkinter