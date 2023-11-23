import React from 'react'

export default function Alert(props) {
    const capitalize =(word)=>{

        let lower = word.toLowerCase()
        return lower.charAt(0).toUpperCase() + lower.slice(1)
    }
    return (
        props.Alert && <div className={`alert alert-${props.Alert.typ} alert-dismissible fade show`} role="alert">
            <strong>{capitalize(props.Alert.typ)}! </strong>{props.Alert.msg}
        </div>


    )

}