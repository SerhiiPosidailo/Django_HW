import React from 'react';
import {useForm} from "react-hook-form";
import {carService} from "../service/carService";

const CarForm = () => {
    const {register, handleSubmit, reset} = useForm();

    const save = async (car)=> {
        await carService.create(car)
        reset()
    }
    return (
        <form onSubmit={handleSubmit(save)}>
            <input type="text" placeholder={'model'}{...register('model')}/>
            <input type="text" placeholder={'year'}{...register('year')}/>
            <input type="text" placeholder={'number_of_seats'}{...register('number_of_seats')}/>
            <input type="text" placeholder={'body_type'}{...register('body_type')}/>
            <input type="text" placeholder={'engine_capacity'}{...register('engine_capacity')}/>
            <button>save</button>
        </form>
    );
};

export {CarForm};