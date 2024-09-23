import { useState } from 'react';
import './App.css';

function App() {
  const [response, setResponse] = useState('');
  const [statusCode, setStatusCode] = useState<number | string>('');

  const handleRequest = async (endpoint: string) => {
    try {
      const res = await fetch(endpoint, {
        method: 'GET',
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
            <p style={{ marginBottom: "2px" }}>/user/get_user</p>
            <button onClick={() => handleRequest('/user/get_user')}>Send Request</button>
          </div>
          <div>
            <p style={{ marginBottom: "2px" }}>/users/get_user</p>
            <button onClick={() => handleRequest('/users/get_user')}>Send Request</button>
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;
