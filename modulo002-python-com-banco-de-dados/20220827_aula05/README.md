
# Exercício

Vamos criar as bases de um sistema de gerencimento de finanças pessoais!

* O sistema terá que armazenar os dados de acesso e os dados pessoais do usuário
* O núcleo do nosso sistema será baseado em contas e transações
* Uma conta terá que possuir um ID, um ID do usuário dono dessa conta, um nome e um saldo, pelo menos
* Uma transação sempre terá um identificador, uma conta a ser debitada, uma conta a ser creditada, o valor da transação e a data e a hora que a transação aconteceu
  * Dica: Na tabela de transações teremos 2 chaves estrangeiras que irão apontar para a mesma coluna da tabela que será referenciada
  * Dica 2: Para salvar a data e a hora que a transação foi feita, consulte https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime/33532154#33532154
* Utilize SQLAlchemy para as models e Alembic para as migrations
* Baseando-se no que foi feito nas aulas anteriores fica mais fácil terminar essa tarefa.