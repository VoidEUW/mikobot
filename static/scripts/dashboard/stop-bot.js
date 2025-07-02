/**
 * @author VoidEUW
 * 
 * @function stopBot
 * @description function to stop the bot and update the status
 * @returns {void}
 */
function stopBot() {
  fetch("/api/v1/bot/status/stop", { method: "GET" })
    .then((res) => res.json())
    .then((data) => {
      document.getElementById(
        "start-status"
      ).textContent = `Bot Status: ${data.status}, PID: -`;
    })
    .catch((err) => {
      console.error(err);
      document.getElementById("start-status").textContent =
        "Fehler beim Stoppen des Bots";
    });
}
