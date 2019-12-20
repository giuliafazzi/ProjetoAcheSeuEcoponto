$(document).ready(function() {
  // mapa
  var botao = document.getElementById("btnLista");
  var mapa = document.getElementById("cardMap");
  var empresas = document.getElementById("cardList");

  // objetivo
  var _comprar = document.getElementById("cbComprar");
  var _vender = document.getElementById("cbVender");
  var _doar = document.getElementById("cbDoar");
  var _coletar = document.getElementById("cbColetar");

  // qualidade do material
  var _prensado = document.getElementById("cbPrensado");
  var _limpo = document.getElementById("cbLimpo");
  var _inteiro = document.getElementById("cbInteiro");
  var _cacos = document.getElementById("cbCacos");
  var _unidade = document.getElementById("cbUnidade");
  var _triturado = document.getElementById("cbTriturado");

  _comprar.checked = false;
  _vender.checked = false;
  _doar.checked = false;
  _coletar.checked = false;

  _prensado.checked = false;
  _limpo.checked = false;
  _inteiro.checked = false;
  _cacos.checked = false;
  _unidade.checked = false;
  _triturado.checked = false;

  // OBJETIVOS (ON CHANGE)
  _comprar.onchange = function() {
    if (_comprar.checked == true) {
      document.getElementById("lbComprar").style.backgroundColor = "#0f9df7";
    } else {
      document.getElementById("lbComprar").style.backgroundColor =
        "rgb(182, 182, 182)";
      document.getElementById("lbComprar").style.borderColor =
        "rgb(182, 182, 182)";
    }
  };

  _vender.onchange = function() {
    if (_vender.checked == true) {
      document.getElementById("lbVender").style.backgroundColor = "#0f9df7";
    } else {
      document.getElementById("lbVender").style.backgroundColor =
        "rgb(182, 182, 182)";
      document.getElementById("lbVender").style.borderColor =
        "rgb(182, 182, 182)";
    }
  };

  _doar.onchange = function() {
    if (_doar.checked == true) {
      document.getElementById("lbDoar").style.backgroundColor = "#0f9df7";
    } else {
      document.getElementById("lbDoar").style.backgroundColor =
        "rgb(182, 182, 182)";
      document.getElementById("lbDoar").style.borderColor =
        "rgb(182, 182, 182)";
    }
  };

  _coletar.onchange = function() {
    if (_coletar.checked == true) {
      document.getElementById("lbColetar").style.backgroundColor = "#0f9df7";
    } else {
      document.getElementById("lbColetar").style.backgroundColor =
        "rgb(182, 182, 182)";
      document.getElementById("lbColetar").style.borderColor =
        "rgb(182, 182, 182)";
    }
  };

  // QUALIDADE DO MATERIAL (ON CHANGE)
  _prensado.onchange = function() {
    if (_prensado.checked == true) {
      document.getElementById("lbPrensado").style.backgroundColor = "#0f9df7";
    } else {
      document.getElementById("lbPrensado").style.backgroundColor =
        "rgb(182, 182, 182)";
      document.getElementById("lbPrensado").style.borderColor =
        "rgb(182, 182, 182)";
    }
  };

  _limpo.onchange = function() {
    if (_limpo.checked == true) {
      document.getElementById("lbLimpo").style.backgroundColor = "#0f9df7";
    } else {
      document.getElementById("lbLimpo").style.backgroundColor =
        "rgb(182, 182, 182)";
      document.getElementById("lbLimpo").style.borderColor =
        "rgb(182, 182, 182)";
    }
  };

  _inteiro.onchange = function() {
    if (_inteiro.checked == true) {
      document.getElementById("lbInteiro").style.backgroundColor = "#0f9df7";
    } else {
      document.getElementById("lbInteiro").style.backgroundColor =
        "rgb(182, 182, 182)";
      document.getElementById("lbInteiro").style.borderColor =
        "rgb(182, 182, 182)";
    }
  };

  _cacos.onchange = function() {
    if (_cacos.checked == true) {
      document.getElementById("lbCacos").style.backgroundColor = "#0f9df7";
    } else {
      document.getElementById("lbCacos").style.backgroundColor =
        "rgb(182, 182, 182)";
      document.getElementById("lbCacos").style.borderColor =
        "rgb(182, 182, 182)";
    }
  };

  _unidade.onchange = function() {
    if (_unidade.checked == true) {
      document.getElementById("lbUnidade").style.backgroundColor = "#0f9df7";
    } else {
      document.getElementById("lbUnidade").style.backgroundColor =
        "rgb(182, 182, 182)";
      document.getElementById("lbUnidade").style.borderColor =
        "rgb(182, 182, 182)";
    }
  };

  _triturado.onchange = function() {
    if (_triturado.checked == true) {
      document.getElementById("lbTriturado").style.backgroundColor = "#0f9df7";
    } else {
      document.getElementById("lbTriturado").style.backgroundColor =
        "rgb(182, 182, 182)";
      document.getElementById("lbTriturado").style.borderColor =
        "rgb(182, 182, 182)";
    }
  };

  // LISTAR EMPRESAS
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
