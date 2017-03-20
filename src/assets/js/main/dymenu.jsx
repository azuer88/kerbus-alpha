var React = require('react');

var Sidebar = require('./sidebar');
var MenuItem = require('./menuitem');

var fetcher = require('fetch-er');
var Holder = require('react-placeholder');


module.exports = React.createClass({
    handleClick: function(e) {
        alert('You click the title');
        if (this.state.group === 'default') 
            this.setState({group: 'test'})
        else
            this.setState({group: 'default'});
    },
    getInitialState: function() {
         return {
             menuready: false,
             group: 'test',
             menu: []
         } 
    },
    
    getMenuItems: function() {
       fetcher.getJSON('/menu/group/'+this.state.group+'/?format=json').then(
         ([v, s, r]) => {
           const menu = v.results;
           this.setState({ menu: menu, menuready: true });
       });
    },

    render: function() {
        this.getMenuItems()
        return (
                <Holder
                   rows={10}
                   ready={this.state.menuready}
                   className="sidebar-brand"
                   >
                   <Sidebar onTitleClick={this.handleClick}>
                      {
                        this.state.menu.map(item =>
                           <MenuItem key={item.id} href={item.link}>
                               {item.title}
                           </MenuItem>
                        )
                      }
                   </Sidebar>
                </Holder>
        );
    }
});
