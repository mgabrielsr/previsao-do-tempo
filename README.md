# API de Previsão do Tempo

API para obter informações sobre o tempo, incluindo temperatura atual e previsões a cada 3 horas.

## Funcionalidades

- **Temperatura Atual**: Temperatura atual da cidade.
- **Previsões**: Previsões a cada 3 horas.
- **Ícones e Gráficos**: Representações visuais das condições climáticas.
- **Detecção de Localização**: Preenchimento automático da cidade com base na localização atual.

## Requisitos

- Python 3.7+
- `requests` `flask` `matplotlib`

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seurepositorio/api-previsao-tempo.git
    ```
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

Inicie o servidor:
```bash
python app.py
Acesse a API em http://localhost:5000.
```

## Endpoints
- GET /weather/current: Temperatura atual.
   - Parâmetro: city (nome da cidade)
- GET /weather/forecast: Previsões a cada 3 horas.
   - Parâmetro: city (nome da cidade)
  
## Exemplo de Requisição

Temperatura Atual:
  
  ```bash
  curl "http://localhost:5000/weather/current?city=São Paulo"
  ```
##  Previsões:

  ```bash
  curl "http://localhost:5000/weather/forecast?city=São Paulo"
  ```

  ## Contribuição
  Para contribuir, faça um fork e envie um pull request.
