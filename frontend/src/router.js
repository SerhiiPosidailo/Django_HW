import {createBrowserRouter, Navigate} from "react-router-dom";

import {LoginPage} from "./pages/LoginPage";
import {CarsPage} from "./pages/CarsPage";
import {MainLayout} from "./layouts/MainLayout";

const router = createBrowserRouter([
    {
        path: '', element: <MainLayout/>, children: [
            {index: true, element: <Navigate to={'login'}/>},
            {path: 'login', element: <LoginPage/>},
            {path: 'cars', element: <CarsPage/>}
        ]
    }
])

export {
    router
}