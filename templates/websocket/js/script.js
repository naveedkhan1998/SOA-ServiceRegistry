const socket = new WebSocket("ws://localhost:8000/ws/connect/");

socket.onopen = (event) => {
  console.log("WebSocket connection opened.");
};

socket.onmessage = (event) => {
  console.log("Received message: " + event.data);
};

socket.onclose = (event) => {
  console.log("WebSocket connection closed.");
};

document.getElementById("sendButton").addEventListener("click", () => {
  // Add your message content here before sending it
  const message = "";
  socket.send(message);
});
