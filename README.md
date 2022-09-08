# Desafio Swapi
> **LORE:**
Esse projeto tem como finalidade fazer uma integração com a swapi para pegar os nomes dos habitantes do planeta escrito pelo cliente.  
Criado em python usando a IDE Pycharm esse projeto utliza arquivos .py e .html para rodar.  
Pode se dizer que essa é a mk.1 do desafio, mesmo ele tendo passado por muitos __buffs e nerfs__ essa seria a versão mais palpavel.  
Com a ajuda da API do star wars o cliente recebe os nomes dos habitantes desde Tatooine onde temos muitas pessoas, até Dagobah, onde teóricamente se lembrarmos foi onde 
Mestre Yoda foi se exilar, considerado o planeta mais puro da galáxia, porém após a morte de Yoda o planeta ficou com 0 habitantes...  
logo a api devolvera uma lista vazia para este planeta.  🪐

**FUNCIONAMENTO:**
📁 Temos 3 pastas principais: _Model, Service e Controller_ uma adaptação do padrão de projeto _MVC_. 📁
* MODEL: Um arquivo com a maioria das classes que estão gerando variaveis locais, seja fazer listas, criar dicionarios, entre outros...
* SERVICE: Faz as integrações com a API do Star wars
* CONTROLLER: Usa toda a informação que é dada pelos outros 2 arquivos com a ajuda do _micro framework FLASK_ para fazer uma _API_ própria**

|**COMO USAR:**|
|----------------------------------------------------------------------------|
| Abra o arquivo controller na sua IDE preferida. |
|Rode o arquivo e clique no link que vai aparecer no terminal. |
| O link ira abrir uma pagina no navegador com uma barra de pesquisa onde você vai poder digitar o nome do planeta. |
|Ao procurar o planeta o código funcionara devolvendo ou o resultado dos habitantes do planeta ou um erro com um link de redirecionamento|

