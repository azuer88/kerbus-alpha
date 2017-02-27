var React = require('react');

var MyJumbotron = require('react-bootstrap/lib/Jumbotron');
var Sidebar = require('./sidebar');
var Alert = require('react-bootstrap').Alert;
var MenuItem = require('./menuitem');

var fetcher = require('fetch-er');

module.exports = React.createClass({
    getInitialState: function() {
         return {
             menu: []
         } 
    },
    
    componentDidMount: function() {
       fetcher.getJSON('/menuitem/?format=json').then(
         ([v, s, r]) => {
           const menu = v.results;
           this.setState({ menu: menu });
       });
    },

    render: function() {
        return (
            <div id="wrapper">
                <div id="sidebar-wrapper">
                    <Sidebar>
                       {
                         this.state.menu.map(item =>
                            <MenuItem key={item.id} href={item.link}>
                                {item.title}
                            </MenuItem>
                         )
                       }
                    </Sidebar>
                </div>
                <div id="page-content-wrapper">
                    <div className="container-fluid">
                        <MyJumbotron>
                           <h1>Hello, there!</h1>
                           <p>This is a  sample Jumbotron</p>
                        </MyJumbotron>
                        <Alert>This is an alert</Alert>
                   </div>
               </div>
            </div>
        );
    }
});
