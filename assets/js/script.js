$(document).ready(function() {
  var botao = document.getElementById("btnLista");
  var mapa = document.getElementById("cardMap");
  var empresas = document.getElementById("cardList");

  botao.onclick = function() {
    if (mapa.style.display != "none") {
      mapa.style.display = "none";
      empresas.style.display = "block";
    } else {
      mapa.style.display = "block";
      empresas.style.display = "none";
    }
  };
});
