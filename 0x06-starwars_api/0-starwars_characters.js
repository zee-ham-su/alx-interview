#!/usr/bin/env node
const request = require('request');

const cinemaId = process.argv[2];

if (!cinemaId) {
    console.log('Usage: node script.js <cinemaId>');
    process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${cinemaId}/`;

request(apiUrl, { json: true }, (err, res, body) => {
    if (err) {
        console.error('Error:', err);
        return;
    }

    if (res.statusCode !== 200) {
        console.error('Failed to fetch movie data. Status code:', res.statusCode);
        return;
    }


    // Print character names
    body.characters.forEach((characterUrl) => {
        request(characterUrl, { json: true }, (err, res, character) => {
            if (err) {
                console.error('Error fetching character:', err);
                return;
            }
            console.log(character.name);
        });
    });
});
