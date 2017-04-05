var React = require('react');
var $ = require('jquery');
var Login = require('./login');

var LoginPage = React.createClass({
    render: function() {
        return (
            <div className="container-fluid">
                <div id="page-content-wrapper">
                    <Login />
                </div>
            </div>
        );
    }
});

module.exports = LoginPage
