# AnalisadorVinhoTinto

## Introdução
Aplicação com o objetivo de fornecer previsões sobre qualidade de vinho com base nos atributos Acidez Fixa, Acidez Volátil, Cloreto, Dióxido de Enxofre, Sulfatos e Álcool.

As previsões são feitas utilizando um modelo de inteligência artificial treinado com os dados presentes no dataset disponível no link a seguir: https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009/data

## Descrição técnica<a name = "descricao_tecnica"></a>
O analisador de vinho é composto por três grandes componentes:
- WebApp: Front-end da aplicação
- WebApi: Api que recebe requisições do front e retorna o resultado da previsão do vinho
- Modelo preditivo: Modelo de machine learning que é utilizado pela WebApi para realizar as previsões de qualidade vinhos
  
A imagem abaixo da topologia da aplicação ilustra a integração entre estes componentes

![Topologia da aplicação](./imagens/topologia_aplicacao.png)

### WebApp:
Para a construção do front-end da aplicação utilizei apenas html, css e javascript.
Segue alguns detalhes sobre a implementação:

- Validação de Entrada: Scripts JavaScript validam os dados inseridos nos campos do formulário, exibindo um aviso se os valores estiverem fora dos limites aceitáveis.
- Arquivo de Configuração (config.js): Contém a URL do back-end Flask API, facilitando a manutenção e atualização da URL da API.

**Observação:** Você encontrará uma descrição detalhada sobre os limites aceitáveis das variáveis do modelo na seção Análise Exploratória de Dados (EDA) do notebook Classificador_de_vinhos.ipynb

### Web Api
#### Tecnologias e Frameworks Utilizados
- Flask: Framework web utilizado para construir a API.
- Flask-RESTx: Extensão do Flask para construção de APIs REST, facilitando a criação de rotas e a documentação com Swagger.
- Flask-CORS: Utilizado para habilitar Cross-Origin Resource Sharing (CORS) na API.
- Injector: Biblioteca para injeção de dependências, promovendo um design desacoplado e testável.
- Pickle: Utilizado para carregar o modelo de machine learning previamente treinado.
- Pydantic: Biblioteca utilizada para a validação de dados e a conversão de tipos de dados.
- Pandas: Utilizado para converter os dados de entrada em um DataFrame, que é o formato esperado pelo modelo.

#### Estrutura da API
Configuração Inicial
- A aplicação Flask é inicializada juntamente com as configurações de CORS e Swagger.
- Um contêiner de injeção de dependência é criado usando o Injector para gerenciar as dependências da aplicação.

Modelo Swagger
- Um modelo Swagger é definido para VinhoDto, especificando os campos e tipos de dados esperados na requisição. Isso inclui acidez fixa, acidez volátil, cloretos, dióxido de enxofre total, sulfatos e álcool.

Rota da API
- Endpoint *prever*: Rota POST que recebe os dados de entrada, valida-os e passa para o modelo preditivo.
- A rota utiliza VinhoDto para a validação dos dados de entrada.
- O modelo preditivo é injetado usando a injeção de dependências, promovendo a inversão de dependência.
- O resultado da predição é retornado como um JSON contendo a qualidade prevista do vinho.

Testes unitários
- Os testes de unidade podem ser encontrados no arquivo desempenho_modelo_testes.py

### Modelo preditivo
Utilizei o google colab para criar o notebook do modelo preditivo.
Segue o link do notebook, onde você encontrará todo o passo a passo para construção do modelo: https://colab.research.google.com/github/matheusmughrabi/AnalisadorVinhoTinto/blob/master/Classificador_de_vinhos.ipynb

