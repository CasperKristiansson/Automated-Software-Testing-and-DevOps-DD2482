import { useState } from 'react';
import './App.css';

function App() {
  const [response, setResponse] = useState('');
  const [statusCode, setStatusCode] = useState<number | string>('');

  const handleRequest = async (endpoint: string) => {
    try {
      const method = endpoint.includes('/user/get_user') ? 'GET' : 'POST';
      const res = await fetch(endpoint, {
        method: method,
        headers: {
          'Content-Type': 'application/json',
          "Cache-Control": "no-store, no-cache, must-revalidate, proxy-revalidate",
          "Expires": "0",
          "Pragma": "no-cache",
        },
        mode: 'cors',
      });

      const body = await res.json();
      setStatusCode(res.status);
      setResponse(JSON.stringify(body, null, 2));
    } catch (error) {
      if (error instanceof Error) {
        setResponse(`Error: ${error.message}`);
      } else {
        setResponse('An unknown error occurred');
      }
      setStatusCode('Error');
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <button
          style={{
            position: 'absolute',
            top: '20px',
            left: '50%',
            transform: 'translateX(-50%)',
            padding: '10px 20px',
            fontSize: '16px',
            cursor: 'pointer',
          }}
          onClick={() => handleRequest(`https://o2i85wdpe0.execute-api.eu-north-1.amazonaws.com/dev/user/add_user?t=${new Date().getTime()}`)}
        >
          Insert User
        </button>

        <div>
          <textarea
            value={`Status Code: ${statusCode}\n\nResponse Body:\n${response}`}
            readOnly
            rows={10}
            cols={50}
          />
        </div>

        <div style={{ display: 'flex', justifyContent: 'space-between', width: '100%', marginTop: '20px' }}>
          <div>
            <p style={{ marginBottom: '2px' }}>/user/get_user</p>
            <button onClick={() => handleRequest(`https://o2i85wdpe0.execute-api.eu-north-1.amazonaws.com/dev/user/get_user?t=${new Date().getTime()}`)}>
              Send Request
            </button>
          </div>
          <div>
            <p style={{ marginBottom: '2px' }}>/get_user</p>
            <button onClick={() => handleRequest(`https://o2i85wdpe0.execute-api.eu-north-1.amazonaws.com/dev/get_user?t=${new Date().getTime()}`)}>
              Send Request
            </button>
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;
