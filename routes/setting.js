var express = require('express');
var router = express.Router();
const request = require('request');

/* GET home page. */
router.post('/', function(req, res, next) {
	
	var data = {"settings": []};
	if(!Array.isArray(req.body['start_at_hours[]'])){
		req.body['start_at_hours[]'] = [req.body['start_at_hours[]']];
		req.body['start_at_mins[]'] = [req.body['start_at_mins[]']];
		req.body['durations[]'] = [req.body['durations[]']];
	}
	console.log(req.body);
	for(var i = 0; i < req.body['start_at_hours[]'].length;i++){
			(function(j){
				data.settings[i] = {
					"hour": parseInt(req.body['start_at_hours[]'][i]),
					"minute": parseInt(req.body['start_at_mins[]'][i]),
					"duration": parseInt(req.body['durations[]'][i])
				}
			})(i);
	}
	console.log(JSON.stringify(data));
	request.post({
		url: 'http://45.76.53.193:8125/api/v1/chicken_farm/settings',
		body: JSON.stringify(data)
	}, function (error, response, body) {
		console.log(body);
		if (!error && response.statusCode == 200) {
			console.log(body)
		}
		res.redirect('/');
	});
	
});

module.exports = router;
