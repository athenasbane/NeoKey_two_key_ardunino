const SerialPort = require("serialport");
const Readline = require("@serialport/parser-readline");
const { spawn } = require("child_process");

/**
 * See Mac Logs in README
 */
const sysLog = spawn("/usr/bin/log", [
  "stream",
  "--predicate",
  'eventMessage CONTAINS "StartStream" || eventMessage CONTAINS "StopStream"',
  "--process",
  "zoom.us",
]);

sysLog.stdout.on("data", (data) => {
  const log = Buffer.from(data).toString();
  if (log.includes("Stop")) {
    setTimeout(() => port.write("VIDEO_OFF"), 500);
  }

  if (log.includes("Start")) {
    setTimeout(() => port.write("VIDEO_ON"), 500);
  }
});

/**
 * SerialPort opens, sends and recieves data to the arduino
 */
const port = new SerialPort("/dev/tty.usbmodem11101", {
  baudRate: 9600,
});
const parser = port.pipe(new Readline({ delimiter: "\n" }));

// Read the port data
port.on("open", () => {
  console.log("serial port open");
});

port.on("drain", (err) => {
  console.log("drained");
  console.log(err);
});
port.on("close", () => {
  console.log("serial port closed");
});
port.on("error", (err) => {
  console.log(err);
});
parser.on("data", (data) => {
  console.log("Recieved:", data);
});
