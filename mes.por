programa {
funcao inicio() {
inteiro mes

escreva("Digite um número de 1 a 12:")
leia(mes)

escolha(mes) {
caso 1: caso 3: caso 5: caso 7: caso 8: caso 10: caso 12:
escreva("Esse mes tem 31 dias\n")
pare

caso 4: caso 6: caso 9: caso 11:
escreva("Esse mes tem 30 dias\n")
pare

caso 2:
escreva("Esse mes tem 28 ou 29 dias")
pare

caso contrario:
escreva("Mes não encontrado!")
}
}
}