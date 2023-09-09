import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Ganti URL sesuai dengan lokasi file JSON Anda
    axios.get('/path/to/your/data.json')
      .then((response) => {
        setData(response.data.items);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h1>JSON Data</h1>
      <ul>
        {data.map((item) => (
          <li key={item.id}>
            <strong>{item.name}</strong>: {item.description}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
