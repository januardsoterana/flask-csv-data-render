$(document).ready(function() {

	// Bar Chart
	
	Morris.Bar({
		element: 'bar-charts',
		data: [
			{ y: 'Jan',  b: 3 },
			{ y: 'Feb', b: 3 },
			{ y: 'Mar', b: 2 },
			{ y: 'Apr', b: 5 },
			{ y: 'May',  b: 2 },
			{ y: 'Jun',  b: 3 }
		],
		xkey: 'y',
		ykeys: ['b'],
		labels: ['New Drivers'],
		lineColors: ['#0253cc'],
		lineWidth: '3px',
		barColors: ['#0253cc'],
		resize: true,
		redraw: true,
		parseTime: false
	});
	
	// Line Chart
	
	Morris.Line({
		element: 'line-charts',
		data: [
			{ y: "Jan",  a: 7,  b: 7 },
			{ y: "Feb", a: 4,  b: 6 },
			{ y: "Mar", a: 3,  b: 5 },
			{ y: "Apr", a: 1,  b: 6 },
			{ y: "May", a: 2,  b: 6 },
			{ y: "Jun", a: 5, b: 7 }
		],
		xkey: 'y',
		ykeys: ['a', 'b'],
		labels: ['Actual Quits', 'Predicted Quits'],
		lineColors: ['#0253cc', '#00c5fb'],
		lineWidth: '3px',
		resize: true,
		redraw: true,
		parseTime: false
	});
		
});