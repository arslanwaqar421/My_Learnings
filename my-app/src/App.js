import Navbar from './components/Navbar';
import './App.css';
import { useState } from 'react';
import TextForm from './components/TextForm';
import About from './components/About';
import Alert from './components/Alert';
// Update the import statements for v6
import {
  BrowserRouter,
  Routes, // Replace 'Switch' with 'Routes'
  Route,
} from "react-router-dom";


function App() {
  const [Mode, setMode] = useState('light')
  const [alert, setAlert] = useState(null)

  const showAlert = (message, type) => {
    console.log("in alert")
    setAlert({
      msg: message,
      typ: type
    })
    setTimeout(() => { setAlert(null) }, 2000)
  }

  const toggleMode = () => {
    if (Mode === "light") {
      setMode("dark")
      document.body.style.backgroundColor = "grey"
      showAlert("Dark mode activated!", "success")
    }
    else {
      setMode("light")
      document.body.style.backgroundColor = "white"
      showAlert("Light mode activated!", "warning")
    }
  }


  return (
    <BrowserRouter>
      <Navbar title="Sitebar" about="About Us" mode={Mode} toggleMode={toggleMode} />
      <Alert Alert={alert} />
        <div className="container my-4">
          <Routes>
            <Route path="/about" element={<About />} />
            <Route path="/" element={<TextForm heading="ExampleTextBox" mode={Mode} />} />
          </Routes>
        </div>
    </BrowserRouter>
  );
}


export default App;
