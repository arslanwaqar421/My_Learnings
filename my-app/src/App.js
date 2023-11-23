import Navbar from './components/Navbar';
import './App.css';
import { useState } from 'react';
import TextForm from './components/TextForm';
import About from './components/About';
import Alert from './components/Alert';

function App() {
  const [Mode, setMode] = useState('light')
  const [alert,setAlert] = useState(null)

  const showAlert = (message,type)=> {
    console.log("in alert")
    setAlert({
      msg : message,
      typ:type
    })
    setTimeout(() => {setAlert(null)},2000)
  }

  const toggleMode = () =>{
    if(Mode === "light"){
      setMode("dark")
      document.body.style.backgroundColor= "grey"
      showAlert("Dark mode activated!", "success")
    }
    else{
      setMode("light")
      document.body.style.backgroundColor="white"
      showAlert("Light mode activated!","warning")
    }
  }


  return (
    <>
      <Navbar title="Sitebar"  about="About Us" mode={Mode} toggleMode={toggleMode}/>
      <Alert Alert = {alert}/>
      <div className="container my-4">
      <TextForm heading="ExampleTextBox" mode ={Mode}/>
      </div>
      <About/>
    </>
  );
}


export default App;
