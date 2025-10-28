import { useState } from 'react';
import './App.css'
import ProductPage from './components/ProductPage';

function App() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [response, setResponse] = useState();

    async function handleSubmit(event) {
        event.preventDefault();//evitiamo il comportamento default di invio form che crea nuova richiesta HTTP
        let response = await fetch("http://127.0.0.1:8001/api/login", {
            method:"post",
            headers: {
                "Content-Type": "application/json"
            },
            body:JSON.stringify( {username, password} )
        });//contattiamo backend
        let data = await response.json();
        setResponse(data);//passo i dati da 'data' a 'response' tramite funzione 'setResponse', per averli direttamente riutilizzabili
    }

    return (
      <>
        {(!response || !response.success) &&
            <form action="" onSubmit={handleSubmit}>
                <input value={username} onChange={ (e) => setUsername(e.target.value) } />
                <input value={password} onChange={ (e) => setPassword(e.target.value) } />
                <button>Login</button>
            </form>
        }

        {response && 
            <>
                <h1>{response.message}</h1>{/* corto circuito logico, ritorna ultimo oggetto della catena (JS), ma è una porcheria */}
                {response.success && <ProductPage />}
            </>
        }
      </>
    )
}

export default App
