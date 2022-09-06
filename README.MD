# API comunicação de perda

-API: https://api-loss-communication.herokuapp.com/

## Loss Communication

#### POST /api/

- Eventos disponiveis: [Seca, Chuva excessiva, Geada, Granizo, Vendaval, Raio]

_Formato da requisição_

```json
{
  "name": "chrystian",
  "email": "teste@gmail.com",
  "cpf": "1111111112",
  "localization": "-20.8202, -49.3797",
  "date": "1993-03-03",
  "type": "trigo",
  "event": "Seca"
}
```

_Formato de resposta_

```json
{
  "id": 7,
  "name": "chrystian",
  "email": "teste@gmail.com",
  "cpf": "1111111112",
  "localization": "-20.8202, -49.3797",
  "type": "trigo",
  "date": "1993-03-03",
  "events": {
    "name": "Seca"
  }
}
```

_Caso coloque um evento invalido recebera a resposta_

```json
{
  "detail": "Not found."
}
```

#### GET /api/

_Formato da requisição_

```json
{}
```

_Formato de resposta_

```json
{
	{
  "communications": [
    {
      "id": 7,
      "name": "chrystian",
      "email": "teste@gmail.com",
      "cpf": "1111111112",
      "localization": "-20.8202, -49.3797",
      "type": "trigo",
      "date": "1993-03-03",
      "events": {
        "name": "Seca"
      }
    },
    {
      "id": 8,
      "name": "chrystian",
      "email": "teste@gmail.com",
      "cpf": "1111111112",
      "localization": "-20.8202, -49.3797",
      "type": "trigo",
      "date": "1993-03-03",
      "events": {
        "name": "Seca"
      }
    },
    {
      "id": 9,
      "name": "chrystian",
      "email": "teste@gmail.com",
      "cpf": "1111111112",
      "localization": "-20.8202, -49.3797",
      "type": "cenoura",
      "date": "1993-03-03",
      "events": {
        "name": "Seca"
      }
    }
  ]
}
}
```

#### PATCH /api/<id>

- Campos que podem ser atualizados: [email, type]

_Formato da requisição_

```json
{
  "type": "feijão"
}
```

_Formato de resposta_

```json
{
  "id": 8,
  "name": "chrystian",
  "email": "teste@gmail.com",
  "cpf": "1111111112",
  "localization": "-20.8202, -49.3797",
  "type": "feijão",
  "date": "1993-03-03",
  "events": {
    "name": "Seca"
  }
}
```

#### DELETE /api/<id>

_Formato da requisição_

```json
{}
```

_Formato de resposta_

```json
{}
```
