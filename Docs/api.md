### Documentação da API

#### Endpoint: Criar Utilizador
- **URL**: `/api/users/`
- **Método**: `POST`
- **Descrição**: Este endpoint permite criar um novo utilizador no sistema.

**Entrada (Request Body)**:
{
  "name": "Rodrigo Lopes",
  "email": "RodrigoLopes@gmail.com"
}

**Saída (Response)**:
- **Sucesso (201 Created)**:
{
  "id": 1,
  "name": "Rodrigo Lopes",
  "email": "RodrigoLopes@gmail.com"
}
- **Erro (400 Bad Request)**:
{
  "error": "user with this email already exists."
}

---

#### Endpoint: Obter Utilizador por ID
- **URL**: `/api/users/{id}/`
- **Método**: `GET`
- **Descrição**: Retorna os detalhes de um utilizador pelo ID fornecido.

**Entrada (Parâmetros de URL)**:
- **id**: ID do utilzador a ser retornado.

**Saída (Response)**:
- **Sucesso (200 OK)**:
{
  "id": 1,
  "name": "Rodrigo Lopes",
  "email": "RodrigoLopes@gmail.com"
}
- **Erro (404 Not Found)**:
{
  "error": "Usuário não encontrado"
}

---

#### Endpoint: Atualizar Utilizador
- **URL**: `/api/users/{id}/`
- **Método**: `PUT`
- **Descrição**: Atualiza os dados de um utilizador existente.

**Entrada (Request Body e Parâmetros de URL)**:
- **id**: ID do usuário a ser atualizado.
- **Body**:
{
  "name": "Pedro Lopes",
  "email": "Pedrolopes@gmail.com"
}

**Saída (Response)**:
- **Sucesso (200 OK)**:
{
  "id": 1,
  "name": "Pedro Lopes",
  "email": "Pedrolopes@gmail.com"
}
- **Erro (400 Bad Request)**:
{
  "error": "Dados inválidos"
}
- **Erro (404 Not Found)**:
{
  "error": "Uyilizador não encontrado"
}

---

#### Endpoint: Deletar Usuário
- **URL**:`/api/users/{id}/`
- **Método**: `DELETE`
- **Descrição**: Remove um utilizador do sistema.

**Entrada (Parâmetros de URL)**:
- **id**: ID do utilizador a ser removido.

**Saída (Response)**:
- **Sucesso (204 No Content)**:
  Não retorna nenhum conteúdo.
- **Erro (404 Not Found)**:
{
  "error":
}

---
