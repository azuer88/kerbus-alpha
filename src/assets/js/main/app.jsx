var React = require('react');

var MyJumbotron = require('react-bootstrap/lib/Jumbotron');

var Alert = require('react-bootstrap').Alert;

module.exports = React.createClass({
    render: function() {
        return <MyJumbotron><h1>Hello, there!</h1><p>This is a  sample Jumbotron</p></MyJumbotron>
    }
});
