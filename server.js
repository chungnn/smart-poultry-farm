var mqtt    = require('mqtt');

var client  = mqtt.connect("mqtt://45.76.53.193");
console.log("connected flag  " + client.connected);

//handle incoming messages
client.on('message',function(topic, message, packet){
	console.log("message is "+ message);
	console.log("topic is "+ topic);
});


client.on("connect",function(){	
console.log("connected  "+ client.connected);

})
//handle errors
client.on("error",function(error){
console.log("Can't connect" + error);
process.exit(1)});
//publish
function publish(topic,msg,options){
	console.log("publishing",msg);

	if (client.connected == true){
		
	client.publish(topic,msg,options);

	}
	//count+=1;
	//if (count==10) //ens script
	//	clearTimeout(timer_id); //stop timer
	//client.end();	
}

//////////////

var options={
retain:false};
var topic="feeding";
var message="1";

console.log("subscribing to topics");
client.subscribe(topic); //single topic

//publish(topic,message,options);

//var message="0";

//notice this is printed even before we connect
console.log("end of script");

const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function ask() {
	
	rl.question('1 or 0? ', (answer) => {
		console.log("answer " + answer);
		if(parseInt(answer) < 2){
			publish(topic,answer,options);
		} else {
			publish("th",'{"temp":"20","hum":"27"}',options);
		}
		ask();
	});

}

ask();
