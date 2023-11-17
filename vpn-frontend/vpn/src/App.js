import logo from './logo.svg';
import './App.css';
import {HomePage} from ".container/mainpage/index.js";


function App() {
  return (
    <Routes>
      <Route
      path="/"
          element={
              <HomePage />
          }/>
    </Routes>
  );
}

export default App;
