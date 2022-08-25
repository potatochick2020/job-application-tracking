import React from 'react';
import { useAuth0 } from '@auth0/auth0-react'
import Profile from './Profile';
const All_table = () => {
    const { user } = useAuth0();
    if (user == null){
        return(
            <div>
                Please Log In
            </div>
        )
    } else {
        return(
            <Profile />
            
        )
    }
    
}

export default All_table