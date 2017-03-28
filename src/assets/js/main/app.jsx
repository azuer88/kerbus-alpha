var React = require('react');

var MyJumbotron = require('react-bootstrap/lib/Jumbotron');
var DynMenu = require('./dymenu');
var LoginButton = require('./login');

var $ = require('jquery');

module.exports = React.createClass({
    onButtonClick: function(ev) {
        var login = $('#loginModal');
        login.open();
        ev.preventDefault();

    },
    onLoginSubmit: function() {
        console.log("submit handler called");
    },
    render: function() {
        return (
            <div>
                <div id="sidebar-wrapper">
                   <DynMenu group="default"/>
                </div>
                <div id="page-content-wrapper">
                        <MyJumbotron>
                           <div className="container-fluid">
                              <h1>Hello, there!</h1>
                              <p>This is a  sample Jumbotron</p>
                              <p>Dolor ipsum porta.
                              Lacus class netus a amet morbi tellus sociis purus per quis phasellus.
                              Morbi augue.</p>
                              <p>Lacus purus aptent nullam purus est.</p>
                              <p>Etiam magna mauris vitae eget ut tincidunt aliquam duis rutrum venenatis eni inceptos.</p>
                              <p>Donec nulla purus montes porta morbi quis ante nunc purus...</p>

                              <p><a href="#" target="_blank" className="btn btn-success btn-lg" onClick={this.onButtonClick}>Get started today</a></p>
                              <LoginButton refId="login-dialog-1" submitHandler={this.onLoginSubmit}></LoginButton>
                            </div>
                        </MyJumbotron>
               </div>
            </div>
        );
    }
});

