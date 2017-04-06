var React = require('react');

var Sidebar = require('./sidebar');
var MenuItem = require('./menuitem');
var $ = require('jquery');

module.exports = React.createClass({
    handleClick: function(e) {
        if (this.state.prior != 0)
            this.loadMenu(this.state.prior)
        e.preventDefault();
    },
    getInitialState: function() {
         return {
             group: 0,
             prior: 0,
             title: '',
             menu: []
         } 
    },
    componentWillMount: function() {
        this.loadMenu(1);
    },
    loadMenu: function(menuid) {
        var target = menuid;
        var target_url;
        const cookie = document.cookie;
        const data = {
            cookie: cookie
        };
        if (target == null) { target = this.state.group; }
        target_url = '/menu/' + target;
        $.ajax({
            url: target_url,
            dataType: 'json',
            cache: false,
            success: function(data) {
                this.setState({
                    title: data.name,
                    prior: data.puid,
                    menu: data.items,
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
                   <Sidebar title={this.state.title} onTitleClick={this.handleClick}>
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
