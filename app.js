// Import the HTTP module
const http = require('http');

// Create a server
const server = http.createServer((req, res) => {
    // Set the HTTP response header
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    
    // Send the response body
    res.end('Hello, World!\n');
});

// Define the PORT
const PORT = 3000;

// Server starts listening
server.listen(PORT, () => {
    console.log(`Server is running at http://localhost:${PORT}/`);
});
