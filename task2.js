const paragraph = 'Investissement locatif T2 loué 496€/mois dont 26€ de charges.';

const searchTerm = 'loué';
const searchDate = '€/mois';

const indexOf = paragraph.indexOf(searchTerm);

const index = paragraph.indexOf(searchDate, (indexOf + 1))

console.log(index);
