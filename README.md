
Vou contar um pouco da experiencia que tive desenvolvento este projeto.



🚨Tecnologias utilizadas Python e Flask (mais nenhum framework ou extensão foi instalado).🚨



---------Parte 1 - API de usuário e senha---------

Na primeira API @app.route('/ValidaLogin', methods = ['POST'])

criei o usuário e a senha padrões para relaizar a validadção, em seguida, criei dois campos "user_in" e "senha_in" que ficam aguardando dois valores em Json.

logo abaixo fiz a estrutura para validadar se os valores enviados pelo usuário(front) estão de acordo com os valores pré definidos e nessas validações são
retornadas em Json as respostas do campo 'status'.


---------Parte 2 - API de imagens---------

Nesta API criei uma especie de Array contendo no formato Json o link de 3 imagens e uma descrição simples.

Logo abaixo crio a função "DataImagens" onde pesso o retorno destes valores inserido no "DATA".
