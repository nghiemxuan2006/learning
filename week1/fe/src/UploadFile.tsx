import React, { useState } from 'react';
import axios from 'axios';

const FileUpload = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [message, setMessage] = useState('');

  const onFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const onFileUpload = () => {
    const formData = new FormData();
    formData.append('file', selectedFile);

    axios.post('http://localhost:80/upload/', formData)
      .then(response => {
        setMessage('File uploaded successfully');
      })
      .catch(error => {
        setMessage('File upload failed');
      });
  };

  return (
    <div>
      <h2>File Upload</h2>
      <input type="file" onChange={onFileChange} />
      <button onClick={onFileUpload}>Upload</button>
      <p>{message}</p>
    </div>
  );
};

export default FileUpload;
