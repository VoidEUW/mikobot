/**
 * @author VoidEUW
 * 
 * @file terminal.js
 * @description file to handle the terminal output in the dashboard
 * @returns {void}
 */

const socket = io();
const terminal = document.getElementById("terminal");

// check if the user is admin -> display debug (unless user hides debug)
socket.on("terminal_output", (msg) => {
  const line = `${msg.time} [${msg.type.toUpperCase()}] ${msg.message}\n`;
  terminal.textContent += line;
  terminal.scrollTop = terminal.scrollHeight;
});
