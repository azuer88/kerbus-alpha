var React = require('react');

var MyJumbotron = require('react-bootstrap/lib/Jumbotron');

var Alert = require('react-bootstrap').Alert;

module.exports = React.createClass({
    render: function() {
        return <div><MyJumbotron><h1>Hello, there!</h1><p>This is a  sample Jumbotron</p></MyJumbotron><Alert>This is an alert</Alert></div>
    }
});
