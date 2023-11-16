import React, {useState} from 'react'

export default function TextForm(props) {

    const [Text,setText] = useState("Enter Text here")

    const handleClick = ()=> {
        console.log("Upper Case clicked")
        let newText = Text.toUpperCase()
        setText(newText)
    }

    const handleOnChange = (event) => {
        console.log("On Change!")
        setText(event.target.value)
    }

    const convertToLower = () =>{
        setText(Text.toLowerCase())
    }

    return (
        <>
            <form id="form1">
                <h1>{props.heading}</h1>
                <div className="mb-3">
                    <textarea name="ex" id="text-1" cols="150" rows="13" value = {Text} onChange={handleOnChange}></textarea>
                </div>
                <button className="btn btn-primary" onClick={handleClick}>Convert to Upper</button>
                <button className="btn btn-primary mx-2" onClick={convertToLower}>Convert to Lower</button>
  
            </form>
            <div className="container my-2">
                <h1>Your text Summary</h1>
                <p>{Text.split(" ").length} words and {Text.length} Characters</p>
            </div>
        </>
    )
}
