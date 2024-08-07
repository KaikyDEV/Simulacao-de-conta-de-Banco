﻿# Simulacao-de-conta-de-Banco

 código começa importando a classe Conta do módulo exercício. Em seguida, uma instância de Conta é criada com número "001" e saldo inicial de 1000. O nome do usuário é solicitado e um menu de opções é gerado dinamicamente com base no nome inserido.

Um loop while True é usado para exibir o menu repetidamente até que o usuário escolha sair (opção 4). O menu oferece as seguintes opções:

    Visualizar o saldo atual da conta chamando o método mostrar_saldo() da instância conta.
    Sacar um valor, onde o valor é solicitado ao usuário, convertido para float, e passado para o método sacar().
    Depositar um valor, onde o valor é solicitado ao usuário, convertido para float, e passado para o método depositar().
    Sair do loop e finalizar o programa, exibindo uma mensagem de agradecimento ao usuário.

Cada opção retorna ao menu após a operação ser concluída, exceto a opção de saída, que encerra o loop.


O código define a classe Conta para gerenciar operações bancárias simples. Abaixo está uma descrição técnica detalhada do código completo:
Classe Conta
Construtor (__init__):

    Inicializa uma instância de Conta com o número da agência (nmr_agencia) e um saldo inicial opcional (saldo), padrão de 0.
    _saldo: Atributo privado que armazena o saldo da conta.
    nmr_agencia: Atributo público que armazena o número da agência.

Métodos:

    depositar(self, valor):
        Recebe um valor como argumento e o adiciona ao saldo da conta.
        Imprime uma mensagem confirmando o depósito e mostrando o saldo atual.

    sacar(self, valor):
        Recebe um valor como argumento e o subtrai do saldo da conta, se houver saldo suficiente.
        Imprime uma mensagem confirmando o saque e mostrando o saldo restante, ou uma mensagem de erro se o saldo for insuficiente.

    mostrar_saldo(self):
        Retorna o saldo atual da conta.

Código Principal
Importação:

    Importa a classe Conta do módulo exercício.

Instanciação:

    Cria uma instância de Conta com número de agência "001" e saldo inicial de 1000.

Interação com o Usuário:

    Solicita o nome do usuário com input.

Menu Dinâmico:

    Cria um menu interativo utilizando uma string formatada com o nome do usuário.

Loop Principal (while True):

    Exibe o menu e solicita uma opção ao usuário.

Opções do Menu:

    Visualizar Conta:
        Chama mostrar_saldo da instância conta e exibe o saldo atual.
    Sacar:
        Solicita um valor ao usuário, converte para float, e chama sacar da instância conta.
    Depositar:
        Solicita um valor ao usuário, converte para float, e chama depositar da instância conta.
    Sair:
        Exibe uma mensagem de agradecimento e encerra o loop, finalizando o programa.


Encapsulamento é um dos pilares fundamentais da Programação Orientada a Objetos (POO). Em Python, ele refere-se à restrição do acesso direto a alguns dos componentes de um objeto, permitindo o controle sobre como esses componentes são acessados e modificados. Isso ajuda a proteger os dados internos de uma classe e a manter a integridade dos objetos.
Como o Encapsulamento é Implementado em Python:

    Atributos Públicos:
        Atributos que podem ser acessados diretamente de fora da classe.
        Não há convenção específica para atributos públicos.


Atributos Protegidos:

    Atributos que devem ser tratados como semi-privados, isto é, uma indicação de que não devem ser acessados diretamente fora da classe e suas subclasses.
    Por convenção, prefixamos o nome do atributo com um único sublinhado (_).


Atributos Privados:

    Atributos que são realmente privados e não devem ser acessados diretamente fora da classe.
    Em Python, prefixamos o nome do atributo com dois sublinhados (__), o que resulta em name mangling, uma forma de modificar o nome do atributo para incluir o nome da classe e evitar conflitos.

Métodos de Acesso (Getters e Setters):

Para acessar e modificar atributos privados ou protegidos, utilizamos métodos especiais chamados getters e setters.

Vantagens do Encapsulamento:

    Proteção de Dados:
        Restringe o acesso direto a dados sensíveis, prevenindo modificações não autorizadas ou acidentais.

    Abstração:
        Permite esconder os detalhes da implementação interna e expor apenas o que é necessário através de uma interface pública.

    Manutenção e Evolução:
        Facilita a manutenção e evolução do código, pois as mudanças na implementação interna não afetam o código que usa a classe.

    Controle sobre Modificações:
        Através de setters, podemos incluir lógica adicional (como validação) ao modificar os atributos.

Encapsulamento é uma prática essencial para escrever código robusto, modular e seguro em programação orientada a objetos.
