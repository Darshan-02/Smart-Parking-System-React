import React from "react";
import {Navigate, Outlet} from 'react-router-dom';
//here the components are made private and are not able to access without logging in.
const PrivateComponent = ()=>{
    const auth = localStorage.getItem('user');
    return auth?<Outlet/>:<Navigate to="/signup"/>
}

export default PrivateComponent;