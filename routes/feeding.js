var express = require('express');
var router = express.Router();
const request = require('request');

/* GET home page. */
router.post('/on', function(req, res, next) {
	request.post({
		url: 'http://45.76.53.193:8125/api/v1/chicken_farm/feeding',
		body: '{"status": "OPEN"}'
	}, function (error, response, body) {
		if (!error && response.statusCode == 200) {
			console.log(body)
		}
		res.send('on');
	});
	
});

/* GET home page. */
router.post('/off', function(req, res, next) {
	request.post({
		url: 'http://45.76.53.193:8125/api/v1/chicken_farm/feeding',
		body: '{"status": "CLOSE"}'
	}, function (error, response, body) {
		if (!error && response.statusCode == 200) {
			console.log(body)
		}
		res.send('off');
	});
});

/* GET home page. */
router.get('/history', function(req, res, next) {
	request.get({
		url: 'http://45.76.53.193:8125/api/v1/chicken_farm/feeding_history',
		body: '{"status": "CLOSE"}'
	}, function (error, response, body) {
		if (!error && response.statusCode == 200) {
			console.log(body)
			res.send(body);
		}
		
	});
});


module.exports = router;
