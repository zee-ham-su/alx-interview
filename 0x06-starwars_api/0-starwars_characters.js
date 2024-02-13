#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function fetchCharactersAndPrint(namesList, idx) {
    if (namesList.length === idx) {
        return;
    }

    request(namesList[idx], (error, response, body) => {
        if (error) {
            console.error(error);
        } else {
            const characterName = JSON.parse(body).name;
            console.log(characterName);
            fetchCharactersAndPrint(namesList, idx + 1);
        }
    });
}

request(movieUrl, (error, response, body) => {
    if (error) {
        console.error(error);
    } else {
        const charactersList = JSON.parse(body).characters;
        fetchCharactersAndPrint(charactersList, 0);
    }
});
