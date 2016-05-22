// var SerialPort = require('serialport').SerialPort;
// var port = new SerialPort('/dev/tty-usbmodem1411');
var google_speech = require('google-speech');

google_speech.ASR({
  developer_key : 'AIzaSyCYQgmfJrYQH2fn1lwgkX7AdETbWtOeKNE',
  file : 'test.mp3'
}, function(err, resp, xml){
  console.log(resp.statusCode, xml);
});
