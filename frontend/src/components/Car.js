import React from 'react';

const Car = ({car}) => {
    const {id, model, year, number_of_seats, body_type, engine_capacity} = car;
    return (
        <div>
            <div>ID: {id}</div>
            <div>model: {model}</div>
            <div>year: {year}</div>
            <div>number_of_seats: {number_of_seats}</div>
            <div>body_type: {body_type}</div>
            <div>engine_capacity: {engine_capacity}</div>

        </div>
    );
};

export {Car};