var React = require('react');

var MyJumbotron = require('react-bootstrap/lib/Jumbotron');
var Sidebar = require('./sidebar');
var MenuItem = require('./menuitem');

var fetcher = require('fetch-er');
var Holder = require('react-placeholder');

module.exports = React.createClass({
    getInitialState: function() {
         return {
             menuready: false,
             menu: []
         } 
    },
    
    componentDidMount: function() {
       fetcher.getJSON('/menuitem/?format=json').then(
         ([v, s, r]) => {
           const menu = v.results;
           this.setState({ menu: menu, menuready: true });
       });
    },

    render: function() {
        return (
            <div>
                <div id="sidebar-wrapper">
                    <Holder
                       rows={10}
                       ready={this.state.menuready}
                       className="sidebar-brand"
                    >
                       <Sidebar>
                          {
                            this.state.menu.map(item =>
                               <MenuItem key={item.id} href={item.link}>
                                   {item.title}
                               </MenuItem>
                            )
                          }
                       </Sidebar>
                    </Holder>
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

                              <p><a href="#" target="_blank" className="btn btn-success btn-lg">Get started today</a></p>
                           </div>
                        </MyJumbotron>
               </div>
            </div>
        );
    }
});
