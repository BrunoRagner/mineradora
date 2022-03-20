# mineradora
 mineradora de bitcoin com python 



Esse é o código que nós vamos utilizar para a mineração de bitcoin dentro do Python!

Deu para ver que ele é bem pequeno, mas vamos a explicação do que cada parte faz para que possam entender como isso funciona.

Inicialmente estamos importando duas bibliotecas, a biblioteca hashlib e a biblioteca time.

Da biblioteca hashlib estamos trazendo a função sha256, que é uma função que vai fazer a criptografia das transações, pois como são informações protegidas é necessária uma criptografia para garantir que os dados não serão disponibilizados de qualquer maneira.

A biblioteca time, vamos utilizar para verificar o tempo de execução do nosso código para que você possa ver quanto tempo demora.

Dentro da função  **sha256**  vamos utilizar outras duas funções que são: função  **encode**  e a função  **hexdigest**.

Como essa função sha256 precisa do texto codificado para que possa fazer a criptografia, vamos utilizar a função encode com o argumento  **ascii**.

Quando utilizamos somente essas duas funções o Python vai retornar um objeto criptografado, então para que possamos visualizar em forma de string, vamos acrescentar a função hexdigest.

Dessa forma vamos poder visualizar a criptografia utilizada para o texto que for inserido!

Agora vamos partir para o código da mineração, nessa parte vamos ter que concatenar as informações do número do bloco, das transações, do hash anterior (que é a criptografia do bloco anterior na nossa cadeia de blocos) e a quantidade de zeros.



**OBS2:**  Então caso tenha interesse em aprender sobre esse assunto é importante que procure fontes específicas que vão tratar do assunto para que saiba com o que está lidando.

Para fazer a junção dessas informações nós vamos utilizar a estrutura de repetição  **while**, pois vamos ficar constantemente verificando se já chegamos ao resultado desejado.

Essa verificação será feita aplicando a função aplicar_sha256 que foi a função que criamos para aplicar essa criptografia e vamos verificar se o resultado começa com a quantidade de zeros desejada.

Essa quantidade vai ser baseada na bitcoin que será descoberto, então no momento em que estamos escrevendo esse post o número de zeros está em 20, o que já vai consumir muito recurso e muito tempo para minerar.

Para finalizar nós vamos testar o código passando alguns parâmetros genéricos (aqui você pode fazer a busca e colocar as informações corretas para minerar).

O if que foi colocado da forma  **if __name__ == “__main__”:**  é para que caso o usuário importe esse código para outro arquivo Python ele não vai executar o que está dentro do if.

No final desse código temos o print para mostrar o resultado e em seguida mostrar o tempo que o código demorou para rodar.

Lembrando que quanto maior a quantidade de zeros, maior o tempo de processamento.

Na máquina que estou rodando esse código no momento da escrita do post, vou colocar os resultados que obtive:

-   4 zeros – 0,11 segundos
-   5 zeros – 1,67 segundos
-   6 zeros – 9,15 segundos
-   7 zeros – 1160,77 segundos = 19,34 minutos

Então aqui temos o código pronto para poder minerar bitcoin, mas veja que a diferença de tempo começa a ficar absurda quando aumentamos apenas 1 zero, agora imagine fazer esse mesmo processamento com 20 zeros!

## Conclusão de Como Minerar Bitcoin com Python

Nessa aula nós conseguimos aprender como fazer a mineração de bitcoin utilizando o Python, no entanto é possível verificar que não é uma tarefa fácil para um computador comum.

Com alguns poucos testes não deu para chegar nem perto do que temos hoje, então vale lembrar que não é só porque o código é pequeno e simples que será fácil executá-lo.

Será necessária uma máquina muito potente para poder fazer isso de forma rápida e eficiente para sair na frente das outras milhares de pessoas que estão tentando fazer o mesmo.

Mas com essa aula já sabe que é possível fazer a mineração em bitcoin, agora caso tenha interesse em aprofundar seus conhecimentos sugerimos que busque livros, artigos, sites que falem especificamente do assunto!
