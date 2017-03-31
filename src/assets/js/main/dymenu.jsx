var React = require('react');

var Sidebar = require('./sidebar');
var MenuItem = require('./menuitem');
var $ = require('jquery');

module.exports = React.createClass({
    handleClick: function(e) {
        if (this.state.group.toUpperCase() === 'DEFAULT') 
            this.loadMenu('Test')
        else
            this.loadMenu('Default');
        e.preventDefault();
    },
    getInitialState: function() {
         return {
             group: 'Default',
             menu: []
         } 
    },
    componentWillMount: function() {
        this.loadMenu();
    },
    loadMenu: function(name) {
        var target = name;
        var target_url;
        const cookie = document.cookie;
        const data = {
            cookie: cookie
        };
        if (target == null) { target = this.state.group; }
        target_url = '/menu/group/'+target+'/?format=json';
        $.ajax({
            url: target_url,
            dataType: 'json',
            cache: false,
            success: function(data) {
                this.setState({
                    menu: data.results,
                    group: target
                });
            }.bind(this),
            error: function(xhr, st, err) {
                alert("Unable to load menu\nReason: "+err.toString());
                window.location = this.props.loginURL;
            }.bind(this),
        });
    },
    render: function() {
        return (
                   <Sidebar title={this.state.group} onTitleClick={this.handleClick}>
                      {
                        this.state.menu.map(item =>
                           <MenuItem key={item.id} href={item.link} load={item.load} loader={this.loadMenu}>
                               {item.title}
                           </MenuItem>
                        )
                      }
                   </Sidebar>
        );
    }
});
