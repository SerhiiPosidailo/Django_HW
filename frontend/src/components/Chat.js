import React, {useEffect, useState} from 'react';
import {socketService} from "../service/socketService";

const Chat = () => {
    const [room, setRoom] = useState(null)
    const [socketClient, setSocketClient] = useState(null)
    const [messages, setMessages] = useState([])

    useEffect(() => {
        if (room) {
            socketInit(room)
        }
    }, [room]);

    const socketInit = async (room) => {
        const {chat} = await socketService();
        const client = await chat(room);


        client.onopen = () => {
            console.log('Chat socket connected');
        }

        client.onmessage = ({data}) => {
            console.log(data);
        }


    }
    return (
        <div>
            Chat
        </div>
    );
};

export {Chat};