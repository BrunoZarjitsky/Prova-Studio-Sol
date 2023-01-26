# Prova Backend Studio Sol
## **Bruno Zarjitsky - Desenvolvedor Backend**
## **brunozar@poli.ufrj.br**
## **[LinkedIn](https://www.linkedin.com/in/brunozar "linkedin.com/in/brunozar")**
## **[GitHub](https://github.com/BrunoZarjitsky)**

### **Objetivo**: Desenvolver uma API para verificação de senha seguindo os seguintes critérios
 - **minSize:**  Ter pelo menos **X** caracteres
 - **minUppercase:** Ter pelo menos **X** caracteres maiúsculos
 - **minLowercase:** Ter pelo menos **X** caracteres minúsculos
 - **minDigit**: Ter pelo menos **X** dígitos (0-9)
 - **minSpecialChars**: Ter pelo menos **X** caracteres especiais ( !@#$%^&*()-+\/{}[] )
 - **noRepeted**: Não ter nenhum caractere repetido em sequência

### **Entrada**
Como entrada, a API deve receber uma requisição HTTP no formato JSON contendo dois campos:
 - **password:** Uma string com a senha a ser testada
 - **rules:** Uma lista com dicionarios, cada dicionario irá conter os campos:
    - **rule:** O nome da regra a ser verificada
    - **value:** O valor de referencia para a verificação

Exemplo de requisição de entrada:
```JSON
{
    "password": "SenhaTestee123!@#",
    "rules": [
        {"rule": "minSize","value": 18},
        {"rule": "minUppercase","value": 3},
        {"rule": "minLowercase","value": 10},
        {"rule": "minSpecialChars","value": 4},
        {"rule": "minDigit","value": 4},
        {"rule": "noRepeted","value": 0}
    ]
}
```
**Observação:** Como a entrada do programa é no formato JSON, e o caracter "\\" faz parte dos caracteres especiais aceitos, para enviar uma senha que contenha este caracter, é preciso utilizar "\\\\" na senha.

### **Saida**
Como saida, a API deve retornar um JSON contendo os campos:
 - **verify:** Um booleano indicando se a senha passou ou não nas verificações
 - **noMatch:** Uma lista contendo o nome das verificações que a senha não passou

Exemplo de retorno da API:
```JSON
{
    "verify": false,
    "noMatch": [
        "minSize",
        "minUppercase",
        "minLowercase",
        "minSpecialChars",
        "minDigit",
        "noRepeted"
    ]
}
```

## **Requisitos do sistema**
 - Python 3.10 (sudo apt-get install python3.10 )
 - venv (sudo apt-get install python3-venv)

## Como rodar o programa:
Criando o ambiente virtual:
    
    python3 -m venv venv_studio_sol

Ativando o ambiente virtual

    source venv_studio_sol/bin/activate

Instalando os requisitos da aplicação

    pip install -r requirements.txt

Iniciando o servidor

    python studio_sol_API.py

Caso queira executar os testes unitários (Opcional)

    pytest test_api.py

### Alguns exemplos de POST requests para a API

```CURL
curl --location --request POST 'localhost:8080/verify' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=E28hRBtFFp0lVtG7kjJjWZ4Q1gqRHeYDg4N5vw6COq9Ta3Iy9V3lNajJT9DRKcPZ' \
--data-raw '{
    "password": "SenhaTeste123!@#",
    "rules": [
        {"rule": "minSize","value": 16},
        {"rule": "minUppercase","value": 2},
        {"rule": "minLowercase","value": 8},
        {"rule": "minSpecialChars","value": 3},
        {"rule": "minDigit","value": 3},
        {"rule": "noRepeted","value": 0}
    ]
}'
```
Resultado esperado:

{
    "verify": true,
    "noMatch": []
}

```CURL
curl --location --request POST 'localhost:8080/verify' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=E28hRBtFFp0lVtG7kjJjWZ4Q1gqRHeYDg4N5vw6COq9Ta3Iy9V3lNajJT9DRKcPZ' \
--data-raw '{
    "password": "SenhaTeste123!@#",
    "rules": [
        {"rule": "minSize","value": 17},
        {"rule": "minUppercase","value": 3},
        {"rule": "minLowercase","value": 9},
        {"rule": "minSpecialChars","value": 3},
        {"rule": "minDigit","value": 3},
        {"rule": "noRepeted","value": 0}
    ]
}'
```
Resultado esperado:

{
    "verify": false,
    "noMatch": [
        "minSize",
        "minUppercase",
        "minLowercase"
    ]
}

```CURL
curl --location --request POST 'localhost:8080/verify' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=E28hRBtFFp0lVtG7kjJjWZ4Q1gqRHeYDg4N5vw6COq9Ta3Iy9V3lNajJT9DRKcPZ' \
--data-raw '{
    "password": "SenhaTestee123!@#",
    "rules": [
        {"rule": "minSize","value": 18},
        {"rule": "minUppercase","value": 3},
        {"rule": "minLowercase","value": 10},
        {"rule": "minSpecialChars","value": 4},
        {"rule": "minDigit","value": 4},
        {"rule": "noRepeted","value": 0}
    ]
}'
```
Resultado esperado:

{
    "verify": false,
    "noMatch": [
        "minSize",
        "minUppercase",
        "minLowercase",
        "minSpecialChars",
        "minDigit",
        "noRepeted"
    ]
}
