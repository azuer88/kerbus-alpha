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
            <div id="wrapper">
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
                    <div className="container-fluid">
                        <MyJumbotron>
                           <h1>Hello, there!</h1>
                           <p>This is a  sample Jumbotron</p>
                        </MyJumbotron>
                   </div>
               </div>
            </div>
        );
    }
});
