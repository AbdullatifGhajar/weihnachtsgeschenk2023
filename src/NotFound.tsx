import React from 'react';

const NotFound = () => {
    return (
        <div>
            <img src= {`${process.env.PUBLIC_URL}/images/falsch.png`} alt="falscher QR-Code" />
        </div>
    );
}

export default NotFound;
