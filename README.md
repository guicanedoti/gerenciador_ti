# Sistema de Gerenciamento de Equipamentos de TI

Este projeto é um sistema web desenvolvido com Django para gerenciar os equipamentos do inventário da **Secretaria de Agricultura e Desenvolvimento Rural do Distrito Federal**. Ele permite o controle de departamentos, salas, responsáveis, equipamentos e alocações, oferecendo funcionalidades de cadastro, edição, visualização e exclusão de registros, com autenticação de usuários.

## 🚀 Funcionalidades

- Autenticação de usuários com login obrigatório
- CRUD completo para:
  - Departamentos
  - Salas
  - Responsáveis
  - Equipamentos
  - Alocações (vínculo entre equipamento, sala e responsável)
- Interface amigável com Bootstrap
- Templates reutilizáveis com `base.html`
- Controle de acesso às views usando `LoginRequiredMixin`

## 🛠️ Tecnologias Utilizadas

- Python 3
- Django
- HTML5
- CSS3 + Bootstrap
- JavaScript (básico para interações visuais)
- SQLite (padrão, mas compatível com PostgreSQL)

## 🔧 Instalação

1. Clone o repositório:
   ```bash
   git clone (https://github.com/guicanedoti/gerenciador_ti)
   cd gerenciador_ti

## 🧑‍💻 Desenvolvedores

Guilherme Canedo Santos https://github.com/guicanedoti <br> 
Ana Gabriela Franco  https://github.com/anagabrielaf
