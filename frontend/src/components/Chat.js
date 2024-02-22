import React, {useEffect, useRef, useState} from 'react';
import {socketService} from "../service/socketService";
import {client} from "websocket";

const Chat = () => {
    const [room, setRoom] = useState(null)
    const [socketClient, setSocketClient] = useState(null)
    const [messages, setMessages] = useState([])
    const roomInput = useRef();


    useEffect(() => {
        if (room) {
            socketInit(room).then(client => setSocketClient(client))
        }
    }, [room]);

    const socketInit = async (room) => {
        const {chat} = await socketService();
        const client = await chat(room);


        client.onopen = () => {
            console.log('Chat socket connected');
        }

        client.onmessage = ({data}) => {
            const {message, user} = JSON.parse(data.toString());
            setMessages(prevState => [...prevState, {user, message}])
        }

        return client

    }

    const setRoomHendler = () => {
        setRoom(roomInput.current.value)
    }

    const handelPressEnter = (e) => {
        if (e.key==='Enter') {
            socketClient.send(JSON.stringify({
                data:e.target.value,
                action:'send_message',
                request_id:new Date().getTime()
            }))
            e.target.value = ''
        }
    };

    return (
        <div>
            {
                !room ?
                <div>
                    <input type="text" ref={roomInput}/>
                    <button onClick={setRoomHendler}>set</button>
                </div>
                    :
                    <div>
                        {messages.map(message=><div>{message.user}:{message.message}</div>)}
                        <input type="text" onKeyDown={handelPressEnter}/>
                    </div>
            }
        </div>
    );
};

export {Chat};