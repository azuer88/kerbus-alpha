var React = require('react');
var $ = require('jquery');

module.exports = React.createClass({
    onLoginSubmit: function() {
        console.log("submit handler called");
    },
    render: function() {
        return (
            <div>
                <div id="page-content-wrapper">
                           <div className="container-fluid">
                              <h1>Hello, there!</h1>
                              <p>This is a  sample Jumbotron</p>
                              <p>Dolor ipsum porta.
                              Lacus class netus a amet morbi tellus sociis purus per quis phasellus.
                              Morbi augue.</p>
                              <p>Lacus purus aptent nullam purus est.</p>
                              <p>Etiam magna mauris vitae eget ut tincidunt aliquam duis rutrum venenatis eni inceptos.</p>
                              <p>Donec nulla purus montes porta morbi quis ante nunc purus...</p>

                            </div>
               </div>
            </div>
        );
    }
});

