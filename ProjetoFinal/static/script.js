document.getElementById("calcular").addEventListener("click", function () {
  var state = document.getElementById("state").value;
  var origin = document.getElementById("origin").value;
  var destination = document.getElementById("destination").value;

  var data = {
    state: state,
    origin: origin,
    destination: destination,
  };

  fetch("/calcular", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then(function (data) {
      var resultadoElement = document.getElementById("resultado");
      resultadoElement.innerHTML = "Distância Total: " + data.distance + " Km";

      var caminhoElement = document.getElementById("caminho");
      caminhoElement.innerHTML = "Caminho: " + data.path.join(" -> ");
    });
});
