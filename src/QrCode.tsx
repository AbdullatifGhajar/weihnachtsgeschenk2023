import React from 'react';
import { useParams } from 'react-router-dom';

type QeCodeParams = {
    codeId: string;
};

const QrCode: React.FC = () => {
    const { codeId } = useParams<QeCodeParams>();

    return (
        <img src={`${process.env.PUBLIC_URL}/static/${codeId}.png`} alt="QR Code" />
    );
}

export default QrCode;
