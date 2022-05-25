const paragraph = 'Investissement locatif T2 loué 496€/mois dont 26€ de charges.';

const searchTerm = 'loué';
const indexOf = paragraph.indexOf(searchTerm);

const index = paragraph.indexOf(searchTerm, (indexOf + 1))

console.log(`The index of the 2nd "${searchTerm}" is ${index}`);
// expected output: "The index of the 2nd "dog" is 52"