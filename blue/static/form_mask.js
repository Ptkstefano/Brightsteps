
function formatar_tel(mascara, documento) {
  let i = documento.value.length;
  let saida = '#';
  let texto = mascara.substring(i);
  while (texto.substring(0, 1) != saida && texto.length ) {
    documento.value += texto.substring(0, 1);
    i++;
    texto = mascara.substring(i);
  }
}


function formatar_cpf(campo) {
    var valor = campo.value.replace(/\D/g, '');
    var formatado = '';

    if (valor.length > 0) {
        formatado = valor.substring(0, 3) + '.';
    }
    if (valor.length > 3) {
        formatado += valor.substring(3, 6) + '.';
    }
    if (valor.length > 6) {
        formatado += valor.substring(6, 9) + '-';
    }
    if (valor.length > 9) {
        formatado += valor.substring(9, 11);
    }

    campo.value = formatado;
}
