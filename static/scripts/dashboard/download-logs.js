/**
 * @author VoidEUW
 * 
 * @function downloadLogs
 * @description function to download the logs from the terminal
 * @returns {void}
 */
function downloadLogs() {
  const text = document.getElementById("terminal").textContent;
  const blob = new Blob([text], { type: "text/plain" });
  const url = URL.createObjectURL(blob);

  const date = new Date().toISOString().split("T")[0];
  const a = document.createElement("a");
  a.href = url;
  a.download = `${date}-mikobot.log`;
  a.click();

  URL.revokeObjectURL(url); // Speicher freigeben
}
