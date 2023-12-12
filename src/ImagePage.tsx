import React from 'react';
import { useLocation } from 'react-router-dom';

const NotFound = () => {
    const location = useLocation();
    const params = new URLSearchParams(location.search);
    
    const alt = params.get('alt') ?? "Falscher QR-Code";
    const image = params.get('image') ?? "falsch.png";

    return (
        <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh' }}>
            <img style={{ maxWidth: '100%', maxHeight: '100%' }} src={`${process.env.PUBLIC_URL}/images/${image}.png`} alt={alt} />
        </div>
    );
}

export default NotFound;
