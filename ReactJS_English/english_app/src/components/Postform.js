import React, {useState}  from "react";
import Axios from "axios";

function Postform(){
    const url = "http://0.0.0.0:8000/vocab"
    const [data, setData] = useState("");
    function sumit(){
        let datas = data
        fetch(url,{
            method: 'POST',
            headers:{
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({"vocab_str": datas})
        }).then(result => {result.json().then((resp)=>{console.log(resp)})
        }) 
    }
    return(
        <div>
            <form>
                <input id="vocab" onChange={(e) => {setData(e.target.value)}} value={data} type="text"></input>
                <button type="button" onClick={sumit}>Sumit</button>
            </form>
        </div>
    )
}
export default Postform;

