import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import QrCode from './QrCode';
import NotFound from './NotFound';

function App() {
  return (
    <Router basename="/weihnachtsgeschenk2023">
      <Routes>
        <Route path="/code/:codeId" element={<QrCode />} />
        <Route path="/no" element={<NotFound />} />
      </Routes>
    </Router>
  );
}
export default App;