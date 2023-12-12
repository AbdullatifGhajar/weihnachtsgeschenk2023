import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ImagePage from './ImagePage';

function App() {
  return (
    <Router basename="/weihnachtsgeschenk2023">
      <Routes>
        <Route path="/" element={<ImagePage />} />
      </Routes>
    </Router>
  );
}
export default App;
