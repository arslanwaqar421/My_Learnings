import Navbar from './components/Navbar';
import './App.css';
import TextForm from './components/TextForm';
import About from './components/About';
import React,  { useState } from 'react';

function App() {
  const [Mode, setMode] = useState('light')

  const toggleMode = () =>{
    if(Mode === "light"){
      setMode("dark")
      document.body.style.backgroundColor= "grey"
    }
    else{
      setMode("light")
      document.body.style.backgroundColor="white"
    }
  }
  return (
    <>
      <Navbar title="Sitebar"  about="About Us" mode={Mode} toggleMode={toggleMode}/>
      <div className="container my-4">
      <TextForm heading="ExampleTextBox" mode ={Mode}/>
      </div>
      <About/>
    </>
  );
}


export default App;
