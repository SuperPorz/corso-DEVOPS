import { useEffect, useState } from "react";

function ProductPage() {
    const [prodotti, setProdotti] = useState([]);
    // 1: logica applicativa
    async function getData() {
        let response = await fetch("http://127.0.0.1:8002/api/prodotti"); //con docker si può usare il nome servizio come URL
        let data = await response.json();
        console.log(data);
        setProdotti(data);
    }

    useEffect(() => {getData()}, [] )//richiama la funzione quando le variabili del secondo param. cambiano -> lasciando vuoto, non viene mai richiamata, ma solo eseguita la prima volta


    // 2: render
    return (
        <>
            <ul>
                {prodotti.map((x, i) => (
                    <Prodotto key={i} prodotto={x} />
                ))}
                
            </ul>
        </>
    )
}

function Prodotto({prodotto}) {
    
    async function handleClick() {
        let response = await fetch("http://127.0.0.1:8002/api/aggiungiProdotto", {
            method:"PUT",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify( {id:prodotto[0]} )
        })
        let data = await response.json()
        //dati
    }

    return (
        <>
            <div>
                <h1>{ prodotto[1] }</h1>
                <p>{ prodotto[2] }</p>
                <h2>{ prodotto[3] }</h2>
                <button onClick={handleClick}>COMPRA</button>
            </div>
        </>
    )
}

export default ProductPage;