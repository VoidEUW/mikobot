/**
 * @author VoidEUW
 * 
 * @function startBot
 * @description function to start the bot and update the status
 * @returns {void}
 */
function startBot() {
  fetch("/api/v1/bot/status/start", { method: "GET" })
    .then((res) => res.json())
    .then((data) => {
      document.getElementById("start-status").textContent = `Bot Status: ${
        data.status
      }, PID: ${data.pid ?? "N/A"}`;
    })
    .catch((err) => {
      console.error(err);
      document.getElementById("start-status").textContent =
        "Fehler beim Starten des Bots";
    });
}