## Requisitos e como executar<a name = "requisitos"></a>
### Requisitos
1. git instalado
2. python instalado
3. [Opcional] Algum gerenciador de pacotes python como virtualenv para facilitar a criação de um ambiente virtual ([virtualenv](https://virtualenv.pypa.io/en/latest/installation.html))

### Como executar
Primeiramente faça o clone do repositório: git clone [https://github.com/matheusmughrabi/AnalisadorVinhoTinto.git](https://github.com/matheusmughrabi/AnalisadorVinhoTinto.git)

#### WebApp
1. Abra o index.html que se encontra no diretório .\WebApp\src

#### WebApi
1. Abra o terminal no diretório relativo a raiz do projeto: .\WebApi\src
2. [Opcional] Crie o ambiente virtual
3. [Opcional] Ative o ambiente virtual
4. Execute o comando pip install -r requirements.txt
5. Execute o comando flask run --host 0.0.0.0 --port 5000 IMPORTANTE EXECUTAR COM A PORTA 5000 POIS O PROJETO WebApp ESTÁ APONTANDO PARA ESTA PORTA

#### Testes de unidade
1. Prepare o ambiente virtual preparado conforme explicado na seção anterior
2. Abra o terminal no diretório relativo a raiz do projeto: .\WebApi\src
3. Execute o comando pytest test_modelo_preditivo.py



## Observação sobre Desenvolvimento de software seguro
*Conforme solicitado nos critérios de avaliação do MVP, segue uma breve reflexão sobre como boas práticas de desenvolvimento de software seguro podem ser aplicadas a este projeto.*

A aplicação de técnicas e práticas de Desenvolvimento de Software Seguro é fundamental para garantir a confidencialidade, integridade e disponibilidade dos dados e sistemas. 

No contexto desta aplicação, várias práticas podem ser implementadas para aumentar a segurança.

Nota-se que a presente aplicação é muito simples e não trabalha com dados sensíveis de usuários, entretanto é importante considerar boas práticas de desenvolvimento seguro (imagine que a aplicação poderá crescer no futuro e guardar dados sensíveis de usuários e/ou empresas).

Segue uma pequena lista de pontos a se considerar.

1. Anonimização de Dados
Objetivo: Proteger a privacidade dos usuários, especialmente se a aplicação lida com dados sensíveis ou pessoais.
Implementação: Anonimizar dados que podem identificar indivíduos, como informações de contato ou localização. Embora dados sobre propriedades químicas do vinho possam não ser diretamente identificáveis, a anonimização ainda é relevante se esses dados estiverem associados a informações de produtores ou fornecedores.
2. Autenticação e Autorização
Objetivo: Controlar o acesso à aplicação e suas funcionalidades.
Implementação: Implementar um sistema robusto de autenticação e autorização, garantindo que apenas usuários autorizados possam acessar determinadas funcionalidades ou dados.
3. Validação de Entrada
Objetivo: Prevenir ataques de injeção e garantir que apenas dados formatados adequadamente sejam processados.
Implementação: Realizar uma validação rigorosa dos dados de entrada, tanto no lado do cliente quanto do servidor, rejeitando quaisquer entradas que não atendam aos critérios estabelecidos.
4. Gerenciamento de Dependências
Objetivo: Evitar vulnerabilidades de segurança decorrentes de bibliotecas de terceiros.
Implementação: Manter as bibliotecas e dependências atualizadas, utilizando ferramentas para monitorar e remediar vulnerabilidades conhecidas em dependências.
5. Tratamento de Erros e Logging
Objetivo: Evitar a exposição de informações sensíveis através de mensagens de erro e manter registros de atividades para auditoria e detecção de anomalias.
Implementação: Implementar um sistema de logging que registre atividades importantes sem expor dados sensíveis. As mensagens de erro devem ser genéricas para o usuário, mas detalhadas nos logs (acessíveis apenas por administradores).
6. Segurança na Comunicação
Objetivo: Proteger os dados durante a transmissão.
Implementação: Utilizar protocolos seguros como HTTPS para criptografar os dados enviados entre o cliente e o servidor.
7. Testes de Segurança
Objetivo: Identificar e corrigir vulnerabilidades de segurança.
Implementação: Realizar testes de segurança regulares, como testes de penetração, para identificar vulnerabilidades na aplicação.

**Conclusão**
A aplicação destas práticas de Desenvolvimento de Software Seguro é essencial para esta e outras aplicações. 
É importante notar que a segurança é um processo contínuo e deve ser considerada em todas as fases do desenvolvimento e manutenção do software.

## Limitações<a name = "limitacoes"></a>
Até o momento nosso modelo de inteligência artificial só é capaz de prever a qualidade de vinhos tinto.

## Observações <a name = "observacoes"></a>
Conforme descrito no notebook o modelo só é capaz de realizar previsões confiáveis se os seguintes limites forem respeitados na variáveis independentes:
- Acidez Fixa: 7.1 a 9.2 g/dm³

- Acidez Volátil: 0.39 a 0.64 g/dm³

- Cloretos: 0.07 a 0.09 g/dm³

- Dióxido de Enxofre Total: 22 a 62 mg/dm³

- Sulfatos: 0.62 a 0.73 g/dm

- Álcool: 9.5 a 10.2 %vol
