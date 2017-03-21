var React = require('react');

var Sidebar = require('./sidebar');
var MenuItem = require('./menuitem');

var fetcher = require('fetch-er');
var Holder = require('react-placeholder');


module.exports = React.createClass({
    handleClick: function(e) {
        if (this.state.group === 'default') 
            this.loadMenu('test')
        else
            this.loadMenu('default');
        return false;
    },
    getInitialState: function() {
         return {
             group: 'test',
             menu: []
         } 
    },
    componentWillMount: function() {
        this.loadMenu();
    },
    loadMenu: function(name) {
        var target = name;
        if (target == null) { target = this.state.group; }
        fetcher.getJSON('/menu/group/'+target+'/?format=json').then(
                ([v, s, r]) => {
                    const menu = v.results;
                    this.setState({ menu: menu, group: target });
                }
                );
    },
    render: function() {
        return (
                   <Sidebar title={this.state.group} onTitleClick={this.handleClick}>
                      {
                        this.state.menu.map(item =>
                           <MenuItem key={item.id} href={item.link}>
                               {item.title}
                           </MenuItem>
                        )
                      }
                   </Sidebar>
        );
    }
});
