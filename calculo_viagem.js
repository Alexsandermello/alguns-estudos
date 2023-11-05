const precoDoCombustivel = 6.30;
const kmPorLitros = 8;
const distanciaDestinoEmKm = 100;

const litrosGastos = distanciaDestinoEmKm / kmPorLitros;
const valorGastos = litrosGastos * precoDoCombustivel;
console.log(valorGastos.toFixed(2));