var keypress = require('keypress');

keypress(process.stdin);

process.stdin.on('keypress', function(ch, key){
  if(key.name == 'c'){
    process.stdin.on('keypress', function(ch1, key1){
      if(key1.name == 'd'){
        console.log('hello');
      }
    });
  }else if(key.ctrl && key.name == 'c'){
    process.exit();
  }
});

process.stdin.setRawMode(true);
