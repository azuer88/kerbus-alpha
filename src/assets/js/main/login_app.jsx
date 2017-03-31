require('bootstrap-loader');
// $ = require('jquery') 

var React = require('react');
var ReactDOM = require('react-dom');
var Login = require('./login');

require("../../sass/login.scss");

ReactDOM.render(<Login/>, document.getElementById('wrapper'));
