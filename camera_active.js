const SerialPort = require("serialport");
const Readline = require("@serialport/parser-readline");
const { spawn } = require("child_process");

// Path to my qtpy yours maybe different
const portPath = "/dev/tty.usbmodem11101";

/**
 * I found that when the camera is turned on and off in zoom the is a log messages of:
 * CMIOHardware.cpp:788:CMIODeviceStopStream (45 46)
 * AND
 * CMIOHardware.cpp:738:CMIODeviceStartStream (45 46)
 *
 * log steam allows you to stream the logs as they come through filtering by process
 * and what the message contains. I haven't tested with other applications yet but if
 * you are looking to use this with other apps you could find the process name using
 * the console.app and replace "zoom.us" with it or remove both --process and zoom.us
 * from the array of arguments below if you are looking for it to be app agnostic
 *
 * Note: I use a usb webcam if you are having issues with the macbook native camera
 * you may need to look and see if the message is different for it in logs
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
 * SerialPort opens, sends and recieves data to the QTPY
 */
const port = new SerialPort(portPath, {
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
