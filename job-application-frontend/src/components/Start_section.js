import React from 'react';
import { useAuth0 } from '@auth0/auth0-react'
import Profile from './Profile';
const Start_section = () => {
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

export default Start_section