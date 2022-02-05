import React, {Component} from 'react';
import {Link} from "react-router-dom";
import {Menu} from 'antd';
import menuList from "../../config/menu_config";

const { SubMenu } = Menu;

class LeftMenu extends Component {

    //创建菜单
    createMenu=(mList)=>{
        return mList.map((item)=>{
            if(!item.children){
                return(
                    <Menu.Item key={item.key} icon={<item.icon />} onClick={()=>{this.save(item.title)}}>
                        <Link to={item.path}>
                            {item.title}
                        </Link>
                    </Menu.Item>
                )
            }
            else{
                return (
                    <SubMenu key={item.key} icon={<item.icon />} title={item.title}>
                        {this.createMenu(item.children)}
                    </SubMenu>
                )
            }
        })
    }

    render() {
        return (
            <Menu
                // defaultSelectedKeys={this.props.location.pathname.split('/').reverse()[0]}
                // defaultOpenKeys={this.props.location.pathname.split('/').splice(2)}
                mode="inline"
                theme="light"
                style={{height:'100%'}}
            >
                {this.createMenu(menuList)}
            </Menu>
        );
    }
}

export default LeftMenu;
