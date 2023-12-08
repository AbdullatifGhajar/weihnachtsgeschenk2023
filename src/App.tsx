import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import QrCode from './QrCode';

function App() {
  return (
    <Router basename="/">
      <Routes>  
        <Route path="/" element={<QrCode />} />
      </Routes>
    </Router>
  );
}
export default App;