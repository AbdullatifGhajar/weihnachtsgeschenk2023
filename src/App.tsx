import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import NotFound from './NotFound';

function App() {
  return (
    <Router basename="/weihnachtsgeschenk2023">
      <Routes>
        <Route path="/" element={<NotFound />} />
      </Routes>
    </Router>
  );
}
export default App;
