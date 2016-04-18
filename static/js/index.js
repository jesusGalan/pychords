var init = {};

init.pintar = function (param){
	for(var i = 0; i <  document.getElementsByClassName(param.getAttribute('value')).length; i++) {
		document.getElementsByClassName(param.getAttribute('value'))[i].innerHTML = init.pintarNota(param);
  }
}

init.pintarNota = function (param) {
  var value = param.getAttribute('value');
  var idNota = value + "-" + Math.random();
  var idWord = value + "-" + Math.random();
  var idPicker = value + "-" + Math.random();
  var idWordPicker = value + "-" + Math.random();

return '<div onmouseover="init.pintarPicker(\'' + idPicker + '\', \'' +idWordPicker+'\')" onmouseout="init.quitarPicker(\'' + idPicker + '\', \'' +idWordPicker+'\')">' +
	'<input id=\'' + idWordPicker+ '\' style="display: none" type="color" id="color" name="colorpicker" oninput="init.cambiarColorLetra(this, \'' + idNota + '\')">'  	+
  '<input style="height:21px;" id="' + idNota  + '" type="button" class="boxed" onclick="init.despintar(this);" value="'+ value + '">' +
       '<input id=\'' + idPicker+ '\' style="display: none" type="color" id="color" name="colorpicker" oninput="init.cambiarColor(this, \'' + idNota + '\')">' +
       '</div>'
}
