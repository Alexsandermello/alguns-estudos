const precoEtanol = 5.79;
const PrecoGasolina = 6.66;
const kmPorLitros = 10;
const distanciaDestinoEmKm = 100;
const tipoCombustivel = 'Gasolina';

const litrosGastos = distanciaDestinoEmKm / kmPorLitros;

if (tipoCombustivel === 'Etanol') {
  const valorGasto = litrosConsumidos * precoEtanol;
  console.log(valorGasto.toFixed(2));
} else {
  const valorGasto = litrosGastos * PrecoGasolina;
  console.log(valorGastos.toFixed(2));
}